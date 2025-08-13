# 1. Imagen base: Empezamos con una que ya tiene Python
FROM python:3.9-slim

# 2. Directorio de trabajo: Creamos una carpeta /app y nos metemos en ella
WORKDIR /app

# 3. Copiar archivos: Copiamos los requisitos primero
COPY requirements.txt .

# 4. Instalar dependencias: Ejecutamos pip para instalar Flask
RUN pip install -r requirements.txt

# 5. Copiar el resto de la app
COPY . .

# 6. Comando final: El comando para ejecutar la app cuando el contenedor arranque
CMD ["flask", "run", "--host=0.0.0.0"]
