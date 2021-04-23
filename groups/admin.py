from django.contrib import admin
from . import models


# Register your models here.

# allows us to utilise the admin interface with the ability to modify
# models on the same page as the parent model
class GroupMemberInline(admin.TabularInline):
    models = models.GroupMember


admin.site.register(models.Group)
