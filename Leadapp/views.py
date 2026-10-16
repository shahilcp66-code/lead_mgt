from django.shortcuts import render
from Leadapp.serializers import LeadSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from Leadapp.models import Lead 
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filtering_fields=["status","source"]
    search_fields=['name','email','status','source']
    ordering_fields=['name','added_date']

class LeadDetail(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=LeadSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Lead.objects.all()



    








