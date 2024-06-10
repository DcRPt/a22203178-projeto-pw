from django.contrib import admin

from .models import Localizacao
from .models import Banda
from .models import Festival

admin.site.register(Localizacao)
admin.site.register(Banda)
admin.site.register(Festival)