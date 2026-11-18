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

## Formulario (`templates/index.html`)

Envía los datos a `/prestar-equipo` con el método `POST`.

**Campos:**
- `nombre` (string): nombre del estudiante.
- `equipo` (string): `Router Cisco`, `Laptop de Pruebas` o `Multímetro Digital`.
- `adeudos` (bool): `Si` / `No`.
- `semestre` (int): semestre que cursa.

**Resultado:**
- Si `aprobado` es verdadero, muestra el `folio`.
- Si `aprobado` es falso, muestra el `motivo` del rechazo.


**Notas:**
- `nombre`: input text, `equipo`: select, `adeudos`: radio, `semestre`: input number (min 1).
- Todos los campos llevan `required`.
- Los `value` deben ser exactos a los que valida `app.py`.
- El resultado se muestra en el mismo `index.html` con `{% if aprobado %}`.
