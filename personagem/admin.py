from django.contrib import admin
from .models import Personagem, PersonagemClasse, PersonagemModelo, PersonagemAtributo


admin.site.register(Personagem)
admin.site.register(PersonagemClasse)
admin.site.register(PersonagemModelo)
admin.site.register(PersonagemAtributo)
