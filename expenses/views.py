from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Post
from expenses.forms import AddPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post
            },
        )


class AuthorCreateView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = '/'
    success_message = '%(title) was created'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)