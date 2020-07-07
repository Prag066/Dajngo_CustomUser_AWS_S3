from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('login/',views.UserLoggedIn,name='login'),
    path('',views.UserRegistration,name='registration'),
    path('registration/',views.UserRegistration,name='registration'),
    path('user-profile',views.UserProfile,name='userprofile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)