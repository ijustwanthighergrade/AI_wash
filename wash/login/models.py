from django.db import models

# Create your models here.

#請在model建立以下資料表 記得最上面些寫這個 UUIDrand function 
import uuid
# Create your models here.
def UUIDrand():
    return str(uuid.uuid4())

class LOGIN(models.Model):
    FKcheck=models.CharField(max_length=36,default=UUIDrand)
    Rstate=models.CharField(max_length=42)
    Raccesscode=models.CharField(max_length=43)
