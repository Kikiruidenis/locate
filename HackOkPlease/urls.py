
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^child/", include("HackOkapp.urls", namespace="child")),
    url(r"^$", views.home, name="home"),
    url('about/', views.about, name="about"),
    url('contact/', include('contact.urls', namespace='contact', app_name='contact')),
    url(r"^login/$", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
]
if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
	urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

