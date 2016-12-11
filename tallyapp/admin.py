
from django.contrib import admin

# Register your models here.
from .models import HistoryHic
from .models import HistoryPitSummary

admin.site.register(HistoryHic)
admin.site.register(HistoryPitSummary)
