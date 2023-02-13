
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("expenses.urls"), name="expenses_urls"),
    path('summernote/', include('django_summernote.urls')),
]
