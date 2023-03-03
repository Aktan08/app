from rest_framework.serializers import ModelSerializer
from .models import Gallery, SubCategory, Category, ProductSite, Company, SubSubCategory


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name",]


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["name",]

class SubSubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = ["name",]



class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["image"]


class ProductSiteSerializer(ModelSerializer):
    images = GallerySerializer(many=True)
    company = CompanySerializer(many=False)
    subcategory = SubCategorySerializer(many=False)
    subsubcategory = SubSubCategorySerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = ProductSite
        fields = ["id", "name", "content", "subcategory","subsubcategory", "category","company", "images",]

