from django.db import models

# Create your models here.

from django.utils import timezone

# Create your models here.
class order(models.Model):
    ORDID = models.CharField('訂單編號',max_length=20, null=False)
    MEMID = models.CharField('使用者編號',max_length=20, null=False)
    APPID = models.IntegerField('app編號',null=False)
    C_AMOUNT = models.IntegerField('花費的碳稅')
    GPOINT = models.IntegerField('獲得的點數')
    AMOUNT = models.IntegerField('消費總金額')
    CDATE = models.DateTimeField('成立時間',default = timezone.now)

    def __str__(self):
        return self.ORDID

class WMODE(models.Model):
    WMODE = models.CharField('模式名稱',max_length=20, null=False)
    MONEY = models.IntegerField('價格', null=False)
    POINTS = models.IntegerField('碳權點數',null=False)
    MEMISSIONS = models.IntegerField('碳排(公斤)')
    TIME = models.IntegerField('所需時間(分鐘)')

    def __str__(self):
        return self.WMODE

class LMODE(models.Model):
    LMODE = models.CharField('模式名稱',max_length=20, null=False)
    MONEY = models.IntegerField('價格', null=False)
    POINTS = models.IntegerField('碳權點數',null=False)
    MEMISSIONS = models.IntegerField('碳排(公斤)')
    TIME = models.IntegerField('所需時間(分鐘)')

    def __str__(self):
        return self.LMODE

class FMODE(models.Model):
    FMODE = models.CharField('模式名稱',max_length=20, null=False)
    MONEY = models.IntegerField('價格', null=False)
    POINTS = models.IntegerField('碳權點數',null=False)
    MEMISSIONS = models.IntegerField('碳排(公斤)')
    TIME = models.IntegerField('所需時間(分鐘)')

    def __str__(self):
        return self.FMODE

class CLIST(models.Model):
    ORDID = models.CharField('訂單編號', max_length=20, null=False)
    WMODE = models.ForeignKey(WMODE, on_delete=models.CASCADE)
    LMODE = models.ForeignKey(LMODE, on_delete=models.CASCADE)
    FMODE = models.ForeignKey(FMODE, on_delete=models.CASCADE)
    BAGNUM = models.IntegerField('袋數', default=1)
    PRICE = models.IntegerField('總金額', default=0)
    TIME = models.IntegerField('總時長', default=0)

    def save(self, *args, **kwargs):
    # 自動產生訂單編號
        i = 1
        while True:
            ordid = f"{i:03d}"
            if not CLIST.objects.filter(ORDID=ordid).exists():
                self.ORDID = ordid
                break
            i += 1
        # 計算總金額和總時長
        self.PRICE = self.WMODE.MONEY + self.LMODE.MONEY + self.FMODE.MONEY + self.BAGNUM * 50 + self.WMODE.MEMISSIONS * 3 + self.LMODE.MEMISSIONS * 3 + self.FMODE.MEMISSIONS * 3
        from .models import order
        order.AMOUNT = self.WMODE.MONEY + self.LMODE.MONEY + self.FMODE.MONEY + self.BAGNUM * 50 + self.WMODE.MEMISSIONS * 3 + self.LMODE.MEMISSIONS * 3 + self.FMODE.MEMISSIONS * 3
        order.GPOINT = self.WMODE.POINTS + self.LMODE.POINTS + self.FMODE.POINTS+ self.BAGNUM * 20
        order.C_AMOUNT = self.WMODE.MEMISSIONS * 3 + self.LMODE.MEMISSIONS * 3 + self.FMODE.MEMISSIONS * 3

        # 建立新的 order 資料
        order = order.objects.create(
            ORDID=self.ORDID,
            # 其他欄位
            APPID=7,
            AMOUNT=self.PRICE,
            GPOINT=self.WMODE.POINTS + self.LMODE.POINTS + self.FMODE.POINTS+ self.BAGNUM * 20,
            C_AMOUNT=self.WMODE.MEMISSIONS * 3 + self.LMODE.MEMISSIONS * 3 + self.FMODE.MEMISSIONS * 3,
        )
        order.save()

        import math
        self.TIME = math.ceil((self.WMODE.TIME + self.LMODE.TIME + self.FMODE.TIME) / 60)
        super().save(*args, **kwargs)

class delivery(models.Model):
    ORDID = models.CharField('訂單編號',max_length=20, null=False)
    SHOPID = models.CharField('店鋪編號',max_length=20, null=False)
    PHONE = models.CharField('使用者電話',max_length=10)
    ADDRESS = models.CharField('使用者地址',max_length=40)
    GDATE = models.DateTimeField('取件時間',default = timezone.now)
    S_CODE = models.CharField('取件條碼',max_length=20)
    G_CODE = models.CharField('送件條碼',max_length=20)

    def __str__(self):
        return self.ORDID

class shop(models.Model):
    SHOPID = models.CharField('店鋪編號',max_length=20, null=False)
    SHOPNAME = models.CharField('店鋪名稱',max_length=10)
    ADDRESS = models.CharField('使用者地址',max_length=40)

    def __str__(self):
        return self.SHOPID

class bag(models.Model):
    BID = models.CharField('洗衣袋編號',max_length=20, null=False)
    MEMID = models.CharField('使用者編號',max_length=20, null=False,default=0)
    GDATE = models.DateTimeField('租借時間',default = timezone.now)
    RDATE = models.DateTimeField('歸還時間',default = timezone.now)

    def __str__(self):
        return self.BID

class lock(models.Model):
    LOCKID = models.CharField('鎖櫃編號',max_length=20, null=False)
    ORDID = models.CharField('訂單編號',max_length=20, null=False)
    INDATE = models.DateTimeField('放入時間',default = timezone.now)
    OUTDATE = models.DateTimeField('取出時間',default = timezone.now)

    def __str__(self):
        return self.LOCKID