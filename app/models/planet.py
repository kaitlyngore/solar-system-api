from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.String)

    def create_dict(self):
        return {
                        "id": self.id,
                        "name": self.name,
                        "description": self.description,
                        "type": self.type,
                    }