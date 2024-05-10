from django.contrib import admin
from .models import Cat_Movie


class movie_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('movie_name',)}
    list_display = ('movie_name', 'slug')


admin.site.register(Cat_Movie, movie_admin)

