from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from carx_drf.models import Customer
from carx_drf.serializers import CustomerSerializer, TyreSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from models import Customer, Tyre
from rest_framework import authentication
from rest_framework import exceptions


# def login(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Customer.objects.all()
#         serializer = CustomerSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CustomerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @receiver(post_save, sender=Customer)
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     print "hello"
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
#
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TyreViewSet(viewsets.ModelViewSet):
    queryset = Tyre.objects.all()
    serializer_class = TyreSerializer


class LoginView(APIView):
    def get(self, request):
        return Response({"message": "please request as a post"})

    def post(self, request):

        data = JSONParser().parse(request)
        try:
            queryset = Customer.objects.get(email=data.get('email'), password=data.get('password'))

        except:
            return Response({"error": 'Invalid Credentials'}, status=403)

        if queryset:
            serializer = CustomerSerializer(queryset, many=False)
            return JsonResponse(serializer.data, status=200)

        else:
            return Response({"errors": 'Invalid Credentials'})

# @csrf_exempt
# def customer_login(request):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         print data
#         serializer = CustomerSerializer(data)
#         return JsonResponse(serializer.data)
#
#     else:
#         return HttpResponse(status=404)

