from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator4_factory import calculator4_factory
from src.errors.error_controller import handler_errors

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        response = calculator1_factory(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        response = calculator2_factory(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        response = calculator3_factory(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        response = calculator4_factory(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]
