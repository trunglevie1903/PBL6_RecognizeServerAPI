from django.contrib import admin
from .models import Employees
# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
  list_display = ['employee_id', 'department_id', 'name', 'age', 'avatar', 'cv']
  search_fields = ['department_id', 'name']
  list_filter = ['employee_id', 'department_id', 'name', 'age']
admin.site.register(Employees, EmployeesAdmin)