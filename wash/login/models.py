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

class MEMBER(models.Model):
    MEMID=models.CharField(max_length=43, primary_key=True, editable=False)
    MEMADDR=models.CharField(max_length=128,default="")
    MEMPHONE=models.CharField(max_length=12,default="")
    ACCESS=models.CharField(max_length=43,default="")
    MEMBAGS=models.CharField(max_length=8,default="")
    MEMCARD=models.CharField(max_length=8,default="")
    
class AGREE(models.Model):
    MEMID=models.CharField(max_length=43, primary_key=True, editable=False)
    
    
# 會員資料表
# 會員編號 VAR13 PK MEMID
# 會員姓名 VAR20
# 會員電話 VAR12
# 會員地址 VAR128
# 洗衣袋編號 VAR8
# ACCESS_CODE VAR8

