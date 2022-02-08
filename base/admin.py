from django.contrib import admin

from .models import Message, Room, Topic


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "topic",
        "description",
        "host",
        "created",
        "updated",
    )


class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "user",
        "body",
        "created",
        "updated",
    )


admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
