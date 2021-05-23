from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Blog, Comment, Like
from django.contrib.auth.decorators import login_required

# Login required for class based view
from django.contrib.auth.mixins import LoginRequiredMixin 
import uuid 
from . import forms
from django.urls import reverse_lazy

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all().order_by('-publish_date')

    return render(request, 'App_Blog/blog_list.html', context={'blogs': blogs})

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form): # This function name is default.
        blog_obj = form.save(commit = False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4()) # Change all spaces with '-' .... sanyam-garg-id
        blog_obj.save()
        
        return redirect('index')

def blog_details(request, slug):
    blog = Blog.objects.get(slug = slug)
    comment = forms.CommentForm()
    liked = Like.objects.filter(blog=blog, user=request.user)

    if liked:
        already_liked = True
    else:
        already_liked = False    

    if request.method == 'POST':
        comment = forms.CommentForm(request.POST)

        if comment.is_valid():
            comment_final = comment.save(commit=False)
            comment_final.user = request.user
            comment_final.blog = blog
            comment_final.save()

            return redirect('App_Blog:blog_details', slug = slug)

    diction = {
        'blog': blog,
        'comment': comment,
        'already_liked': already_liked,
    }

    return render(request, 'App_Blog/blog_details.html', context=diction)

@login_required
def like(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog = blog, user = user) # Objects(Likes) with the corressponding user and blog.

    if not already_liked: # If such a like does not exist
        liked_blog = Like(blog = blog, user=user) # Liking it
        liked_blog.save()

        return redirect('App_Blog:blog_details', slug=blog.slug)

@login_required
def unlike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)

    if already_liked: # If such a like exists
        already_liked.delete()

    return redirect('App_Blog:blog_details', slug=blog.slug)

class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blogs.html'

class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'App_Blog/edit_blog.html' 
    fields = ('blog_title', 'blog_content', 'blog_image') 
    context_object_name = 'blog'

    def get_success_url(self, **kwargs): # After everything is done.
        return reverse_lazy('App_Blog:blog_details', kwargs = {'slug': self.object.slug})  # Use ONLY reverse_lazy here







