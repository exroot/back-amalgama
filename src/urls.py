"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('src.api.authentication.urls', 'authentication'), namespace="authentication")),
    path('api/v1/', include(('src.api.categories.urls', 'categories'), namespace="categories")),
    path('api/v1/', include(('src.api.currencies.urls', 'currencies'), namespace="currencies")),
    path('api/v1/', include(('src.api.registries.urls', 'registries'), namespace="registries")),
    path('api/v1/', include(('src.api.users.urls', 'users'), namespace="users"))
    # path('api/v1/', include(('src.api.expenses.urls'), namespace="expenses")),
    # path('api/v1/', include(('src.api.incomes.urls'), namespace="incomes")),
    # path('api/v1/', include(('src.api.reports.urls'), namespace="reports")),
]
