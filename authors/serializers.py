from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    # bio = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'bio', 'active')
        # read_only_fields = ('id')

    # def get_bio(self):
    #     return "hello, it looks good"
