import uuid
from django.db import models

# Create your models here.
class Lab(models.Model):
    lab_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lab_name = models.CharField(max_length=50)
    lab_description = models.CharField(max_length=250)

    JAVASCRIPT = 'JS'
    PYTHON = 'PY'
    JAVA = 'JV'
    LANGUAGE_CHOICES = (
        (JAVASCRIPT, 'JavaScript'),
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
    )
    lab_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default=JAVASCRIPT
    )
    lab_created_time = models.DateTimeField(auto_now_add=True)
    lab_modified_time = models.DateTimeField(auto_now=True)
    lab_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.lab_name