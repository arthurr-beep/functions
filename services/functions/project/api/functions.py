from flask import Blueprint, jsonify, request, Response
import redis
from project.services.functions_service import fibonacci, factorial, Ackerman

# connect to redis
client = redis.Redis(host="redis", port=6379)


functions_blueprint = Blueprint("functions", __name__)


# UnComment Below to allow Prometheus fetch metrics via the below endpoint

# @functions_blueprint.route("/functions/metrics", methods=["GET"])
# def functions_metrics():
#     """export metrics
#     Returns:
#         [type]: [description]
#     """
#     MIME_TYPE = str("text/plain; version=0.0.4; charset=utf-8")

#     return Response(prometheus_client.generate_latest(), mimetype=MIME_TYPE)


@functions_blueprint.route("/functions/test", methods=["GET"])
def check_server():
    """Check Server is up

    Returns:
        [type]: [description]
    """
    return jsonify({"status": True, "message": "Running!!!"}), 200


@functions_blueprint.route("/functions/fibonacci/<number>", methods=["GET"])
def compute_fibonacci(number: int):
    """Fibonacci Computation"""

    try:
        key = int(number)

        if not non_negative(key):
            return (
                jsonify(
                    {
                        "status": "failed",
                        "error": f"input {key} must be greater than zero",
                    }
                ),
                400,
            )

        if client.exists(f"fib({key})"):
            return (
                jsonify(
                    {
                        "status": "success",
                        "result": int(client.get(f"fib({key})").decode("utf-8")),
                    }
                ),
                200,
            )

        result = fibonacci(key)

        client.set(f"fib({key})", result)
        return jsonify({"status": "success", "result": result}), 200

    except ValueError as ex:
        return (
            jsonify(
                {
                    "status": "failed",
                    "error": f"input {number} must be a valid integer ",
                }
            ),
            400,
        )


@functions_blueprint.route("/functions/factorial/<number>", methods=["GET"])
def compute_factorial(number: int):
    """Factorial Computation

    Args:
        number (int): [positive integer]
    """

    try:

        key = int(number)

        if not non_negative(key):
            return (
                jsonify(
                    {
                        "status": "failed",
                        "error": f"input {key} must be greater than zero",
                    }
                ),
                400,
            )

        elif client.exists(f"fac({key})"):
            return (
                jsonify(
                    {
                        "status": "success",
                        "result": int(client.get(f"fac({key})").decode("utf-8")),
                    }
                ),
                200,
            )

        fact = factorial(key)
        client.set(f"fac({key})", fact)
        return jsonify({"status": "success", "result": fact}), 200

    except ValueError as ex:
        return (
            jsonify(
                {
                    "status": "failed",
                    "error": f"input {number} must be a valid integer",
                }
            ),
            400,
        )


@functions_blueprint.route(
    "/functions/ackerman/<first_number>/<second_number>", methods=["GET"]
)
def compute_ackerman(first_number: int, second_number: int) -> int:
    """Compute Ackerman Function

    Args:
        first_number (int): First Parameter
        second_number (int): Second Parameter

    Returns:
        int: Compute Result
    """

    try:

        first_key = int(first_number)
        second_key = int(second_number)

        if not non_negative(first_key):
            return (
                jsonify(
                    {
                        "status": "failed",
                        "error": f"input {first_key} must be greater than zero",
                    }
                ),
                400,
            )

        if not non_negative(second_key):
            return (
                jsonify(
                    {
                        "status": "failed",
                        "error": f"input {second_key} must be greater than zero",
                    }
                ),
                400,
            )

        elif client.exists(f"ack({first_key, second_key})"):
            return (
                jsonify(
                    {
                        "status": "success",
                        "result": int(
                            client.get(f"ack({first_key, second_key})").decode("utf-8")
                        ),
                    }
                ),
                200,
            )

        ackerman = Ackerman().compute(first_key, second_key)

        client.set(f"ack({first_key, second_key})", ackerman)
        return jsonify({"status": "success", "result": ackerman}), 200

    except ValueError as ex:
        return (
            jsonify(
                {
                    "status": "failed",
                    "error": f"{str(ex)}",
                }
            ),
            400,
        )


def non_negative(number: int) -> bool:
    """Checks if An Integer is non negative and greater than 0

    Args:
        number (int): [description]

    Returns:
        bool: [description]
    """

    if number <= 0:
        return False
    return True
