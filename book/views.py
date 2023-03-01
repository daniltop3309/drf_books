from rest_framework.decorators import api_view
from rest_framework.response import Response
from book.models import Book
from book.serializers import BookSerializer
from rest_framework import status


@api_view(['GET'])
def api_overview(request):
    api_roots = {
        'List view': 'api/v1/get_books/',
        'Detail view': 'api/v1/get_book/<int:pk>/',
        'Update view': 'api/v1/update_book/<int:pk>/',
        'Create view': 'api/v1/create_book/',
        'Delete view': 'api/v1/delete_book/<int:pk>/',
    }
    return Response(api_roots)


@api_view(['GET'])
def get_books(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    queryset = Book.objects.get(id=pk)
    serializer = BookSerializer(queryset)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def update_book(request, pk):
    queryset = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, pk):
    queryset = Book.objects.get(id=pk)
    queryset.delete()

    return Response(status=status.HTTP_200_OK)
