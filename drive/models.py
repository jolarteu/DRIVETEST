from django.db import models
from django.contrib.auth.models import User

class drivetest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    csv = models.FileField(upload_to = "csv/", default=None)
    date=models.DateField(null=True)
    date_created = models.DateField(auto_now = True)
    kml = models.FileField(upload_to ="kml/", default=None)
    bill = models.FileField(upload_to ="bill/", default=None, blank=True)


    def get_object(self):

        #link=str(self.uploadedFile)
        return str(uploadedFile.url)
