from django.shortcuts import render, reverse, redirect
from wishes.models import Profile

from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    template_name = 'home/index.html'
    items = User.objects.all()
    context = {
        'items': items,
    }
    return render(request, template_name, context)


def search(request):
    query = None
    items = User.objects.all()
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            return redirect(reverse('home'))

        queries = Q(name__icontains=query)
        items = users.filter(queries)
    return render(request, 'home/search.html', {'items': items})
