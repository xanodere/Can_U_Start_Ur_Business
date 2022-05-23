
from django.contrib import admin
from django.urls import include,path

admin.site.site_header = "Business Audit Admin"
admin.site.site_title = "Business Audit Admin"
admin.site.index_title = "Welcome to Business audit"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls"))
]
