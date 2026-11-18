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
