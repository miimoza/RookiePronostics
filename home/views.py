from django.shortcuts import render
import youtube_api


# Create your views here.

def home(request):
    print("Subscriber count So la lune: ", youtube_api.get_subscriber_count("UCTGKo4bqLYXjB78f9VCzGNg"))
    return render(request, 'index.html', {})



# views.py
from .forms import LoginForm


def home(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            print("putain c tellement valide")
    else:
        login_form = LoginForm()
    return render(request, 'index.html', {'login_form': login_form})