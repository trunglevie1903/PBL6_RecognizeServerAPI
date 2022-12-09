from django.shortcuts import render
from .models import Department

# Create your views here.
def getHomePage(request):
  department_list = Department.objects.filter().order_by('department_id')
  return render(request, 'home.html', {'department_list': department_list})