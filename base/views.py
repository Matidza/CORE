from django.shortcuts import render
from django.http import JsonResponse 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import School

# Serialize the Model
from .serializers import SchoolSerializer

# Search
from django.db.models import Q

# Class based views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import School
from .serializers import SchoolSerializer
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/schools', '/school/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def schools(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        schools = School.objects.filter(username__icontains=query)
        serializer = SchoolSerializer(schools, many=True, context={'request': request})  # Pass request context
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Class-based views
'''  class SchoolDetail(APIView):
    def get_object(self, username):
        try:
            return School.objects.get(schoolname=username)  
        except School.DoesNotExist:
            raise JsonResponse('School doesnt exists')
        
    def get(self, request, username):
        schools = School.objects.get(schoolname=username)
        serializer = SchoolSerializer(schools, many=False)
        return Response(serializer.data)
    
    def put(self, request, username):
        schools = self.get_object(username)

        # fill form/dict to update
        schools.schoolname=request.data['schoolname'],
        schools.telephone=request.data['telephone'],
        schools.schoolemail=request.data['schoolemail'],
        schools.schooladdress=request.data['schoolname'],
        schools.postal_address=request.data['postal_address'],
        schools.website=request.data['website'],
        schools.slogan=request.data['slogan'],
        schools.emblem=request.data['emblem'],
        schools.type_of_school=request.data['type_of_school'],
        #schools.province=request.data['province']

        # Save
        schools.save()
        serializer = SchoolSerializer(schools, many=False)
        return Response(serializer.data)
    
    # Delete school
    def delete(self, request, username):
        schools = School.objects.get(schoolname=username)
        schools.delete()
        return Response("School was deleted")
'''

# Function-Based Views
@api_view(['GET', 'PUT', 'DELETE'])
def school(request, username):
    # Retrieve the school instance or return a 404 error if not found
    school = get_object_or_404(School, username=username)

    # Handle GET request
    if request.method == 'GET':
        serializer = SchoolSerializer(school, many=False, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle PUT request
    if request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request
    if request.method == 'DELETE':
        school.delete()
        return Response({"message": "School was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
