from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from store.filters import ProductFilter
from store.models import Product
from store.serializer import ProductSerializer


# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all() ## brings all object in dataBase
    serializer = ProductSerializer(products, many=True) ## because many items must be true
    return Response({
        'products': serializer.data
    })

@api_view(['GET'])
def get_by_id_product(request,pk):
    products = get_object_or_404(Product , pk=pk) ## brings one object
    serializer = ProductSerializer(products, many=False) ## because one item must be false
    return Response({
        'products': serializer.data
    })

@api_view(['GET'])
def get_all_products_by_filter(request):
    filtered_product = ProductFilter(request.GET,queryset=Product.objects.all().order_by('addAt'))
    serializer = ProductSerializer(filtered_product.qs, many=True)
    return Response({
        'products': serializer.data
    })

##how many pages (elements) to show
@api_view(['GET'])
def get_all_products_by_Pagination(request):
    filterSet = ProductFilter(request.Get , queryset=Product.objects.all().order_by('addAt'))
    resPage = 2
    paginator = PageNumberPagination()
    paginator.page_size=resPage
    querySet = paginator.paginate_queryset(filterSet.qs,request)
    serializer = ProductSerializer(querySet,many=True)
    return Response({
        'products': serializer.data
    })