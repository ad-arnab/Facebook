
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
   
    path('user/<int:user_id>/', views.user_link_view, name='user_link'),
    path('logout/', views.logout_view, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

