
from django.contrib import admin

# Register your models here.
from .models import HistoryHicAPI
from .models import HistoryPitSummaryAPI

admin.site.register(HistoryHicAPI)
admin.site.register(HistoryPitSummaryAPI)
