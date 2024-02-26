from django.db import models

 
class PredResults(models.Model):
    #id = models.AutoField(primary_key=True)

    Age = models.FloatField()
    air_pollution = models.FloatField()
    alcohol_use = models.FloatField()
    genetic_risk = models.FloatField()
    chronic_lung_disease = models.FloatField()
 
    Level = models.CharField(max_length=30)

    def __str__(self):
        return self.Level
