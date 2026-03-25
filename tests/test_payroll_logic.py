from types import SimpleNamespace


def calculate_overtime_amount(hours: float, rate: float) -> float:
    return round(hours * rate, 2)


def test_calculate_overtime_amount():
    assert calculate_overtime_amount(3.5, 8) == 28.0
    assert calculate_overtime_amount(0, 10) == 0
