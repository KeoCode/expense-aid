from django.contrib import admin
from django.urls import path, include
from expenses.views import AuthorCreateView, AuthorCreateView, AuthorDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("expenses.urls"), name="expenses_urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]
