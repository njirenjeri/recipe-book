from flask_restx import Namespace, Resource, fields
from models import Recipe
from flask import request
from flask_jwt_extended import  jwt_required



recipe_ns = Namespace('recipes', description="a namespace for recipes")


# model / serializer
recipe_model=recipe_ns.model(
    "Recipe",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "description": fields.String()
    }
)


# === Recipe Routes === 
@recipe_ns.route('/recipes')
class RecipeResource(Resource):
    @recipe_ns.marshal_list_with(recipe_model)
    def get(self):
        """Get all Recipes"""
        recipes = Recipe.query.all()
        return recipes
        

    @recipe_ns.marshal_with(recipe_model)
    @recipe_ns.expect(recipe_model) #decorator for swagger UI
    @jwt_required()
    def post(self):
        """Create a new recipe"""

        # access data from json
        data = request.get_json()

        new_recipe = Recipe(
            title=data.get('title'),
            description=data.get('description')
        )

        new_recipe.save()
        return new_recipe, 201
        

@recipe_ns.route('/recipe/<int:id>')
class RecipebyIdResource(Resource):
    @recipe_ns.marshal_with(recipe_model)
    def get(self, id):
        """Get a recipe by Id"""
        # searches for the recipe by id and returns a 404 err if not found
        recipe=Recipe.query.get_or_404(id)

        return recipe
    
    @recipe_ns.marshal_with(recipe_model)
    @jwt_required()
    def put(self, id):
        """Update recipe by Id"""
        recipe_to_update=Recipe.query.get_or_404(id)

        data=request.get_json()

        recipe_to_update.update(data.get('title'), data.get('description'))

        return recipe_to_update
        
    @recipe_ns.marshal_with(recipe_model)
    @jwt_required()
    def delete(self, id):
        """delete a recipe by Id"""

        recipe_to_delete=Recipe.query.get_or_404(id)

        recipe_to_delete.delete()

        return recipe_to_delete
