from django.db import models


class Employee(models.Model):
	username = models.CharField(primary_key = True, max_length=15)
	employee_id = models.IntegerField(unique=True)
	email = models.EmailField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30) 
	body_temp = models.IntegerField(null= True)
	blood_pressure = models.IntegerField(null= True)
	respiration = models.IntegerField(null= True)
	glucose = models.IntegerField(null= True)
	heart_rate = models.IntegerField(null= True)
	oxygen_saturation = models.IntegerField(null= True)

	def __str__(self):
		return f'{self.employee_id} {self.username}'

