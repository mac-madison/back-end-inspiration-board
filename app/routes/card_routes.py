from flask import Blueprint, request, jsonify, make_response, abort
from app import db
import app.routes.validate as validate
from app.models.card import Card


# ADD VALIDATE FUNCTIONALITIES 


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# delete
@cards_bp.route('/<card_id>', methods = ['DELETE'])
def delete_card(card_id):
    card = get_card_by_id(card_id)

    db.session.delete(card)
    db.session.commit()
    response_body ={"details": f'Card {card.card_id} "{card.title}" successfully deleted'}
    return make_response(response_body), 200

# UPDATE LIKE
@cards_bp.route('/<card_id>/likes', methods = ['PATCH'])
def update_like(card_id):
    # custom endpoint for updating like columns in cards

    pass 






# Helper functions

def get_card_by_id(card_id):
    valid_int(card_id, "card_id")
    return Card.query.get_or_404(card_id, description='{card not found}')

def valid_int(number, parameter_type):
    try:
        int(number)
    except:
        abort(make_response({"error": f'{parameter_type} must be an integer'}, 400))