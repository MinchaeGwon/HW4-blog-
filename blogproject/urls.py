from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)