"""
Cat model
"""
from flask_restplus import Namespace, fields

import app


class CatDto:
    """Cat DTO"""
    api = Namespace('cats', description='Cats related operations')
    cat_model = api.model('cat', {
        'id': fields.Integer(readOnly=True, description='The cat identifier'),
        'name': fields.String(required=True, description='The cat name'),
    })

    @classmethod
    def get_cats(cls):
        """List all cats"""
        return list(app.App.mongodb.db.cats.find({}))

    @classmethod
    def create_cat(cls, data):
        """Create a cat"""
        app.App.mongodb.db.cats.insert_one(data)

    @classmethod
    def get_cat(cls, cat_id):
        """Get a cat"""
        return app.App.mongodb.db.cats.find_one({'id': cat_id})

    @classmethod
    def update_cat(cls, cat_id, data):
        """Update a cat"""
        app.App.mongodb.db.cats.update_one({'id': cat_id}, {'$set': {'name': data['name']}})

    @classmethod
    def delete_cat(cls, cat_id):
        """Delete a cat"""
        app.App.mongodb.db.cats.delete_one({'id': cat_id})
