from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default=0)
    address = models.TextField(blank=True)
    user_image = models.URLField(blank=True, null=True)

    # social links
    linkedIn = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    # word address
    address = models.CharField(max_length=400)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Categories(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return str(self.name)




class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=300, blank=True, null=True)
    Book_image = models.URLField()
    book_name  = models.CharField(max_length=400)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    strike_price = models.IntegerField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    overview = models.TextField(blank=True, null=True)
    # book_file = models.URLField()
    category_name = models.CharField(max_length=300, blank=True, null=True)
    categories =  models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str :
        return f'{self.book_name}'



class Chapter(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book_ref = models.ForeignKey(Book, on_delete=models.CASCADE)
    booK_name = models.CharField(max_length=300)
    chapter_name = models.CharField(max_length=200)
    Chapter_title = models.CharField(max_length=200, null=True)
    book_text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.book_name}'


class checkout(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    total_amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self) -> str :
        return str(self.owner)


class UserBooks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return str(self.owner)

class Wishlist(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return f'{self.owner}'



class Referal(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="users")





class Withdrawer(models.Model):
    owner = models.CharField(max_length=300)
    amount =  models.CharField(max_length=300)
    user_address = models.TextField()


    def __str__(self) -> str:
        return str(self.owner)






