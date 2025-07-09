from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Student Portal Admin"
admin.site.site_title = "Student Portal Admin System"
admin.site.index_title = "Welcome to Student Portal Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]