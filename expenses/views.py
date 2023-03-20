from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from .models import Post, User
from expenses.forms import AddPostForm


class PostList(generic.ListView):
    paginate_by = 6
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        else:
            return Post.objects.none()


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post
            },
        )


class AuthorCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = '/'
    success_message = 'Post was Created Successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'update_post.html'
    success_url = '/'
    success_message = "Post was Updated successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Post was Updated successfully"


class AuthorDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = '/'
    success_message = 'Post was Deleted Successfully'
