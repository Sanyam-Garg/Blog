from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.blog_list, name = 'blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name = 'create_blog'),
    path('blog-details/<slug:slug>/', views.blog_details, name = 'blog_details'),
    path('like/<pk>', views.like, name = 'like'),
    path('unlike/<pk>', views.unlike, name = 'unlike'),
    path('my-blogs/', views.MyBlogs.as_view(), name = 'my_blogs'),
    path('edit-blog/<pk>', views.EditBlog.as_view(), name = 'edit_blog')
]
