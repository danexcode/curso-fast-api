import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
Resumen:
    Nº1: 
        Se crea la url de coneccion: "postgres://user:password@host:port/database"
    
    Nº2:
        Se crea el motor: engine = create_engine(URI)
        
    Nº3:
        Se crea la sesion: SessionLocal = sessionmaker(bind=engine)
        
    Nº4:
        Se crea la base para manipular las tablas: Base = declarative_base()
"""

# Se guardara el nombre de la base de datos
sqlite_file_name = "../database.sqlite"

# Se leera el directorio actual del archivo database
base_dir = os.path.dirname(os.path.realpath(__file__))

# sqlite:/// es la forma en la que se conecta a una 
# base de datos, se usa el metodo join para unir las urls
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# representa el motor de la base de datos, 
# con el comando “echo=True” para que al momento 
# de realizar la base de datos,
# me muestre por consola lo que esta realizando, que seria el codigo
engine = create_engine(database_url, echo=True)

# Se crea session para conectarse a la base de datos, 
# se enlaza con el comando “bind” y se iguala a engine
Session = sessionmaker(bind=engine)

# Sirve para manipular todas las tablas de la base de datos
Base = declarative_base()
