from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'editprofile/(\d+)/$', views.edit_profile, name='edit_profile'),
    url(r'news/',views.news, name = 'news'),
    url(r'comment/',views.comment, name = 'comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)