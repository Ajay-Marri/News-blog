from django.shortcuts import render,get_object_or_404
from .models import post
from django.views.generic import ListView,DetailView
from .form import commetform

class dashboard(ListView):
    template_name="blog/index.html"
    model=post
    ordering=["-date"]
    context_object_name="port"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data

class posts(ListView):
    template_name="blog/all-posts.html"
    model=post
    ordering=["-date"]
    context_object_name="recent_post"

class post_details(DetailView):
    template_name="blog/mainpost.html"
    model=post

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["post_tag"]=self.object.tag.all()
        context["comment_form"]=commetform()
        return context






# def dashboard(request):
#     lastest_post=post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{
#         "port":lastest_post
#     })

# def posts(request):
#     recent_posts=post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/all-posts.html",{
#         "recent_post":recent_posts
#     })

# def post_details(request, slug):
#     identified_post = get_object_or_404(post, slug=slug)
#     return render(request, "blog/mainpost.html", {
#         "post": identified_post,
#         "post_tag":identified_post.tag.all()
#     })