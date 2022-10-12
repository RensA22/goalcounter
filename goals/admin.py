from django.contrib import admin
from .models import Wedstrijd, Goal, Assist

# Register your models here.
admin.site.register(Wedstrijd)
admin.site.register(Goal)
admin.site.register(Assist)
