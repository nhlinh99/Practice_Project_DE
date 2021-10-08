from django.db import models

# Create your models here.
class Information_Book_Detail(models.Model):

    Book_Title = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50) 
    Author_Url = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000) 
    Rating = models.FloatField() 
    Rating_Counts = models.IntegerField()
    Reviews_Counts = models.IntegerField() 
    Num_Pages = models.IntegerField() 
    Book_Format  = models.CharField(max_length=50)
    Time_publish = models.CharField(max_length=50) 
    Publisher = models.CharField(max_length=50) 
    ISBN = models.CharField(max_length=50) 
    Language = models.CharField(max_length=50) 
    Genres = models.JSONField() 
    Book_Url = models.CharField(max_length=100)
 
    class Meta:
        db_table = "Book_Details"
        verbose_name = 'Book Detail'
        verbose_name_plural = 'Book Details'
        ordering = ['Author_Name', 'Book_Title']
 
    def __str__(self):
        return self.Book_Title


class User_Rating_Information(models.Model):

    username = models.CharField(max_length=50)
    user_url = models.CharField(max_length=100)
    book_id = models.IntegerField()
    book_url = models.CharField(max_length=100)
    user_rating = models.FloatField()
 
    class Meta:
        db_table = "Book_Details"
        verbose_name = 'Book Detail'
        verbose_name_plural = 'Book Details'
        ordering = ['Author_Name', 'Book_Title']
 
    def __str__(self):
        return self.Book_Title