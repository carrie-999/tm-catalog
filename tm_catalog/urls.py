from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel administracyjny
    path('admin/', admin.site.urls),

    # Logowanie / wylogowanie
    path('accounts/', include('django.contrib.auth.urls')),

    # Obsługa zmiany języka
    path('i18n/', include('django.conf.urls.i18n')),

    # Główne widoki Twojej aplikacji pod '/'
    path('', include('catalog.urls', namespace='catalog')),
]
