from django.contrib import admin
from .models import Lagostas_brabas, Agregados, Tabelados

# Register your models here.

admin.site.register(Lagostas_brabas)
admin.site.register(Agregados)
admin.site.register(Tabelados)

# template pro forms

from .models import Author
from .forms import AuthorForm

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm

admin.site.register(Author, AuthorAdmin)