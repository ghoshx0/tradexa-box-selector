from rest_framework import serializers


class RecommendationItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class RecommendationSerializer(serializers.Serializer):
    items = RecommendationItemSerializer(many=True)