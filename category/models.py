from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Products(models.Model):
	Subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	def __str__(self):
		return self.name	