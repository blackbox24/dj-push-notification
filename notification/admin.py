from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Notification
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync # make sync calls

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
                
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "notifications",
                    # define wat we want to do
                    {
                        "type":"send_notification", # use send_notification func
                        "message":message   # send message
                    }
                )

                return HttpResponseRedirect("../{}/".format(notification.pk))
        else:
            form = SendNotificationForm()
        context = self.get_changeform_initial_data(request)
        context["form"] = form
        return super().add_view(request,form_url,extra_context=context)
    
    def get_urls(self):
        urls = super().get_urls
        custom_url = [
            path("send-notification/",self.admin_site.admin_view(self.add_view),name="send-notification")
        ]
        return custom_url + urls
