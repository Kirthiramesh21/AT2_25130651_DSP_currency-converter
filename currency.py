def _fmt_rate(x: float) -> str:
    return f"{x:.6f}".rstrip("0").rstrip(".")

def _fmt_amount(x: float) -> str:
    return f"{x:.2f}"

def format_conversion_text(dt: str, from_code: str, to_code: str, rate: float, amount: float):
    converted = amount * rate
    inverse = 1.0 / rate
    text = (
        f"The conversion rate on {dt} from {from_code} to {to_code} was {_fmt_rate(rate)}. "
        f"So {_fmt_amount(amount)} in {from_code} correspond to {_fmt_amount(converted)} in {to_code}. "
        f"The inverse rate was {_fmt_rate(inverse)}."
    )
    return text, converted, inverse
