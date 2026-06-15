from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from boxes.models import Box

from .serializers import RecommendationSerializer

class RecommendBoxView(APIView):

    def post(self, request):

        serializer = RecommendationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        items = serializer.validated_data["items"]

        required_length = 0
        required_width = 0
        required_height = 0
        total_weight = 0

        for item in items:
            
            try:
                product = Product.objects.get(
                    id=item["product_id"]
                )

            except Product.DoesNotExist:
                return Response(
                    {
                        "error":
                        f"Product with id {item['product_id']} does not exist"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )


            quantity = item["quantity"]

            required_length = max(
                required_length,
                product.length
            )

            required_width = max(
                required_width,
                product.width
            )

            required_height += (
                product.height * quantity
            )

            total_weight += (
                product.weight * quantity
            )

        required_volume = (
            required_length *
            required_width *
            required_height
        )

        valid_boxes = []

        boxes = Box.objects.all()

        for box in boxes:

            dimension_fit = (
                box.internal_length >= required_length
                and
                box.internal_width >= required_width
                and
                box.internal_height >= required_height
            )

            weight_fit = (
                box.max_weight >= total_weight
            )

            if dimension_fit and weight_fit:

                box_volume = (
                    box.internal_length *
                    box.internal_width *
                    box.internal_height
                )

                unused_volume = (
                    box_volume -
                    required_volume
                )

                valid_boxes.append(
                    {
                        "box": box,
                        "unused_volume": unused_volume
                    }
                )
        if not valid_boxes:

            return Response(
                {
                    "message":
                    "No suitable box found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        valid_boxes.sort(
            key=lambda x: (
                x["box"].cost,
                x["unused_volume"]
            )
        )
        best_box = valid_boxes[0]
        return Response(
            {
                "recommended_box":
                    best_box["box"].name,

                "cost":
                    best_box["box"].cost,

                "unused_volume":
                    best_box["unused_volume"],

                "total_weight":
                    total_weight
            }
        )