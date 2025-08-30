from datetime import datetime, date
from .strings import collapse_spaces   # importación relativa

__all__ = ["parse_date", "days_between", "format_iso"]


def parse_date(s: str, fmt: str = "%Y-%m-%d") -> date:
    s = collapse_spaces(s)
    return datetime.strptime(s, fmt).date()


def days_between(a: str, b: str, fmt: str = "%Y-%m-%d") -> int:
    da = parse_date(a, fmt)
    db = parse_date(b, fmt)
    return abs((db - da).days)


def format_iso(d: date | datetime) -> str:
    if isinstance(d, datetime):
        return d.isoformat(timespec="seconds")
    elif isinstance(d, date):
        return d.isoformat()
    else:
        raise TypeError("format_iso espera date o datetime")
