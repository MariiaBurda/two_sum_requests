from rest_framework import serializers

from .models import TwoSumRequest


class TwoSumRequestSerializer(serializers.Serializer):
    nums = serializers.JSONField()
    target = serializers.IntegerField()

    def create(self, validated_data):
        return TwoSumRequest.objects.create(**validated_data)
