from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


echo "# Anvarov-AsqarbekModule6" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/awaxos/Anvarov-AsqarbekModule6.git
git push -u origin main