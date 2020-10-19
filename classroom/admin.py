from django.contrib import admin
from .models import Process, Activity, Decision, Type_actors,Output,Task,Input, Actor, Technologie


# Register your models here.

admin.site.register(Process)
admin.site.register(Activity)
admin.site.register(Type_actors)
admin.site.register(Decision)
admin.site.register(Output)
admin.site.register(Task)
admin.site.register(Input)
admin.site.register(Actor)
admin.site.register(Technologie)

