from django.db import models

class DepartmentModel(models.Model):
	did   = models.IntegerField(primary_key=True)
	dname = models.CharField(max_length=20)

	def __str__(self):
		return self.dname


class StudentModel(models.Model):
	rno  = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 	20)
	dept = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)

	def __str__(self):
		return self.name