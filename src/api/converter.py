from flask import Blueprint, request

from src.external.exchangerate import ExchangerateClient

blueprint = Blueprint('converter', __name__)


@blueprint.route('/convert_currency')
def convert_currency():
    from_currency = request.args.get("from")
    to_currency = request.args.get("to")
    amount = request.args.get("amount")
    result = ExchangerateClient.convert_currency(
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
    )
    return {"result": result}


@blueprint.route('/latest_rates')
def latest_rates():
    base = request.args.get("base")
    symbols = request.args.get("symbols")
    result = ExchangerateClient.latest_rates(
        base=base,
        symbols=symbols,
    )
    return {"result": result}


@blueprint.route('/symbols')
def symbols():
    result = ExchangerateClient.symbols()
    return {"result": result}
