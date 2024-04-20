from django.urls import path
from .views import ChirpListView, ChirpDetailView, AddCommentView

urlpatterns = [
    path("post/<int:pk>/", ChirpDetailView.as_view(), name="chirp_detail"),
    path("", ChirpListView.as_view(), name="home"),
    path('add_comment/<int:chirp_pk>/', AddCommentView.as_view(), name='add_comment'),

]