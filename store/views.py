from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import (ChapterSerializer, ProfileSerializer, UserBookSerializer, UserSerializer, ReferalSerializer,
                          BookSerializer, CategoriesSerializer, wishListSerializer, CheckOutSerializer, WithdrawerSerializer)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView)
from .models import Book, Categories, Referal, User, Wishlist, checkout, Chapter, UserBooks, Withdrawer
from rest_framework.permissions import IsAuthenticated
import json



# Create your views here.

@api_view(['GET'])
def getRouter(request) -> Response:
    routes = [
        '/register',
        '/login/token',
        'login/token/refresh/',
        'book',
        'books/id/'
    ]
    return Response(routes)


@api_view(["GET"])
def withdrawer(request, username, amount, address):
    withdrawer = Withdrawer.objects.get_or_create(owner=username, amount=amount, user_address=address)
    serializer = WithdrawerSerializer(withdrawer, many=False)
    return Response(serializer.data)



@api_view(['PATCH'])
def amount(request, pk, num):
    user = User.objects.get(id=pk)
    print(user.amount)
    user.amount += num
    user.save()
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getchapter(request, pk):
    chapter = Chapter.objects.filter(book_ref=pk)
    serializer = ChapterSerializer(chapter, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserProfile(request, email):
    profile = User.objects.get(email=email)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getoverview(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    except:
        return Response("No data")


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self) -> User:
        print(self.request.user)
        return User.objects.filter(email=self.request.user)


class ProfileAmountView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = "id"

    def get_queryset(self) -> User:
        return User.objects.filter(id=int(self.lookup_field))


class BookListCreateView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self) -> Book:
        return Book.objects.filter(author=self.request.user)

class AllBooksView(ListAPIView):
    serializer_class = BookSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    # permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self) -> Book:
        return Book.objects.filter(author=self.request.user)


class BookUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self) -> Book:
        return Book.objects.filter(author=self.request.user)


class CategoriesListView(ListAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> Categories:
        return Categories.objects.all()


class CheckoutListView(ListCreateAPIView):
    serializer_class = CheckOutSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self) -> checkout:
        return checkout.objects.filter(owner=self.request.user)



class WishListView(ListCreateAPIView):
    serializer_class = wishListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self) -> Wishlist:
        return Wishlist.objects.filter(owner=self.request.user)


class WishListUpdateView(RetrieveUpdateAPIView):
    serializer_class = wishListSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "email"

    def get_queryset(self) -> Wishlist:
        return Wishlist.objects.filter(owner=self.request.user)



class ReferalListCreateView(ListCreateAPIView):
    serializer_class = ReferalSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self) -> Referal:
        return Referal.objects.filter(owner=self.request.user)


class ReferalListUpdateView(RetrieveUpdateAPIView):
    serializer_class = ReferalSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "email"

    def get_queryset(self) -> Referal:
        return Referal.objects.filter(owner=self.request.user)


class ChapterView(ListCreateAPIView):
    serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self) -> Chapter:
        return Chapter.objects.filter(owner=self.request.user,)



class UserBooksView(ListCreateAPIView):
    serializer_class = UserBookSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        return UserBooks.objects.filter(owner=self.request.user)



class UserBookUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserBookSerializer
    # permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self) -> UserBooks:
        return UserBooks.objects.filter(owner=self.request.user)


class ChapterUpdateView(RetrieveUpdateDestroyAPIView):
    # serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticated,)

    lookup_field = "id"


    def get_queryset(self) -> Chapter:
        return Chapter.objects.filter(owner=self.request.user)