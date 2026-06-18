import pytest

def calculate_actual_pay(player_dict):
    status = player_dict.get("status")
    base_salary = float(player_dict.get("salary", 0.0))
    if status == "Active":
        return base_salary
    elif status == "Benched":
        return base_salary * 0.5
    return 0.0


def test_calculate_pay_active():
    player_active = {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active",
    }
    assert calculate_actual_pay(player_active) == 5000.0

def test_calculate_pay_benched():
    player_benched = {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched",
    }
    assert calculate_actual_pay(player_benched) == 3000.0