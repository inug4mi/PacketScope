from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

# Configuración de la aplicación
APP_NAME = os.getenv("APP_NAME", "PacketScope")
DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASE_URL = os.getenv("DATABASE_URL")

# JWT
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "cambia-esta-clave-en-producción"
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv(
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    "30"
))