from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null = True)
    price       = models.DecimalField(decimal_places=3, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField() # null=True, default= True