# Sistema de Gestión - Servicio Diesel (API REST)

Este proyecto es una API REST completa desarrollada con **Django REST Framework** para la gestión digital de un taller especializado en inyección diésel y mecánica.

El sistema está diseñado para resolver una necesidad real: administrar tanto el ingreso de vehículos completos como trabajos de laboratorio (banco de pruebas para bombas e inyectores sueltos).

## Características Principales

* **Gestión Híbrida de Órdenes:** Permite crear mantenciones asociadas a un vehículo (con patente y kilometraje) o a piezas sueltas (sin vehículo obligatorio).
* **Control de Áreas:** Diferenciación entre trabajos de "Patio Mecánica" y "Laboratorio Diésel".
* **Seguridad:** Autenticación robusta mediante **Tokens** para proteger la información sensible.
* **Filtros Avanzados:** Búsqueda de trabajos por rango de fechas, kilometraje, tipo de servicio y estado.
* **Documentación Automática:** Integración con Swagger y Redoc para explorar la API visualmente.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework:** Django 5.x
* **API Toolkit:** Django REST Framework (DRF)
* **Documentación:** drf-yasg (Swagger)
* **Base de Datos:** SQLite (Entorno de desarrollo)

##  Instalación y Ejecución

Si deseas clonar y correr este proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/backend_taller_diesel.git](https://github.com/TU_USUARIO/backend_taller_diesel.git)
    cd backend_taller_diesel
    ```

2.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Correr el servidor:**
    ```bash
    python manage.py runserver
    ```

## 📖 Documentación de la API

Una vez iniciado el servidor, puedes ver los endpoints disponibles en:
* **Swagger UI:** `http://127.0.0.1:8000/swagger/`
* **API Root:** `http://127.0.0.1:8000/api/`

---
*Proyecto desarrollado para la evaluación final de Programación Backend - 2025.*
Daniel Jara Palma.