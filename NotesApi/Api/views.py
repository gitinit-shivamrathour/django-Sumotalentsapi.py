from django.shortcuts import render
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# List and Create Notes
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def NotesAPILP(request):
    if request.method == 'GET':
        user = request.user
        notes = Notes.objects.filter(user=user)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        user = request.user
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'Message': 'Created'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_502_BAD_GATEWAY)


# Retrieve update and delete Notes
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def NotesAPIRUD(request, pk=None):
    if request.method == 'GET':
        id = pk
        notes = Notes.objects.get(id=id)
        serializer = NotesSerializer(notes)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        id = pk
        notes = Notes.objects.get(id=id)
        serializer = NotesSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_502_BAD_GATEWAY)

    if request.method == 'PATCH':
        id = pk
        notes = Notes.objects.get(id=id)
        serializer = NotesSerializer(notes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Updated Partially'}, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_502_BAD_GATEWAY)

    if request.method == 'DELETE':
        id = pk
        notes = Notes.objects.get(id=id)
        notes.delete()
        return Response({'Message': 'Deleted'}, status=status.HTTP_200_OK)
