from typing import Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        media = self.__driver_handler.media(input_data)

        return self.__format_response(media)

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"Calculator": 4, "result": round(calc_result, 2)}}
