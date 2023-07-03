from django.contrib import admin

from animals.models import Animals


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'kind_of_animal')
    search_fields = ('name', 'age', 'kind_of_animal')
    list_filter = ('kind_of_animal', 'age')
