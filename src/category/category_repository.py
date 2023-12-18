from src import db
from src.category.category_model import CategoryModel


class CategoryRepository:
    _categories = []

    def addCategory(self, name, idPrivateUser):
        if idPrivateUser is None:
            idPrivateUser = 0
            
        category = CategoryModel(name=name, idPrivateUser=idPrivateUser)
        db.session.add(category)
        db.session.commit()

        return category.toDict()

    def removeCategoryById(self, id):
        categoryToDelete = CategoryModel.query.get(id)
        if categoryToDelete is not None:
            db.session.delete(categoryToDelete)
            db.session.commit()

        return True

    def getAllPublicCategories(self):
        return CategoryModel.toDictList(CategoryModel.query.all(CategoryModel.idPrivateUser == 0))

    def getAllPrivateCategories(self, id):
        return CategoryModel.toDictList(CategoryModel.query.filter(CategoryModel.idPrivateUser == id))

    def getCategoryById(self, id):
        category = CategoryModel.query.get(id)
        if category is not None:
            return category.toDict()
        else:
            return None


categoryRepository = CategoryRepository()
