from django.shortcuts import render, redirect
from .models import Employees
from home.models import Department

# Create your views here.
def getEmployees(request, id):
  employees_list = Employees.objects.filter(department_id = id).order_by('employee_id')
  department = Department.objects.get(department_id = id)
  return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})

def getAddEmployee(request):
  department_list = Department.objects.filter().order_by('department_id')
  return render(request, 'addEmployeeForm.html', {'department_list': department_list})

def addEmployee(request):
  if request.method == 'POST':
    return
  else:
    return render(request, 'error.html')