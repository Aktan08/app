from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
    # path("products/v1/auth", include("djoser.urls")),
    # re_path("auth/", include("djoser.urls.authtoken")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
