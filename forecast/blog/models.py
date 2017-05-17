from django.db import models

class Register(models.Model):
    Username = models.CharField(max_length=140)
    Password = models.CharField(max_length=140)
   # Re-enter = models.CharField(max_length=140)
	

    def __str__(self):
        return self.Username
