import os
import pytest
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 1) == 1

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)

def test_save_and_load_history(tmpdir):
    calc = Calculator()
    calc.add(1, 2)
    calc.subtract(5, 3)
    calc.multiply(2, 4)
    calc.divide(8, 2)

    # Save history
    history_file = os.path.join(tmpdir, 'history.csv')
    calc.save_history(history_file)

    # Create a new calculator instance and load history
    new_calc = Calculator()
    new_calc.load_history(history_file)

    # Check if history is correctly loaded
    assert len(new_calc.history) == 4
    assert new_calc.history.iloc[0]['operation'] == 'add'
    assert new_calc.history.iloc[1]['operation'] == 'subtract'
    assert new_calc.history.iloc[2]['operation'] == 'multiply'
    assert new_calc.history.iloc[3]['operation'] == 'divide'
