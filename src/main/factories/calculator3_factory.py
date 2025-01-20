from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3


def calculator3_factory(request: FlaskRequest):  # type: ignore
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    response = calc.calculate(request)
    return response
