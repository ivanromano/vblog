from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('blog/', include('vblog.url')),
    path('api/', SpectacularAPIView.as_view(), name='api'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api'), name='api-docs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html') )]


