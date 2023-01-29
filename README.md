# README

## Descripción del proyecto
Este código es una prueba técnica para GA-Tech-Solutions para la posición de desarrollador python jr. Se utiliza SQLite con los módulos del núcleo de python, 
además de FastAPI, Uvicorn y Requests.

## Requisitos
Para poder ejecutar este proyecto es necesario tener instalado:
- FastAPI
- Uvicorn
- Requests

Además, el proyecto ya incluye un entorno virtual llamado "fastAPI-GA", por lo que se describe a continuación cómo activarlo en los distintos sistemas operativos:

### Windows

```
python -m venv fastAPI-GA
fastAPI-GA\Scripts\activate
```

### Linux/Mac

```
python3 -m venv fastAPI-GA
source fastAPI-GA/bin/activate
```

## Ejecutar Uvicorn
Una vez activado el entorno virtual, ejecutar el siguiente comando:

```
uvicorn main:app --reload
```

Puedes acceder a la documentación de la API a través del localHost y el puerto utilizado (normalmente 8000) utilizando un enlace de la forma:
http://127.0.0.1:8000/docs

## CLI para ingreso de usuario y contraseña
Para ejecutar el código cli.py, que es una app de consola para pedir el usuario y contraseña y recibir la respuesta de la API, utilizar el siguiente comando:

```
python cli.py
```

### Nota
Asegúrese de tener la base de datos creada antes de ejecutar el código, en caso contrario, modifique el archivo models.py para crear la base de datos según 
sus necesidades.

## Enlaces de utilidad

- SQLite: https://www.sqlite.org/
- FastAPI: https://fastapi.tiangolo.com/



