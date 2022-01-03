from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
import app.validate as validate

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")


@boards_bp.route("", methods=["POST"])
def create_board():

    request_body = request.get_json(force=True)

    try:
        new_board = Board(
            title=request_body["title"],
            owner=request_body["owner"],
        )
        db.session.add(new_board)
        db.session.commit()

        return new_board.to_dict(), 201

    except KeyError:

        return make_response(validate.missing_fields(request_body, Board), 400)


@boards_bp.route("", methods=["GET"])
def get_boards():

    boards = Board.query.all()
    return jsonify([board.to_dict() for board in boards])


@boards_bp.route("/<id>/cards", methods=["GET"])
def get_board(id):

    board_id = validate.valid_id(id)
    board = validate.valid_model(board_id, Board)

    return board.to_dict()