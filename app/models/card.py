from app import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(255), nullable=False)
    likes_count = db.Column(db.Integer, nullable=True)
    board = db.relationship("Board", back_populates="cards", lazy=True)
    board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
<<<<<<< HEAD
    required_fields = ["message","likes_count","board_id"]
=======
>>>>>>> d7390ee2c70f62448fd51cb5daad4f9a8c537e0a

    def to_dict(self):
        return {
            "card_id": self.id,
            "message": self.message,
<<<<<<< HEAD
            "likes_count": self.likes_count,
            "board_id": self.board_id,
=======
            "likes_count": self.like_count,
            "board_id": self.board.id,
>>>>>>> d7390ee2c70f62448fd51cb5daad4f9a8c537e0a
        }
