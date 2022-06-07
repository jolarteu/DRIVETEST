from django.db import models

class drivetest(models.Model):
    name = models.CharField(max_length=100)
    csv = models.FileField(upload_to = "csv/", default=None)
    date=models.DateField(null=True)
    date_created = models.DateField(auto_now = True)
    kml = models.FileField(upload_to ="kml/", default=None)
    bill = models.FileField(upload_to ="bill/", default=None)


    def get_object(self):

        #link=str(self.uploadedFile)
        return str(uploadedFile.url)
