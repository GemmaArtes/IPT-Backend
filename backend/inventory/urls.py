from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, ReportViewSet, CategoryListView, ProductListView, ReportListView

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('api/', include(router.urls)),
]