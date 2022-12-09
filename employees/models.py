from django.db import models
from home.models import Department

# Create your models here.
class Employees(models.Model):
  employee_id = models.AutoField(primary_key=True)
  department_id = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=False)
  age = models.IntegerField(null=True)
  avatar = models.ImageField(upload_to='images', null=False, default=None)
  cv = models.FileField(upload_to='files', null=False, default=None)

  def __str__(self):
    return f'{self.employee_id} - {self.department_id} - {self.name} - {self.age} - {self.avatar} - {self.cv}'