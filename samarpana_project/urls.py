"""
URL configuration for samarpana_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# samarpana_project/urls.py
from django.contrib import admin
from django.urls import path, include
from ticketing.views import CustomLoginView  # import your custom login view
from ticketing.views import CustomLogoutView  # Adjust import if needed


urlpatterns = [
    path('admin/', admin.site.urls),

    # Override the login URL with your custom login view
    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),


    # Include other auth URLs (logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Your app URLs
    path('', include('ticketing.urls')),
]
