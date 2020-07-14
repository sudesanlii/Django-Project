from django.db import models

# Create your models here.
class ControlTable(models.Model):
    cuet=models.TextField(max_length=50,default='')
    uet=models.TextField(max_length=50,default='')
    atolye=models.TextField(max_length=20,default='')
    ca=models.TextField(max_length=20,default='')
    kontrolNoktasi=models.TextField(max_length=60, blank=True)
    kritiklik=models.CharField(max_length=10)
    frekans=models.IntegerField(default='')
    kontrolMetod=models.TextField(max_length=100,blank=True)
    
    def __str__(self):
        return self.cuet