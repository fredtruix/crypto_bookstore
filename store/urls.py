from django.urls import path
from .views import (ChapterView, CheckoutListView, RegisterView, WishListUpdateView, getRouter, WishListView, AllBooksView, BookUpdateView, UserBooksView, UserBookUpdateView,getoverview, getUserProfile,
                    BookListCreateView, ReferalListCreateView, ReferalListUpdateView, BookDetailView, CategoriesListView, ProfileDetailView, ChapterUpdateView, ProfileAmountView, amount, getchapter, withdrawer)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="StarlyBooks API",
        default_version='v1',
        description="Get all data on  StarlyBooks",
        terms_of_service="https://link.medium.com/sQFZhouMgmb",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="StarlyBooks License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("getrouter/", getRouter, name="router"),
    path('userbooks/<int:id>/', UserBookUpdateView.as_view(), name="update_user_books"),# to update user books
    path('register/', RegisterView.as_view(), name="register"), # register a user to the database
    path('user/<int:id>', ProfileDetailView.as_view(), name="user"), #profiledetails
    path('book/', BookListCreateView.as_view(), name="book"), #create book
    path('amount/<int:pk>/<int:num>/', amount, name="amount"),
    path('getprofile/<str:email>/', getUserProfile, name="getprofile"),
    path('chapter/<int:pk>/', getchapter, name="chapter_book"),
    path('overview/<int:pk>/', getoverview, name="getoverview"),
    path('books/<int:id>/', BookDetailView.as_view(), name="books"), #update, get,  delete
    path('book/update/<int:id>/', BookUpdateView.as_view(), name="book_update"), #update, get,  delete
    path('chapter/', ChapterView.as_view(), name="chapter"), #chapter create or Post
    path('chapter/<int:id>/', ChapterUpdateView.as_view(), name="chapter_update"), # to update a chapter in a book
    path('checkout/', CheckoutListView.as_view(), name="checkout"), # create checkout
    path('userbooks/', UserBooksView.as_view(), name="userbooks"), # to create or Post book
    path('categories/', CategoriesListView.as_view(), name="categories"), # get books categories
    path('wishlist/', WishListView.as_view(), name="wishlist"), # add items  to wishlist
    path('wishlist/<str:email>/',
         WishListUpdateView.as_view(), name="wishlist-update"), # update item or delete item
    path('allbooks/', AllBooksView.as_view(), name="allbook"),
    path('profileAmount/<int:id>/', ProfileAmountView.as_view(), name="profileAmount"),
    path('referal/', ReferalListCreateView.as_view(), name="referal"), # add to referal
    path('referal/<str:email>/', ReferalListUpdateView.as_view(), name="referal_add"), # add to referal
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # login to get token and refresh  token
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # get  acces token with refresh
    path('withdrawer/<str:username>/<str:amount>/<str:address>/',withdrawer, name="withdrawer")







]
