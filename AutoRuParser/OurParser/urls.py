from django.urls import path, include
from OurParser import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
	path('autoruparser', views.autoruparser, name = 'autoruparser'),
	path('registration', views.registration, name = 'registration'),
    path('login', views.login_user, name = 'login_user'),
]

