from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomerCategory, Product
from .serializers import CustomerCategorySerializer, ProductSerializer
from .permissions import CanModifyProduct

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomerCategory.objects.all().order_by("id")
    serializer_class = CustomerCategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all().order_by("id")
    serializer_class = ProductSerializer
    permission_classes = [CanModifyProduct]
