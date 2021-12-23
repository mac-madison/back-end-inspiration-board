from flask import Blueprint, request, jsonify, make_response
from app import db

# example_bp = Blueprint('example_bp', __name__)
kinder_code_bp = Blueprint("kinder_code", __name__)
