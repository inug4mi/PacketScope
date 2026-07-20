from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

# Configuración de la aplicación
APP_NAME = os.getenv("APP_NAME", "PacketScope")
DEBUG = os.getenv("DEBUG", "False") == "True"
DATABASE_URL = os.getenv("DATABASE_URL")