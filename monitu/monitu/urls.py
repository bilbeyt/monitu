"""monitu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django.contrib.auth.views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import accounts.views as views
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.RegisterView.as_view(template_name='home.html'), name='home'),
    url(r'^accounts/login/$', auth_views.login, {'authentication_form': LoginForm}, name='login'),
    url(r'^accounts/register/$', views.RegisterView.as_view(), name='register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/itupass/$', views.itupass, name='itupass'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

