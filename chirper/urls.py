from django.urls import path
from .views import ChirpListView, ChirpDetailView, AddCommentView, Home, user_login, register, user_logout, create_chirp, delete_chirp, update_chirp

urlpatterns = [
    path("post/<int:pk>/", ChirpDetailView.as_view(), name="chirp_detail"),
    path("dashboard/", ChirpListView.as_view(), name="dashboard"),
    path('add_comment/<int:chirp_pk>/', AddCommentView.as_view(), name='add_comment'),
    path("", Home.as_view(), name="home"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_chirp/', create_chirp, name='create_chirp'),
    path('delete_chirp/<int:pk>/', delete_chirp, name='delete_chirp'),
    path('update_chirp/<int:pk>/', update_chirp, name='update_chirp'),

]