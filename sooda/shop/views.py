from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, GallerySerializer, ProductSiteSerializer
from .models import Category, Gallery, SubCategory, ProductSite


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"Endpoint": "", "method": "GET", "body": None, "description": "Ссылки"},
        {
            "Endpoint": "/productssite",
            "method": "GET",
            "body": None,
            "description": "Продукты",
        },
        {
            "Endpoint": "/productssite/<str:pk>",
            "method": "GET",
            "body": None,
            "description": "продукт по id",
        },
        {
            "Endpoint": "productssite/images/<str:pk>",
            "method": "GET",
            "body": None,
            "description": "фотографии продукта ",
        },
        {
            "Endpoint": "productssite/<str:pk>/image/<str:pp>",
            "method": "GET",
            "body": None,
            "description": "Создано",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getCategories(request):
    Categories = Category.objects.all()
    serializer = CategorySerializer(Categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProducts(request):
    products = SubCategory.objects.all()
    serializer = ProductSiteSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = SubCategory.objects.get(id=pk)
    serializer = ProductSiteSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getProductsSite(request):
    productsSite = ProductSite.objects.all()
    serializer = ProductSiteSerializer(productsSite, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProductsSiteCategory(request,name):
    productsSite =  ProductSite.objects.all()
    productsSiteCategory = (filter(lambda x: ( x.category.name == name), productsSite))
    serializer = ProductSiteSerializer(productsSiteCategory, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProductsSiteSubCategory(request,name):
    productsSite =  ProductSite.objects.all()
    productsSiteCategory = (filter(lambda x: ( x.subcategory.name == name), productsSite))
    serializer = ProductSiteSerializer(productsSiteCategory, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProductsSiteSubCategory(request,name):
    productsSite =  ProductSite.objects.all()
    productsSiteCategory = (filter(lambda x: ( x.subsubcategory.name == name), productsSite))
    serializer = ProductSiteSerializer(productsSiteCategory, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProductSite(request, pk):
    productSite = ProductSite.objects.get(id=pk)
    serializer = ProductSiteSerializer(productSite, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getProductSiteImages(request, pk):
    productSiteImages = ProductSite.objects.get(id=pk).images.all()
    serializer = GallerySerializer(productSiteImages, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProductSiteImage(request, pk, pp):
    productSiteImages = ProductSite.objects.get(id=pk).images.get(id=pp)
    serializer = GallerySerializer(productSiteImages, many=False)
    return Response(serializer.data)



@api_view(["GET"])
def search(request,str):
    filteredProducts = filter(lambda x: x.name.__contains__(str) or x.subcategory.name.__contains__(str) or x.category.name.__contains__(str)or x.subsubcategory.name.__contains__(str)  , ProductSite.objects.all())
    serializer = ProductSiteSerializer(filteredProducts , many=True)
    return Response(serializer.data)



