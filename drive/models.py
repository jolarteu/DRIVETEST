from django.db import models

class drivetest(models.Model):
    name = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to = "Files/")
    date=models.DateTimeField()
    date_created = models.DateTimeField(auto_now = True)
    extra = models.FileField(upload_to ="Extra/")
