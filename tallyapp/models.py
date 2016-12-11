
from django.db import models

class HistoryHic(models.Model):
    """
    Database schema for HistoryHic - City of Portland homeless shelter tally
    """

    shelter = models.CharField(max_length=60, null=True, default='')
    bedtype = models.CharField(max_length=60, null=True, default='')
    tallyyear = models.IntegerField()

    class Meta:
         ordering = ('shelter',)

    def __str__(self):
        return '%s %s %d' % (self.shelter, self.bedtype, self.tallyyear)

class HistoryPitSummary(models.Model):
    """
    Database schema for HistoryPitSummary - City of Portland homeless population tally
    """

    Table = models.CharField(max_length=17, null=True, default='')
    Population = models.CharField(max_length=32, null=True, default='')
    SubPopulation = models.CharField(max_length=37, null=True, default='')
    Date = models.DateField(null=True, blank=True)
    Value = models.CharField(max_length=11, null=True, default='')

    class Meta:
         ordering = ('Table',)

    def __str__(self):
        return '%s %s %s %s %s' % (self.Table, self.Population, self.Sub-Population, self.Date, self.Value)
