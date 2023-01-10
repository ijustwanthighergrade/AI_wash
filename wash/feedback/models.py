from django.db import models

# Create your models here.
class REPROBLEMS(models.Model):
    PID = models.CharField('回報序號',max_length=43, editable=False,primary_key=True,default="001")
    MEMID=models.CharField('會員序號',max_length=43, editable=False,default="")
    ORDID =models.CharField('訂單序號',max_length=43,null=True)
    PTYPE=models.CharField('回報類型',max_length=43,null=True)
    PTIME=models.DateField ('回報時間',null=True, blank=True)
    PDISC=models.CharField('問題敘述',max_length=43,null=True)
    PRE=models.CharField('處理回覆',max_length=43,null=True)
    PDEAL=models.CharField('處理與否',max_length=43,null=True)
        
    class Meta:
        managed = True    
        
    
# 回報序號 VAR13 PK
# 會員序號 VAR13 
# 訂單序號 VAR13 
# 回報類型
# 回報時間 DATETIME
# 問題敘述 TEXT
# 處理回覆 TEXT
# 處理與否 INT
