from django.db import models

# Create your models here.

class ProbeModelDetail(models.Model):
    ModelName = models.CharField(max_length=20)
    PortCount = models.IntegerField()
    CPU = models.CharField(max_length=50)
    Memony = models.CharField(max_length=50)
    HDD = models.CharField(max_length=50)
    Provider = models.IntegerField()
    UsedCount = models.IntegerField()
    Note = models.CharField(max_length=200,null=True,blank=True)

class ProbeList(models.Model):
    ProbeID = models.IntegerField(primary_key=True)
    ModelID = models.ForeignKey(ProbeModelDetail,on_delete=models.CASCADE)
    Status = models.IntegerField()
    CreateDate = models.DateField()
    Note = models.CharField(max_length=200,null=True,blank=True)
