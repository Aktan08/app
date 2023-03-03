from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("productssite/", views.getProductsSite),
    path("productssite/<str:pk>/", views.getProductSite),
    path("productssite/images/<str:pk>/", views.getProductSiteImages),
    path("productssite/<str:pk>/image/<str:pp>/", views.getProductSiteImage),
    path("productssite/searchcategory/<str:name>/", views.getProductsSiteCategory),
    path("productssite/searchsubcategory/<str:name>/", views.getProductsSiteSubCategory),
    path("productssite/searchsubsubcategory/<str:name>/", views.getProductsSiteSubCategory),
    path("search/<str:str>/", views.search),
]
