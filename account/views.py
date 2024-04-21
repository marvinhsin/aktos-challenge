from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework.pagination import PageNumberPagination

# Setup up pagination for AccountView
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create view for Account
class AccountView(generics.ListAPIView):
    serializer_class = AccountSerializer
    pagination_class = CustomPagination

    # Create API that queries database by parameters
    def get_queryset(self):
        # Retrieve parameters from URL
        min_balance = self.request.query_params.get('min_balance')
        max_balance = self.request.query_params.get('max_balance')
        status = self.request.query_params.get('status')
        consumer_name = self.request.query_params.get('consumer_name')
        
        # Filter results according to optional parameters
        queryset = Account.objects.all()
        if min_balance:
            try:
                min_balance = float(min_balance)
                queryset = queryset.filter(balance__gte = min_balance)
            except TypeError:
                pass
        if max_balance:
            try:
                max_balance = float(max_balance)
                queryset = queryset.filter(balance__lte = max_balance)
            except TypeError:
                pass
        if status:
            try:
                status = str(status)
                queryset = queryset.filter(status = status.upper())
            except TypeError:
                pass
        if consumer_name:
            try:
                consumer_name = str(consumer_name)
                queryset = queryset.filter(consumer_name = consumer_name.lower())
            except TypeError:
                pass
        
        return queryset