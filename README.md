
# 🌦️ ETL Clima Maullín

Este proyecto implementa un proceso ETL (Extract, Transform, Load) en Python que obtiene datos meteorológicos en tiempo real de la comuna de **Maullín, Chile** mediante la API pública de [Open-Meteo](https://open-meteo.com/en/docs), los transforma y los carga en una base de datos MySQL.

---

## 🚀 Estructura del Proyecto

```
tiempo/
├── main.py              # Ejecuta el proceso ETL completo
├── config.py            # Configuración de conexión a la base de datos
└── etl/
    ├── extract.py       # Obtención de datos desde la API
    ├── transform.py     # Limpieza y enriquecimiento de los datos
    └── load.py          # Inserción en MySQL
```

---

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- Pandas
- Requests
- SQLAlchemy
- MySQL / MariaDB
- API pública de Open-Meteo

---

## 🧪 Cómo ejecutar

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/etl-clima-maullin.git
cd etl-clima-maullin
```

### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

> Puedes crear un archivo `requirements.txt` con:
> ```
> pandas
> requests
> mysql-connector-python
> SQLAlchemy
> ```

### 3. Configura tu conexión en `config.py`

```python
db_config = {
    "usuario": "root",
    "password": "tu_contraseña",
    "host": "localhost",
    "puerto": "3306",
    "base_datos": "etl_datos"
}
```

### 4. Ejecuta el ETL

```bash
python main.py
```

---

## 🧾 Estructura de la tabla MySQL

Asegúrate de tener la base y tabla creadas con:

```sql
CREATE DATABASE etl_datos;

USE etl_datos;

CREATE TABLE clima (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperatura_celsius FLOAT,
    velocidad_viento_kmh FLOAT,
    winddirection INT,
    weathercode INT,
    descripcion_clima VARCHAR(50),
    time_utc DATETIME,
    extracted_at DATETIME
);
```

---

## 📈 Ejemplo de resultado

| temperatura_celsius | velocidad_viento_kmh | winddirection | weathercode | descripcion_clima | time_utc           | extracted_at         |
|---------------------|----------------------|---------------|-------------|-------------------|---------------------|-----------------------|
| 12.3                | 20.1                 | 180           | 63          | Lluvia moderada   | 2025-05-17 03:00:00 | 2025-05-17 00:00:15   |

---

## 📚 Aprendizajes clave

- Consumir una REST API
- Procesar y enriquecer datos con `pandas`
- Cargar información estructurada a un `data warehouse` (MySQL)
- Aplicar buenas prácticas de modularización en proyectos ETL

---

## 📌 Autor

**Sebastián Jesús Schafer Calisto**  
Estudiante de Ingeniería en Informática – INACAP  
📧 schafer.calisto2001@gmail.com

---

## 📝 Licencia

Este proyecto es de uso libre para fines educativos y demostrativos.
