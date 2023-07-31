from django.contrib import admin
from django.urls import path, include

admin.site.site_url = "https://localhost:8000/admin"
admin.site.site_header = "JoupiLou Admin"
admin.site.site_title = "JoupiLou Admin Portal"
admin.site.index_title = "Welcome to JoupiLou Portal"
from .views import CustLogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('joupilou_members.urls')),
    path('accounts/logout/', CustLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

]
