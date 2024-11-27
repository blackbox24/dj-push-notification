from django.contrib import admin
from .models import Notification

# Register your models here.
from django import forms

class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification",max_length=200)

@admin.register(Notification)
class NotifiationAdmin(admin.ModelAdmin):
    pass