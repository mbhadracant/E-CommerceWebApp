from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name
