from django.urls import path
from . import views
urlpatterns = [
    path(' ',views.home, name='home'),
    path('blog/categories/',views.categories,name="categories"),
    path('blog/articles/',views.articles, name="articles" ),
]