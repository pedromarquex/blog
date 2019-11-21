from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.


class PostView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm()
        comments = Comment.objects.filter(post=pk)
        context = {
            'post': post,
            'comment_form': comment_form,
            'comments': comments,
        }
        return render(request, template_name='post/post.html',
                      context=context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm()
        comment_text = request.POST['text']

        if request.user == AnonymousUser:
            user = User.objects.get(username="anon")
        else:
            user = request.user

        post_comment = Post.objects.get(pk=pk)

        Comment.objects.create(post=post_comment, user=user, text=comment_text)
        comments = Comment.objects.filter(post=post)

        context = {
            'comments': comments,
            'post': post,
            'comment_form': comment_form,
        }
        return render(request, template_name='post/post.html',
                      context=context)
