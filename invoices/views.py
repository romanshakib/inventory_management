from django.db.models import Count, Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Invoice
from .serializers import InvoiceSerializer
from .permissions import CanModifyInvoice

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related("product", "created_by").all().order_by("-created_at")
    serializer_class = InvoiceSerializer
    permission_classes = [CanModifyInvoice]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=["get"], url_path="report")
    def report(self, request):
        summary = Invoice.objects.aggregate(
            total_invoices=Count("id"),
            total_sales=Sum("total"),
            total_products_sold=Sum("quantity"),
        )
        return Response({
            "total_invoices": summary["total_invoices"] or 0,
            "total_sales": summary["total_sales"] or 0,
            "total_products_sold": summary["total_products_sold"] or 0,
        }, status=status.HTTP_200_OK)
