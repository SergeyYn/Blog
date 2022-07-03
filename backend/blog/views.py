from django.shortcuts import render

from .models import Post, Category

from .serializers import PostSerializer, CategorySerializer

from rest_framework.viewsets import ModelViewSet


def channels_admin(request):
    return render(request, 'channels/users.html')


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.query_params.get('cat'):
            cat = self.request.query_params.get('cat')
            queryset = Post.objects.filter(category_id=cat).order_by('-post_date')
        else:
            queryset = Post.objects.all().order_by('-post_date')
        return queryset



class PostDetailViewSet(ModelViewSet):
    serializer_class = PostSerializer
    def put(self, request, id):
        print('AAAAAAA')
        post = self.get_object(pk=id)
        prev_cat = post.category.id

        data = request.data

        post_category = Category.object.get(id=data['category_id'])

        post.title = data['title']
        post.body = data['body']

        post.save(previous_cat=prev_cat)
        serializer = PostSerializer(post)
        return (serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


#def HomeView(request):
#    posts = Post.objects.all().order_by('-post_date')
#    context = {}
#    context['posts'] = posts
#    return render(request, 'home.html', context)
#
#
#def PostDetailView(request, pk):
#    post = Post.objects.get(id=pk)
#    context = {'post': post}
#    return (request,  context)


#def CreatePostView(request):
#    context = {}
#    if request.method == 'POST':
#        form = CreatePostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/')
#    else:
#        form = CreatePostForm()
#        context['form'] = form
#        return render(request, "create_post.html", context)


#def EditPostView(request, pk):
#    context = {}
#    post = Post.objects.get(id=pk)
#    if request.method == 'POST':
#        form = EditPostForm(request.POST, instance=post)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/post/' + str(pk))
#    else:
#        form = EditPostForm(initial={'title': post.title, 'category': post.category, 'body': post.body, })
#        context['form'] = form
#        context['post'] = post
#        return render(request, "edit_post.html", context)


#def DeletePostView(request, pk):
#    context = {}
#    post = Post.objects.get(id=pk)
#    if request.method == "POST":
#        post.delete()
#        return HttpResponseRedirect('/')
#    else:
#        context['post'] = post
#        return render(request, 'delete_post.html', context)


#def CreateCategoryView(request):
#    context = {}
#    if request.method == 'POST':
#        form = CreateCategoryForm(request.POST)
#        print(form.errors)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/category-list/')
#    else:
#        form = CreateCategoryForm()
#        context['form'] = form
#        return render(request, "create_category.html", context)



#def CategoryView(request, cat):
#    category_posts = Post.objects.filter(category=cat).values()
#    print(category_posts)
#    category = Category.objects.filter(id=cat).values()
#    print(category)
#    return JsonResponse({'category': list(category), 'category_posts': list(category_posts)})


#def CategoryListView(request):
#    category_menu_list = Category.objects.values('id', 'name').order_by('name')
#    return render(request, 'category_list.html', {'category_menu_list': category_menu_list})

