from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, url
from django.views.static import serve
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='Chat Seguro'),    
    path('admin/', admin.site.urls),
    path('timeline/', views.timeline, name='Timeline'),
    path('signup/', views.signup, name='Sign Up'),
    path('contect/', views.contect, name='Contect'),
    path('forgotpasswd/', views.forgotpasswd, name='ForgotPassword'),
    path('forgotpasswd/resetpass/', views.resetpass, name='Resetpass'),
    path('forgotpasswd/savepass/', views.savepass, name='Resetpass'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('timeline/logout/', views.logout, name='logout'),
    path('timeline/story/', views.story, name='Story'),
    path('timeline/searchUser/', views.searchUser, name='searchUser'),
    path('timeline/getstatus/', views.sendStatus, name='sendstatus'),
    path('timeline/savemessage/', views.saveMessage, name='savemessage'),
    path('timeline/getmessage/', views.getMessage,),
    path('timeline/cmsg/', views.cmsg,),
    path('timeline/getuser/', views.getUser,),
    path('get_support/', views.get_support, name='Send Query'),
    path('matchnum/', views.matchnumber, name="matchnumber"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': 
        settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': 
        settings.STATIC_ROOT}),
]


handler404 = 'Chat.views.error'