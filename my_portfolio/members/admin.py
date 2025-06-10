from django.contrib import admin
from .models import Member #add

# Register your models here.
# add
class MemberAdmin(admin.ModelAdmin):
    list_display = ("lastname","firstname","joined_date",)

admin.site.register(Member, MemberAdmin) #add
