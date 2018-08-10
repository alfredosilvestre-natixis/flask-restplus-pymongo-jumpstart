"""
Dogs related operations
"""
import logging

from flask import request
from flask_restplus import Resource

from .model import DogDto

LOG = logging.getLogger(__name__)
api = DogDto.api  # pylint: disable=invalid-name


@api.route('/')
class DogList(Resource):
    """Operations over the dog list"""
    @classmethod
    @api.doc('list_dogs')
    @api.marshal_list_with(DogDto.dog_model)
    def get(cls):
        """List all dogs"""
        return DogDto.get_dogs()

    @classmethod
    @api.expect(DogDto.dog_model)
    @api.marshal_with(DogDto.dog_model)
    @api.response(201, 'Dog successfully created')
    def post(cls):
        """
        Creates a new dog
        """
        DogDto.create_dog(request.json)
        LOG.info('Created dog: %s', str(request.json))
        return request.json, 201


@api.route('/<int:dog_id>')
@api.param('dog_id', 'The dog identifier')
@api.response(404, 'Dog not found')
class Dog(Resource):
    """Operations over a dog item"""
    @classmethod
    @api.doc('get_dog')
    @api.marshal_with(DogDto.dog_model)
    def get(cls, dog_id):
        """Fetch a dog given its identifier"""
        dog_obj = DogDto.get_dog(dog_id)
        if dog_obj:
            return dog_obj
        LOG.info('Dog not found: %s', str(dog_id))
        return None, 404

    @classmethod
    @api.doc('update_dog')
    @api.expect(DogDto.dog_model)
    @api.marshal_with(DogDto.dog_model)
    @api.response(204, 'Dog successfully updated.')
    def put(cls, dog_id):
        """
        Updates a dog

        Use this method to change the name of a dog

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Dog Name"
        }
        ```

        * Specify the ID of the dog to modify in the request URL path
        """
        dog_obj = DogDto.get_dog(dog_id)
        if dog_obj:
            DogDto.update_dog(dog_id, request.json)
            LOG.info('Updated dog: %s', str(request.json))
            return None, 204
        LOG.info('Dog not found: %s', str(dog_id))
        return None, 404

    @classmethod
    @api.doc('delete_dog')
    @api.marshal_with(DogDto.dog_model)
    @api.response(204, 'Dog successfully deleted.')
    def delete(cls, dog_id):
        """
        Deletes a dog
        """
        dog_obj = DogDto.get_dog(dog_id)
        if dog_obj:
            DogDto.delete_dog(dog_id)
            LOG.info('Deleted dog: %d', str(dog_obj))
            return None, 204
        LOG.info('Dog not found: %s', str(dog_id))
        return None, 404
