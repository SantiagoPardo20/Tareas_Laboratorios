from cadenas_utils import normalize, is_valid_slug, format_title, require_non_empty

def demo():
    print("== Parte A: Uso de cadenas_utils ==")

    original = "   ¡Hola  MÚNDO   de  PYTHON!  "
    print("Original:", repr(original))
    print("normalize:", normalize(original))

    titulo = "  introducción al diseño de software con Python  "
    print("format_title:", format_title(titulo))

    for s in ["curso-python", "curso--python", "Curso-Python", "curso123", "curso python"]:
        print(f"is_valid_slug({s!r}) ->", is_valid_slug(s.lower()))

    # Caso límite
    try:
        require_non_empty("   \t  ")
    except ValueError as e:
        print("Caso límite OK -> ValueError capturado:", e)


if __name__ == "__main__":
    demo()
