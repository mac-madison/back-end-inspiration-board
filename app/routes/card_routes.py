from flask import Blueprint, request, jsonify, make_response, abort
from app import db
import app.routes.validate as validate
from app.models.card import Card


# ADD VALIDATE FUNCTIONALITIES 


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# delete
@cards_bp.route('/<id>', methods = ['DELETE'])
def delete_card(id):
    card_id= validate.valid_id(id)
    card = validate.valid_model(card_id, Card)

    db.session.delete(card)
    db.session.commit()
    response_body ={"details": f'Card {card.id} {card.message} successfully deleted'}
    return make_response(response_body), 200


@cards_bp.route("/<id>", methods=["GET"])
def get_a_card(id):

    card_id = validate.valid_id(id)
    card = validate.valid_model(card_id, Card)

    return card.to_dict()

@cards_bp.route("", methods=["GET"])
def get_all_cards():

    cards = Card.query.all()
    return jsonify([card.to_dict() for card in cards])


