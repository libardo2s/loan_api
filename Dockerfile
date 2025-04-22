# Usar imagen oficial de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Puerto expuesto
EXPOSE 8000

# Comando para ejecutar (se sobrescribirá en docker-compose)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]