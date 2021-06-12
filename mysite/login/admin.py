from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Person


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'gender', 'email',
                    'date_created')
    list_filter = ('gender', )


class EmailListFilter(SimpleListFilter):
    pass
