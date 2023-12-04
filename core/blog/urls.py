from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    # path('fbv-index', views.indexView, name="fbv-test"),
    # path('cbv-index', TemplateView.as_view(template_name='index.html', extra_context={'name': "feri"})),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('post/', views.PostList.as_view(), name="post-list"),
    path('go-to-maktabkhooneh', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path('', views.IndexView.as_view(), name='index'),
    path('post/create', views.PostCreateView.as_view(), name='post-create'),

]
