from django.db import models

# Create your models here.
class Document(models.Model):
    WORD = 'WORD'
    PDF = 'PDF'
    TYPES_CHOICES = (
        (WORD, 'Word'),
        (PDF, 'PDF'),
    )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=2,
                            choices=TYPES_CHOICES,
                            default=PDF)
    upload = models.FileField(upload_to='uploads/')
    topics = models.CharField(max_length=500)
