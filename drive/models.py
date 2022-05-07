from django.db import models

class drivetest(models.Model):
    name = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to = "Files/", default=None)
    # #date=models.DateField(null=True)
    # date_created = models.DateField(auto_now = True)
    # extra = models.FileField(upload_to ="Extra/")
