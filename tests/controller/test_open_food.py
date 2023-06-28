import unittest
from unittest.mock import patch

from starlette.testclient import TestClient

from main import app
from resources.data import data

client = TestClient(app)


class TestOpenFood(unittest.TestCase):
    def test_get_foods_should_return_foods(self):
        with patch("controller.open_food.MongoPipeline.get_foods") as mock_get_foods:
            mock_get_foods.return_value = data

            response = client.get("/food")

            assert response.status_code == 200

    def test_get_foods_should_return_404_if_no_foods_available(self):
        with patch("controller.open_food.MongoPipeline.get_foods") as mock_get_foods:
            mock_get_foods.return_value = []

            response = client.get("/food")

            assert response.status_code == 404

    def test_get_food_by_barcode_should_return_name(self):
        with patch("controller.open_food.MongoPipeline.get_food") as mock_get_foods:
            mock_get_foods.return_value = data

            response = client.get("/food/2345")

            assert response.status_code == 200

    def test_get_food_by_barcode_should_return_404_if_not_found(self):
        with patch("controller.open_food.MongoPipeline.get_food") as mock_get_foods:
            mock_get_foods.return_value = []

            response = client.get("/food/222")

            assert response.status_code == 404





