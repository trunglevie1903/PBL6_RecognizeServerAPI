from django.db import models

# Create your models here.
class RecognizeHistory(models.Model):
  recognize_id = models.AutoField(primary_key=True)
  recognize_uuid = models.CharField(max_length=200, null=False)
  recognize_image = models.FileField(upload_to='images', null=False, default=None)

  def __str__(self):
    return f'{self.recognize_id} - {self.recognize_uuid} - {self.recognize_image}'
