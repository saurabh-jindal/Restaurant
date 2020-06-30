from django.db import models

# Create your models here.
## Booktable Model
class Booktable(models.Model):
    name = models.CharField(max_length= 50)
    email= models.EmailField()
    phone =models.CharField(max_length= 12)
    date = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
    count= models.IntegerField()
    message =models.TextField()

    def __str__(self):
        return 'Table booked by ' + self.name + ' for ' + self.count + ' people. '

class FoodItem(models.Model):
    name = models.CharField(max_length = 50)
    small_desc = models.TextField()
    large_desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='main_app/images', default='')
    tag = models.CharField(max_length = 20)
    # special = models.BooleanField()

    def __str__(self):
        return 'Item added ' +self.name


class Special(models.Model):
    item = models.OneToOneField(FoodItem, on_delete= models.CASCADE)

    def __str__(self):
        return self.item.name

class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return "New Email added " + self.email

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return " New message recieved from "+ self.name