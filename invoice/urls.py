from django.urls import include, path
from rest_framework.routers import DefaultRouter
from invoice.views import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoice', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
