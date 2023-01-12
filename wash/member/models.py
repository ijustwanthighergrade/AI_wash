from django.db import models

# Create your models here.

class COLOR(models.Model):
    MEMID = models.CharField('使用者編號',max_length=20, null=False)
    WHICHCOLOR = models.CharField('COLOR',max_length=20, null=False)
    def __str__(self):
        return self.MEMID