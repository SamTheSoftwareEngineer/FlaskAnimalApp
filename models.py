"""Contains the models for the application."""
from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"


class Pet(db.model):
    """Defines the Pet model."""
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, required=True)
    species = db.Column(db.String(80), nullable=False, required=True )
    photo_url = db.Column(db.String(200), required=False)
    age = db.Column(db.Integer, required=False)
    notes = db.Column(db.String(200), required=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    def image_url(self):
        """Returns the image url for the pet."""
        return self.photo_url or GENERIC_IMAGE
    
def connect_db(app):
    """Connects to the database."""
    db.app = app
    db.init_app(app)
    