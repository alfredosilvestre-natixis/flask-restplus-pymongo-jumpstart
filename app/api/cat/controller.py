"""
Cats related operations
"""
import logging

from flask import request
from flask_restplus import Resource

from .model import CatDto

LOG = logging.getLogger(__name__)
api = CatDto.api  # pylint: disable=invalid-name


@api.route('/')
class CatList(Resource):
    """Operations over the cat list"""
    @classmethod
    @api.doc('list_cats')
    @api.marshal_list_with(CatDto.cat_model)
    def get(cls):
        """List all cats"""
        return CatDto.get_cats()

    @classmethod
    @api.expect(CatDto.cat_model)
    @api.marshal_with(CatDto.cat_model)
    @api.response(201, 'Cat successfully created')
    def post(cls):
        """
        Creates a new cat
        """
        CatDto.create_cat(request.json)
        LOG.info('Created cat: %s', str(request.json))
        return request.json, 201


@api.route('/<int:cat_id>')
@api.param('cat_id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    """Operations over a cat item"""
    @classmethod
    @api.doc('get_cat')
    @api.marshal_with(CatDto.cat_model)
    def get(cls, cat_id):
        """Fetch a cat given its identifier"""
        cat_obj = CatDto.get_cat(cat_id)
        if cat_obj:
            return cat_obj
        LOG.info('Cat not found: %s', str(cat_id))
        return None, 404

    @classmethod
    @api.doc('update_cat')
    @api.expect(CatDto.cat_model)
    @api.marshal_with(CatDto.cat_model)
    @api.response(204, 'Cat successfully updated.')
    def put(cls, cat_id):
        """
        Updates a cat

        Use this method to change the name of a cat

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Cat Name"
        }
        ```

        * Specify the ID of the cat to modify in the request URL path
        """
        cat_obj = CatDto.get_cat(cat_id)
        if cat_obj:
            CatDto.update_cat(cat_id, request.json)
            LOG.info('Updated cat: %s', str(request.json))
            return None, 204
        LOG.info('Cat not found: %s', str(cat_id))
        return None, 404

    @classmethod
    @api.doc('delete_cat')
    @api.marshal_with(CatDto.cat_model)
    @api.response(204, 'Cat successfully deleted.')
    def delete(cls, cat_id):
        """
        Deletes a cat
        """
        cat_obj = CatDto.get_cat(cat_id)
        if cat_obj:
            CatDto.delete_cat(cat_id)
            LOG.info('Deleted cat: %s', str(cat_obj))
            return None, 204
        LOG.info('Cat not found: %s', str(cat_id))
        return None, 404
