from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView


class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code': '200'}, status=status.HTTP_200_OK)