from flask import request
from app import app, db
from app.database import Message


# db.session.add(
#         Message(
#             title=title,
#             body=body
#         )
#     )
#     db.session.commit()


@app.route("/messages", methods=["POST"])
def create_message():
    message_data = request.json
    title = message_data.get("title") #Because we're using get, if the key isn't found .......
    body = message_data.get("body")   #...... we'll get a NoneType as a result.
    if not title or not body:
        return "<h1>Invalid syntax</h1>", 400
    message = Message(title=title, body=body)
    db.session.add(message)
    db.session.commit()
    return "<h1>Created</h1>", 201

@app.get("/messages")
def get_all_messages():
    return Message.query.all()

@app.get("/messages/<int:pk>")
def get_message_by_id(pk):
    return Message.query.filter_by(id=pk).first()
