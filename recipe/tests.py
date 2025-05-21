from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_category_creation_and_iter(self):
        cat = Category.objects.create(name="Салати")
        self.assertEqual(str(cat), "Салати")
        self.assertIn("Салати", list(iter(cat)))


class RecipeModelTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="Основні страви")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Борщ",
            description="Традиційна страва",
            instructions="Готувати 2 години",
            ingredients="буряк, капуста, картопля",
            category=self.cat
        )
        self.assertEqual(str(recipe), "Борщ")
        self.assertEqual(recipe.category.name, "Основні страви")

