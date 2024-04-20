from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from .models import Chirp
from .models import Comment

class ChirpListView(ListView):
    model = Chirp
    template_name = "home.html"

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = "chirp_detail.html"

class AddCommentView(View):
    def post(self, request, chirp_pk):
        if request.method == 'POST':
            body = request.POST.get('body')
            comment = Comment.objects.create(
                chirp_id=chirp_pk,
                chirper=request.user,
                body=body
            )
        return redirect('chirp_detail', pk=chirp_pk)