from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializers, MovieSerializers, ReviewSerializers
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def Director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializers(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def Director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    serializers = DirectorSerializers(director)
    return Response(data=serializers.data)


@api_view(['GET'])
def Movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def Moview_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Movie': 'Movie not found'})
    serializer = MovieSerializers(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def Review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializers(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def Review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Review': 'Review not found'})
    serializer = ReviewSerializers(review)
    return Response(data=serializer.data)







