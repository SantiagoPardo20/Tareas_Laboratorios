from miniutils.strings import normalize, is_valid_slug
from miniutils.datetime_utils import days_between, parse_date
from miniutils import format_title, format_iso

def demo():
    print("== Parte B: Uso del paquete miniutils ==")
    print("normalize:", normalize("  Café  con  Leche  "))
    print("format_title:", format_title(" introducción al desarrollo con python "))
    print("is_valid_slug('python-312'):", is_valid_slug("python-312"))
    print("days_between('2024-12-31', '2025-01-02'):", days_between("2024-12-31", "2025-01-02"))

    d = parse_date(" 2025-08-20 ")
    print("format_iso(parse_date(...)):", format_iso(d))


if __name__ == "__main__":
    demo()
