from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# ✅ Pagination
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'   # ?limit=10
    page_query_param = 'page'

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=False)

        # 🔍 Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)

        # 🎯 Category filter
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        # 💰 Price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    # ❌ Soft Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"message": "Product soft deleted"})