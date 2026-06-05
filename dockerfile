#paso 1 buscar iamgen base
FROM python:3.12-alpine3.22

#paso 2 crear el directorio de trabajo en el contenedor
WORKDIR /app

#paso 3 copiar el archivo de dependencias
COPY requirements.txt /app

#paso 4 instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#paso5 copiar el codigo fuente
COPY app.py /app

#paso6 exponer el puerto 5000
EXPOSE 5000

#paso7 ejecutar la aplicacion
CMD [ "python", "app.py" ]