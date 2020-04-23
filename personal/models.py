from django.db import models

# Create your models here.
# PRIORITY = [
# 	("H","Low"),
# 	("L","Medium"),
# 	("H","High"),
# ]

# class Question(models.Model):
# 	tilte                   =models.CharField(max_length=60)
# 	question                =models.TextField(max_length=400)
# 	priority                =models.CharField(max_length=1,choices=PRIORITY)
	
# 	def __str__(self):
# 		return self.tilte

# 	class Meta: 
# 		verbose_name = "The Question"
# 		verbose_name_plural = "Peoples Question"