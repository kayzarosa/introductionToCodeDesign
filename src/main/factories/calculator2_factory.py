from flask import request as FlaskRequest
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler


def calculator2_factory(request: FlaskRequest):  # type: ignore
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    response = calc.calculate(request)
    return response
