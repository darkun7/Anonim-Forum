from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('thread/', views.post, name="post"),
    path('thread/create/', views.createPost, name="createpost"),
    path('thread/show/<str:id>', views.showPost, name="showpost"),
    path('thread/edit/<str:id>', views.editPost, name="editpost"),
    path('thread/delete/<str:id>', views.deletePost, name="deletepost"),

    path('komentar/create/<str:thread_id>', views.createKomentar, name="createkomentar"),
    path('komentar/edit/<str:thread_id>/<str:id>', views.editKomentar, name="editkomentar"),
    path('komentar/delete/<str:thread_id>/<str:id>', views.deleteKomentar, name="deletekomentar"),

    path('author/<str:penulis>', views.authorThreads, name="author") 
]
