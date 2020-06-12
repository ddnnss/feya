from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# from page.views import customhandler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('events-content/', include('events_content.urls')),
    path('news/', include('news.urls')),
    path('promotions/', include('promotions.urls')),
    path('reviews/', include('reviews.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)