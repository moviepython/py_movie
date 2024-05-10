from django.contrib import admin
from .models import List_Movies


class list_movie_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('movies',)}
    list_display = ('movies', 'slug')


admin.site.register(List_Movies, list_movie_admin)