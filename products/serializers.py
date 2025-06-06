from rest_framework import serializers
from .models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(     
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id', 'image', 'rating']
        read_only_fields = ['id', 'rating'] 

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) 
    
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']