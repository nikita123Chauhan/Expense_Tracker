from django.contrib import admin
from django.urls import path
from tracker import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='home'),  # Root URL (home page)
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
