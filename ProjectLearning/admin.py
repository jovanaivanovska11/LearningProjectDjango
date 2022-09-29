from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import User, Person, Lecture, Forum, Reply

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email")

admin.site.register(Person, PersonAdmin)

class LectureVideos(AdminVideoMixin, admin.ModelAdmin):
    list_display = ("name", "time")

admin.site.register(Lecture, LectureVideos)

class ForumAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.name.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.name.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Forum, ForumAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.name.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.name.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Reply, ReplyAdmin)


