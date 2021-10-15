from app import db

# When using an ORM, classes that represent database tables
# are called MODELS.
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Message [ID: %r] [title: %r] [body: %r]>" % (self.id, self.title, self.body)