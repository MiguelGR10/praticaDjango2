from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='index'),
    path('<slug:slug>/', post, name='detallep'),
    #ath('categorias', categorias, name='categorias'),
    #path('<slug:categoria>/', lista, name='lista'),
    #path('<categoria:categoria>/', bloca, name="bloca"),
    

    path('Tecnologias', tecno, name='Tecnologia'),
    path('Deportes', depo, name='Deportes'),
    path('Ciencias', cien, name='Ciencias'),
    path('Espectaculoss', espc, name='Espectaculos'),
    path('Salud', sal, name='Salud'),
    path('Historia', his, name='Historia'),
    path('Educacion', edu, name='Educacion'),
    path('Videojuegos', vid, name='Videojuegos'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)