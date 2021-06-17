from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registration,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path('upload/',views.upload,name='upload'),
    path('update/<int:book_id>',views.update_book,name='update_book'),
    path('delete/<int:book_id>',views.delete_book,name='delete_book'),
    path('search/',views.search,name='search'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_URL}),
    
]
urlpatterns+=staticfiles_urlpatterns()