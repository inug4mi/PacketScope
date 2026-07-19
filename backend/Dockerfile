# Imagen base
FROM python:3.13-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY app ./app

# Puerto que usará FastAPI
EXPOSE 8000

# Comando que inicia la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]