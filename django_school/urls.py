from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from classroom.views import classroom
import notifications.urls
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext








urlpatterns = [
    
 
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += i18n_patterns (
    path('', include('classroom.urls')),
    path('admin/', admin.site.urls),
    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

