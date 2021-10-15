from app import db
from app.database import Message
from pprint import pprint


def create_message(title, body):
    db.session.add(
        Message(
            title=title,
            body=body
        )
    )
    db.session.commit()

if __name__ == "__main__":
    print("Create a new message:")
    title = input("Title: ")
    body = input("Body: ")
    create_message(title,body)
    print("Your messages:")
    messages = Message.query.all()
    pprint(messages)
    print("Your first message: ")
    message = Message.query.filter_by(id=1).first()
    print(message)