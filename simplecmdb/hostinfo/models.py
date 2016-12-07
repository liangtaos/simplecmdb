from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.IPAddressField()
    vendor = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    sn = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    cpu_num = models.IntegerField()
    memory = models.CharField(max_length=50)
    osver = models.CharField(max_length=50)
    def __unicode__(self):
        return self.hostname

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)
    member = models.ManyToManyField(Host)
