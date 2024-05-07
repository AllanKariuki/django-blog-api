from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ViewSet):

    def list(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        if serializer.data:
            return Response(
                {'detail': serializer.data, 'code': 200},
                status=status.HTTP_200_OK
            )

        return Response(
            {'detail': 'No blogs yet', 'code': 200},
            status=status.HTTP_200_OK
        )

    def create(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'Blog created successfully', 'code': 201},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'detail': serializer.errors, 'code': 400},
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response(
                {'detail': 'Blog not found', 'code': 404},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogSerializer(blog)
        return Response(
            {'detail': serializer.data, 'code': 200},
            status=status.HTTP_200_OK
        )

    def update(self, request, pk=None):
        try:
            blog= Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response(
                {'detail': 'Blog not found', 'code': 404},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'Blog updated successfully', 'code': 200},
                status=status.HTTP_200_OK
            )

    def destroy(self, request, pk=None):
        Blog.objects.get(id=pk).delete()
        return Response(
            {'detail': 'Blog deleted successfully', 'code': 200},
            status=status.HTTP_200_OK
        )