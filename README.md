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

Recibe los datos del formulario HTML (`application/x-www-form-urlencoded`), aplica las reglas en orden y devuelve `index.html` con el resultado.

**Parámetros:**
- `nombre` (string): nombre del estudiante.
- `equipo` (string): `Router Cisco`, `Laptop de Pruebas` o `Multímetro Digital`.
- `adeudos` (string): `Si` / `No`.
- `semestre` (int): semestre que cursa.

**Reglas:**
1. `adeudos = Si`: se rechaza sin importar el equipo.
2. `equipo = Laptop de Pruebas` y `semestre < 4`: se rechaza por política de seguridad.
3. Si pasa las anteriores: se aprueba y genera un folio único (`LAB-XXXXXXXX`).

**Respuesta:**
- Aprobado: `aprobado = True`, `nombre`, `equipo`, `folio`.
- Rechazado: `aprobado = False`, `nombre`, `equipo`, `motivo`.

---

## Formulario (`templates/index.html`)

Envía los datos a `/prestar-equipo` con el método `POST`.

**Resultado:**
- Si `aprobado` es verdadero, muestra el `folio`.
- Si `aprobado` es falso, muestra el `motivo` del rechazo.

**Notas:**
- `nombre`: input text, `equipo`: select, `adeudos`: radio, `semestre`: input number (min 1).
- Todos los campos llevan `required`.
- Los `value` deben ser exactos a los que valida `app.py`.
- El resultado se muestra en el mismo `index.html` con `{% if aprobado %}`.
