# Tarea 3.0 — CI/CD con GitHub Actions y Docker IP

Aplicación sencilla en Python con flujo de CI/CD automatizado usando GitHub Actions y Docker.

---

## Requisitos

- Python 3.11+
- Docker

---

## Ejecución local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app/main.py

# Ejecutar pruebas
pytest tests/ -v
```

## Ejecución con Docker

```bash
docker build -t ejercicio:3.0.0 .
docker run --rm ejercicio:3.0.0
```

---

## CI/CD

El workflow `.github/workflows/python-application.yml` se ejecuta automáticamente en cada `push` y realiza:

1. Descarga del código fuente
2. Instalación de dependencias
3. Ejecución de pruebas
4. Ejecución de la aplicación
5. Simulación de despliegue
6. Build de imagen Docker
7. Autenticación en GHCR
8. Publicación de la imagen

---

## Autor

**Nombre:** `<Tu Nombre>`  
**Materia:** DevOps / CI-CD  
**Período:** 2025
