from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Information_Book_Detail(models.Model):

    Book_Id = models.IntegerField(primary_key=True, null=False)
    Book_Title = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50) 
    Author_Url = models.CharField(max_length=50, null=True)
    Description = models.CharField(max_length=1000, null=True) 
    Rating_Avg = models.FloatField(null=True) 
    Rating_Count = models.IntegerField(null=True)
    Reviews_Count = models.IntegerField(null=True)
    Num_Pages = models.IntegerField(null=True) 
    Book_Format  = models.CharField(max_length=50, null=True)
    Time_publish = models.CharField(max_length=50, null=True) 
    Publisher = models.CharField(max_length=50, null=True) 
    ISBN = models.CharField(max_length=50, null=True) 
    Language = models.CharField(max_length=50, null=True) 
    Genres = models.JSONField(null=True) 
    Book_Url = models.CharField(max_length=100)
 
    class Meta:
        db_table = "Book_Details"
        verbose_name = 'Book Detail'
        verbose_name_plural = 'Book Details'
        ordering = ['Author_Name', 'Book_Title']
 
    def __str__(self):
        return self.Book_Title


class Information_User_Detail(models.Model):
    User_Id = models.IntegerField(primary_key=True, null=False)
    Username = models.CharField(max_length=50)
    User_Url = models.CharField(max_length=100)

    def __str__(self):
        return self.Username


class User_Rating_Information(models.Model):

    Book_Info = models.ForeignKey(Information_Book_Detail, on_delete=models.PROTECT)
    User_Info = models.ForeignKey(Information_Book_Detail, on_delete=models.PROTECT)
    book_url = models.CharField(max_length=100)
    user_rating = models.FloatField()
 
    class Meta:
        db_table = "User_Rating"
        verbose_name = 'User Rating'
        verbose_name_plural = 'User_Ratings'

    def __str__(self):
        return "{} - {}".format(self.User_Info, self.Book_Info)