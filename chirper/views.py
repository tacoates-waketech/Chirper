from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Chirp
from .models import Comment
from .forms import ChirpForm

class ChirpListView(ListView):
    model = Chirp
    template_name = "dashboard.html"

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
    
class Home(View):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        chirp_list = Chirp.objects.all()
        return render(request, self.template_name, {'body_class': 'home-body'})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'dashboard')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def create_chirp(request):
    if request.method == 'POST':
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.chirper = request.user  # Assign the logged-in user as the chirper
            chirp.save()
            return redirect('dashboard')  # Redirect to the dashboard 
    else:
        form = ChirpForm()
    return render(request, 'create_chirp.html', {'form': form})

def delete_chirp(request, pk):
    chirp = get_object_or_404(Chirp, pk=pk)
    if request.user == chirp.chirper:
        chirp.delete()
        # Redirect to the dashboard 
        return redirect('dashboard')