from django.template.defaulttags import url
from django.urls import path, include

from .views import PostViewSet, CategoryViewSet #PostDetailView, CategoryView,  CreatePostView, EditPostView, DeletePostView, CreateCategoryView, \


from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]

#urlpatterns = [
#    path('', HomeView, name='home'),
#    path('post/<int:pk>', PostDetailView, name='post-details'),
#    path('post/create', CreatePostView, name='create-post'),
#    path('post/edit/<int:pk>', EditPostView, name='edit-post'),
#    path('post/delete/<int:pk>', DeletePostView, name='delete-post'),
#    path('category/create', CreateCategoryView, name='create-category'),
#    path('category/<int:category>', CategoryView, name='category'),
#    path('category-list/', CategoryListView, name='category-list')
#]