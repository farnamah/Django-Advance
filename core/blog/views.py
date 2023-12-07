from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, CreateView, UpdateView
from .forms import PostForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

'''
# function base view show a template
 def indexView(request):
     name = "feri"
     context = {"name": name}
     return render(request, "index.html", context)
'''


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'feri'
        context['posts'] = Post.objects.all()
        return context


'''
FBV for redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')
'''


class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    # model = Post
    content_object_name = 'posts'

    def get_queryset(self):
        posts = Post.object.filter(status=True)
        return posts


"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


@api_view()
def api_post_list_view(request):
    return Response("OK")
