"""
Dog model
"""
from flask_restplus import Namespace, fields

import app


class DogDto:
    """Dog DTO"""
    api = Namespace('dogs', description='Dogs related operations')
    dog_model = api.model('dog', {
        'id': fields.Integer(readOnly=True, description='The dog identifier'),
        'name': fields.String(required=True, description='The dog name'),
    })

    @classmethod
    def get_dogs(cls):
        """List all dogs"""
        return list(app.App.mongodb.db.dogs.find({}))

    @classmethod
    def create_dog(cls, data):
        """Create a dog"""
        app.App.mongodb.db.dogs.insert_one(data)

    @classmethod
    def get_dog(cls, dog_id):
        """Get a dog"""
        return app.App.mongodb.db.dogs.find_one({'id': dog_id})

    @classmethod
    def update_dog(cls, dog_id, data):
        """Update a dog"""
        app.App.mongodb.db.dogs.update_one({'id': dog_id}, {'$set': {'name': data['name']}})

    @classmethod
    def delete_dog(cls, dog_id):
        """Delete a dog"""
        app.App.mongodb.db.dogs.delete_one({'id': dog_id})
