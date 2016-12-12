
from django.db import models


class HistoryPitSummaryAPI(models.Model):
    """
    Database schema for City of Portland's Point-In-Time Counts (HistoryPitSummary)
    """

    Table = models.CharField(max_length=17, null=True, default='')
    Population = models.CharField(max_length=40, null=True, default='')
    SubPopulation = models.CharField(max_length=40, null=True, default='')
    Date = models.DateField(null=True, blank=True)
    Value = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
         ordering = ('Date', 'Table', 'Population',  'SubPopulation', )

    def __str__(self):
        return '%s %s %s %s' % (self.Table, self.Population, self.SubPopulation, self.Date)

class HistoryPitSubpopulationsAPI(models.Model):
    """
    Database schema for City of Portland's Point-In-Time Subpopulation Counts (HistoryPitSubpopulations)
    """

    Table = models.CharField(max_length=18, null=True, default='')
    Population = models.CharField(max_length=67, null=True, default='')
    Shelter = models.CharField(max_length=40, null=True, default='')
    Date = models.DateField(null=True, blank=True)
    Value = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
        ordering = ('Date', 'Table', 'Population', 'Shelter', )

    def __str__(self):
        # return '%s %s %s %s %f' % (self.Table, self.Population, self.Shelter, self.Date, self.Value)
        return '%s %s %s %s' % (self.Table, self.Population, self.Shelter, self.Date)

class HistoryHicAPI(models.Model):
    """
    Database schema for City of Portland's Housing-Inventory-Count (HistoryHic)
    """

    Table = models.CharField(max_length=23, null=True, default='')
    Shelter = models.CharField(max_length=40, null=True, default='')
    UnitBed = models.CharField(max_length=40, null=True, default='')
    Date = models.DateField(null=True, blank=True)
    Value = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
         ordering = ('Date', 'Table', 'Shelter', 'UnitBed', )

    def __str__(self):
        return '%s %s %s' % (self.Shelter, self.UnitBed, self.Date)
