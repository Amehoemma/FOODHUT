from django.db import models

# Create your models here.
class BookTable(models.Model):
    email=models.EmailField(max_length=25)
    number_guest=models.IntegerField(int)
    time=models.TimeField()
    date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

