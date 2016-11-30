"""facebook_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from users import views as user_views

from allauth.account import views as allauth_views
from allauth.socialaccount.providers.facebook.urls import urlpatterns as fb_urlpatterns
from allauth.socialaccount.urls import urlpatterns as social_urlpatterns

urlpatterns = [
    url(r'^$', login_required()(user_views.HomeView.as_view()), name="home"),
    url(r'^admin/', admin.site.urls),

    # All Auth urls
    url(r'^login/$', allauth_views.login, name="account_login"),
    url(r'^logout/$', allauth_views.logout, name="account_logout"),
    url(r"^signup/$", allauth_views.signup, name="account_signup"),
    url(r"^password/reset/$", allauth_views.password_reset,
        name="account_reset_password"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", allauth_views.confirm_email,
        name="account_confirm_email"),
]

urlpatterns += social_urlpatterns + fb_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
