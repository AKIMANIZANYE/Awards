from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^project/(\d+)',views.project,name ='home'),
    url(r'^$', views.post_today, name = 'post_today'),
   
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^awards/project$', views.new_project, name='new-project'),
     
     url(r'^rating/(?P<id>\d+)', views.rating, name='rating'),
   
    url(r'^profile/', views.profile, name='profile'),

    url(r'^upload_images/', views.upload_images, name='upload_images'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'^api/merch/$', views.MerchList.as_view()) 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
