from rest_framework import serializers


class TraitsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(max_length=20, source="name")
    created_at = serializers.DateTimeField(read_only=True)