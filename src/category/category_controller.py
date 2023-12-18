from flask import request
from marshmallow import ValidationError

from src import app
from src.category.category_schema import CategorySchema, PrivateCategorySchema
from src.category.category_service import CategoryService

categoryService = CategoryService()


@app.route('/category', methods=['POST'])
def addCategory():
    try:
        CategorySchema().load(data=request.get_json())
        return categoryService.addCategory(request.get_json())
    except ValidationError as e:
        return {'message': e.messages}


@app.route('/category/private', methods=['POST'])
def addPrivateCategory():
    try:
        PrivateCategorySchema().load(data=request.get_json())
        return categoryService.addPrivateCategory(request.get_json())
    except ValidationError as e:
        return {'message': e.messages}


@app.route('/category', methods=['GET'])
def getCategories():
    return categoryService.getAllCategories(request.args.get('userId'))


@app.route('/category/<int:id>', methods=['DELETE'])
def deleteCategory(id):
    return categoryService.deleteCategory(id)
