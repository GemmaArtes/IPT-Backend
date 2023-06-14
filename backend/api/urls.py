from django.urls import path, include

app_name = 'inventory'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('inventory/', include('inventory.urls')),
]