from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='Chat Seguro'),
    path('timeline/', views.timeline, name='Timeline'),
    path('signup/', views.signup, name='Sign Up'),
    path('contect/', views.contect, name='Contect'),
    path('forgotpasswd/', views.forgotpasswd, name='ForgotPassword'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('timeline/logout/', views.logout, name='logout'),
    path('timeline/story/', views.story, name='Story'),
    path('timeline/searchUser/', views.searchUser, name='searchUser'),
    path('get_support/', views.get_support, name='Send Query'),
    path('admin/', admin.site.urls),
]


handler404 = 'Chat.views.error'
