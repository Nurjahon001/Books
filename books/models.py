import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# Create your models here.

class Books(models.Model):

    isbn = models.CharField(max_length=13, unique=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image_book=models.ImageField(default='books_image/default_book_image.png',upload_to='books_image')
    price=models.DecimalField(max_digits=7,decimal_places=2)
    publisher=models.CharField(max_length=50,blank=True,null=True)
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='books_table'

class Author(models.Model):
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table='book_author_table'
class BookAuthor(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.SET_DEFAULT,default='delated author')

    def __str__(self):
        return  f'{self.book.title}  {self.author.name}'

    def get_info(self):
        return  f'{self.book.title}  {self.author.name}'

    class Meta:
        db_table='author_table'

class BookReview(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE,related_name='book_review')
    comment=models.TextField()
    star_given=models.PositiveIntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table='review_table'

    def __str__(self):
        return self.book.title