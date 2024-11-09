from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)  # Added domain field
    year_founded = models.IntegerField()  # Assuming year_founded is an integer
    industry = models.CharField(max_length=100)
    size_range = models.CharField(max_length=100)  # Added size_range field
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)  # Added country field
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)  # Added linkedin_url field
    current_employee_estimate = models.IntegerField(null=True, blank=True)  # Added current_employee_estimate field
    total_employee_estimate = models.IntegerField(null=True, blank=True)  # Added total_employee_estimate field

    def __str__(self):
        return self.name

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
