from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def media(self, numbers: List[float]) -> float:
        return 100


def test_calculate():
    mock_request = MockRequest(body={"numbers": [90, 8, 10, 192, 253.90]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 100
    assert response["data"]["Calculator"] == 4


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
