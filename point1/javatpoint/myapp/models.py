from django.db import models



class Employee(models.Model):
    eid = models.CharField(max_length=20,null=True)
    ename = models.CharField(max_length=100,null=True)
    econtact = models.CharField(max_length=15,null=True)

    class Meta:
        db_table = "employee"
