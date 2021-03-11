from django import forms
from .models import DepartmentModel
from .models import StudentModel

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = DepartmentModel
		fields = "__all__"

class StudentForm(forms.ModelForm):
	class Meta:
		model = StudentModel
		fields = "__all__"
