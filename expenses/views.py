from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post
            },
        )


class AuthorCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'add_post.html'
    success_url = '/'
    success_message = '%(title) was created'

    # def get(self, request):
    #     add = ''
    #     form = AddPostForm()

    # def post(self, request, *args, **kwargs):
    #     form = AddPostForm(request.POST)
    #     if form.is_valid():
    #         add = form.cleaned_data['add/']

    # title = request.POST.get('post_title')
    # date = request.POST.get('post_date')
    # expense_amount = request.POST.get('post_expense_amount')
    # content = request.POST.get('post_content')
    # image =request.POST.get('post_image')
    #  Post.objects.create(title=title, date=date, expense_amount=expense_amount, content=content)

    # return redirect('index.html')

    # return render(request, 'add_post.html')
