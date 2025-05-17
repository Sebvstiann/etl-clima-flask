from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import db_config

# Crear motor de conexión PostgreSQL usando SQLAlchemy
engine = create_engine(
    f"postgresql+psycopg2://{db_config['usuario']}:{db_config['password']}@{db_config['host']}:{db_config['puerto']}/{db_config['base_datos']}"
)
Session = sessionmaker(bind=engine)

def guardar_datos_postgres(data):
    session = Session()
    sql = text("""
        INSERT INTO clima 
        (temperatura_celsius, velocidad_viento_kmh, winddirection, weathercode, descripcion_clima, time_utc, extracted_at)
        VALUES (:temp, :vel_viento, :dir_viento, :weathercode, :descripcion, :time_utc, :extracted_at)
    """)
    params = {
        "temp": data.get("temperature"),
        "vel_viento": data.get("windspeed"),
        "dir_viento": data.get("winddirection"),
        "weathercode": data.get("weathercode"),
        "descripcion": data.get("descripcion_clima"),
        "time_utc": data.get("time"),
        "extracted_at": data.get("extracted_at")
    }
    session.execute(sql, params)
    session.commit()
    session.close()

def obtener_ultimo_registro():
    session = Session()
    sql = text("SELECT * FROM clima ORDER BY id DESC LIMIT 1")
    result = session.execute(sql).fetchone()
    session.close()
    return result

def obtener_todos_los_registros():
    session = Session()
    sql = text("SELECT * FROM clima ORDER BY id DESC")
    result = session.execute(sql).fetchall()
    session.close()
    return result


from sqlalchemy import Column, Integer, Float, String, Table, MetaData, TIMESTAMP

metadata = MetaData()

clima_table = Table(
    "clima",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("temperatura_celsius", Float),
    Column("velocidad_viento_kmh", Float),
    Column("winddirection", Integer),
    Column("weathercode", Integer),
    Column("descripcion_clima", String(50)),
    Column("time_utc", TIMESTAMP),
    Column("extracted_at", TIMESTAMP),
)


metadata.create_all(engine)
