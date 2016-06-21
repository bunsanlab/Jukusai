from django.db import models
from program.models import program
import binascii
import os
# Create your models here.

class token(models.Model):
    key              = models.CharField(max_length=50)
    banFlag          = models.BooleanField(default=False)
    created_at       = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class photo(models.Model):
    program          = models.ForeignKey(program)
    token            = models.ForeignKey(token)
    path             = models.CharField(max_length=255, blank=True)
    publicFlag       = models.BooleanField(default=False)
    created_at       = models.DateTimeField(null=True, auto_now_add=True)
