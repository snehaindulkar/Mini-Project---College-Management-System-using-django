from django.shortcuts import render,redirect
from .models import DepartmentModel,StudentModel
from .forms import DepartmentForm,StudentForm

def home(request):
	return render(request,'home.html')

def showdept(request):
	data = DepartmentModel.objects.all()
	return render(request,'showdept.html',{'data':data})

def adddept(request):
	if request.method =="POST":
		f = DepartmentForm(request.POST)
		if f.is_valid():
			f.save()
			fm = DepartmentForm()
			return render(request,'adddept.html',{'fm':fm,'msg':'Record added'})
		else:
			return render(request,'adddept.html',{'fm':f,'msg':'Check errors'})
	else:
		fm = DepartmentForm()
		return render(request,'adddept.html',{'fm':fm})

def addstudent(request):
	if request.method =="POST":
		f = StudentForm(request.POST)
		if f.is_valid():
			f.save()
			fm = StudentForm()
			return render(request,'addstudent.html',{'fm':fm,'msg':'Record added'})
		else:
			return render(request,'addstudent.html',{'fm':f,'msg':'Check errors'})
	else:
		fm = StudentForm()
		return render(request,'addstudent.html',{'fm':fm})

def showstudent(request):
	data = StudentModel.objects.all()
	return render(request,'showstudent.html',{'data':data})

def deletedept(request,id):
	d = DepartmentModel.objects.get(did=id)
	d.delete()
	return redirect('showdept')


def deletestudent(request,id):
	d = StudentModel.objects.get(rno=id)
	d.delete()
	return redirect('showstudent')