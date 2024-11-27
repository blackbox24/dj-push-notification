from django.contrib import admin
from .models import Notification

# Register your models here.
from django import forms

class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification",max_length=200)

@admin.register(Notification)
class NotifiationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custom_add_form.html"

    def add_view(self,request,form_url="",extra_context=None):
        if request.method == "POST":
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]
                notification = Notification.objects.create(message=message)

        else:
            form = SendNotificationForm()
        context = self.get_changeform_initial_data(request)
        context["form"] = form
        return super().add_view(request,form_url,extra_context=context)