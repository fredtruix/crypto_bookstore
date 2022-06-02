from django.contrib import admin
from .models import(User, Book, Categories, checkout, Wishlist, Referal,UserBooks, Withdrawer)
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Categories)
admin.site.register(checkout)
admin.site.register(Wishlist)
admin.site.register(Referal)
admin.site.register(UserBooks)
admin.site.register(Withdrawer)
