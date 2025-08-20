# Parte A — Notas del Módulo `cadenas_utils`

## API pública
- `normalize(texto) -> str`
- `is_valid_slug(texto) -> bool`
- `format_title(texto) -> str`
- `require_non_empty(texto) -> str`

## Motivo
Agrupa utilidades de cadenas reutilizables, separando lógica de validación y formateo del código principal.

## Caso límite
`require_non_empty("   \t  ")` → lanza `ValueError` (controlado en main_a).

## Referencia
[Modules — Python 3.12 Docs](https://docs.python.org/3.12/tutorial/modules.html)
