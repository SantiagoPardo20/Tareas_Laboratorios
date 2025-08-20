# Parte B — Notas del Paquete `miniutils`

## Absolutas vs relativas
- **Absolutas (`from paquete.modulo import`)**: recomendadas para consumidores externos.
- **Relativas (`from .otro_modulo import`)**: útiles dentro del mismo paquete.

## __init__.py
Reexporta: `normalize`, `is_valid_slug`, `format_title`, `days_between`, `parse_date`, `format_iso`.
Motivo: dar una API simple sin exponer detalles internos.

## Referencia
[Packages — Python 3.12 Docs](https://docs.python.org/3.12/tutorial/modules.html#packages)
