from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserU(AbstractUser):
	Surname=models.CharField(max_length=50)
	Name=models.CharField(max_length=50)
	Fathername=models.CharField(max_length=50)
	class Meta:
		db_table = "table_users"
	def __str__(self):
		return self.Surname + " " + self.Name + " " + self.Fathername
# Create your models here.
