from django.test import TestCase
from rest_framework.test import APIClient

from products.models import Product
from boxes.models import Box

class RecommendBoxTests(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.laptop = Product.objects.create(
            name="Laptop",
            length=35,
            width=25,
            height=5,
            weight=2
        )

        self.keyboard = Product.objects.create(
            name="Keyboard",
            length=45,
            width=15,
            height=5,
            weight=1
        )

        Box.objects.create(
            name="Small Box",
            internal_length=40,
            internal_width=30,
            internal_height=10,
            max_weight=5,
            cost=50
        )

        Box.objects.create(
            name="Medium Box",
            internal_length=50,
            internal_width=40,
            internal_height=20,
            max_weight=10,
            cost=80
        )

        Box.objects.create(
            name="Large Box",
            internal_length=70,
            internal_width=50,
            internal_height=30,
            max_weight=20,
            cost=120
        )
    def test_recommend_box_success(self):

        response = self.client.post(
            "/api/recommend-box/",
            {
                "items": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 1
                    },
                    {
                        "product_id": self.keyboard.id,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.data["recommended_box"],
            "Medium Box"
        )
    def test_invalid_product(self):

        response = self.client.post(
            "/api/recommend-box/",
            {
                "items": [
                    {
                        "product_id": 999,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            404
        )
    def test_no_box_found(self):

        heavy_product = Product.objects.create(
            name="Server Rack",
            length=100,
            width=100,
            height=100,
            weight=100
        )

        response = self.client.post(
            "/api/recommend-box/",
            {
                "items": [
                    {
                        "product_id": heavy_product.id,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            404
        )
    def test_cheapest_box_selected(self):

        Box.objects.create(
            name="Premium Box",
            internal_length=50,
            internal_width=40,
            internal_height=20,
            max_weight=10,
            cost=150
        )

        response = self.client.post(
            "/api/recommend-box/",
            {
                "items": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 1
                    },
                    {
                        "product_id": self.keyboard.id,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(
            response.data["recommended_box"],
            "Medium Box"
        )
    def test_unused_volume_tiebreaker(self):

        Box.objects.create(
            name="Compact Box",
            internal_length=48,
            internal_width=30,
            internal_height=15,
            max_weight=10,
            cost=80
        )

        response = self.client.post(
            "/api/recommend-box/",
            {
                "items": [
                    {
                        "product_id": self.laptop.id,
                        "quantity": 1
                    },
                    {
                        "product_id": self.keyboard.id,
                        "quantity": 1
                    }
                ]
            },
            format="json"
        )

        self.assertEqual(
            response.data["recommended_box"],
            "Compact Box"
        )