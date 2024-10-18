from django.shortcuts import render
from .forms.forms import ShortURLForm

def index(request):
    short_url = None
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short_url_object = form.save()
            short_url = request.build_absolute_uri('/') + short_url_object.short_url
    else:
        form = ShortURLForm()
    
    return render(request, 'shortener/index.html', {'form': form, 'short_url': short_url})