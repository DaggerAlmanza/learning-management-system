from django.db import models
from rest_framework import (
    serializers,
)


class Queries:
    def __init__(self):
        self.conn = models
        self.seria = serializers

    def find_many(self) -> list:
        data = self.conn.objects.all()
        response = self.seria(data, many=True)
        return [
            one_by_one for one_by_one in response.data
        ]

    def find_one(self, id: int, object: bool = False):
        data = self.conn.objects.filter(id=id).first()
        if not object:
            response = self.seria(data)
            return response.data
        return data

    def save_data(self, **kwargs):
        response = self.seria(data=kwargs)
        if response.is_valid():
            response.save()
            return response.data
        return response.errors

    def update_data(self, params: dict, id: int) -> dict:
        data = self.conn.objects.filter(id=id).first()
        response = self.seria(data, params)
        if response.is_valid():
            response.save()
            return response.data
        return response.errors

    def delete_one(self, id: int) -> bool:
        data = self.find_one(id, True)
        if not data:
            return False
        data.delete()
        return True
