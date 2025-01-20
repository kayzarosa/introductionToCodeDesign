from src.calculators.calculator_1 import Calculator1
from flask import request as FlaskRequest


def calculator1_factory(request: FlaskRequest):  # type: ignore
    calc = Calculator1()
    response = calc.calculate(request)
    return response
