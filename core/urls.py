from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
admin.site.enable_nav_sidebar = False



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('camel.urls', namespace='camel')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'camel admin'
admin.site.site_title = 'camel admin'
admin.site.site_url = 'https://camel/'
admin.site.index_title = 'camel administration'