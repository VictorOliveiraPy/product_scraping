import unittest
from unittest.mock import patch

from starlette.testclient import TestClient

from main import app

data = {
    "name": "Spring water",
    "url": "https://world.openfoodfacts.org/product/3274080005003/eau-de-source-cristaline",
    "barcode": "3274080005003",
    "quantity": "1,5 L",
    "brands": [
        {
            "href": "/brand/cristaline",
            "name": "Cristaline"
        }
    ],
    "packaging": [
        {
            "href": "/packaging/lid-or-cap",
            "name": "Lid or cap"
        },
        {
            "href": "/packaging/plastic",
            "name": "Plastic"
        },
        {
            "href": "/packaging/bottle-cap",
            "name": "Bottle cap"
        },
        {
            "href": "/packaging/bottle-or-vial",
            "name": "Bottle or vial"
        },
        {
            "href": "/packaging/bottle",
            "name": "Bottle"
        }
    ],
    "categories": [
        {
            "href": "/category/beverages",
            "name": "Beverages"
        },
        {
            "href": "/category/waters",
            "name": "Waters"
        },
        {
            "href": "/category/spring-waters",
            "name": "Spring waters"
        },
        {
            "href": "/category/mineral-waters",
            "name": "Mineral waters"
        },
        {
            "href": "/category/natural-mineral-waters",
            "name": "Natural mineral waters"
        },
        {
            "href": "/category/unsweetened-beverages",
            "name": "Unsweetened beverages"
        }
    ],
    "imported_t": "2023-06-28T13:25:14.348004",
    "status": "imported"
}
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





