from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^about/$', views.about, name='about'),
	url(r'^single_post/(?P<ppk>\d+)$', views.single_post, name='single_post')
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)