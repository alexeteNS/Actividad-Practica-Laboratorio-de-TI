# Lab TI – Sistema de Préstamo de Equipos

Este proyecto automatiza el préstamo de equipos (laptops, multímetros y routers de prácticas) en el laboratorio de redes y hardware de la carrera de **Ingeniería en Tecnologías de la Información**.

---

## Estructura del proyecto

```
lab_ti/
  app.py
  templates/
    index.html
  README.md
```

---


## Instalación y ejecución

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
Linux: source venv/bin/activate | Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install flask

# 3. Ejecutar el servidor
python app.py
```

Después abre en el navegador: **http://127.0.0.1:5000/**



---

## Endpoints

`GET`  : `/`               | Muestra el formulario de solicitud de préstamo.
`POST` : `/prestar-equipo` | Procesa la solicitud y devuelve el resultado.

### `POST /prestar-equipo`

Recibe los datos del formulario HTML (`application/x-www-form-urlencoded`).


**Parámetros:**
- `nombre` (string): nombre del estudiante.
- `equipo` (string): `Router Cisco`, `Laptop de Pruebas` o `Multímetro Digital`.
- `adeudos` (bool): `Si` / `No`.
- `semestre` (int): semestre que cursa.

**Respuesta:**
- Aprobado: muestra el folio único de autorización.
- Rechazado: muestra el motivo.

