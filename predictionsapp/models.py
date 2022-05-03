from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Sequences(models.Model):
    sequence=models.TextField(max_length=600)
    prediction=models.CharField(max_length=1)
    probnotvenom=models.FloatField(default=0.0)
    probvenom=models.FloatField(default=0.0)
    # fasta_file = models.FileField(default='default.fasta', blank=True, validators=[FileExtensionValidator(allowed_extensions=['fasta'])])
    date=models.DateTimeField(auto_now_add=True)
    consultant=models.ForeignKey(User, default=None, on_delete=models.PROTECT)
