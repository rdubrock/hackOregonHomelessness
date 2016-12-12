
from django.contrib import admin

# Register your models here.
from .models import HistoryPitSummaryAPI
from .models import HistoryPitSubpopulationsAPI
from .models import HistoryHicAPI

admin.site.register(HistoryPitSummaryAPI)
admin.site.register(HistoryPitSubpopulationsAPI)
admin.site.register(HistoryHicAPI)
