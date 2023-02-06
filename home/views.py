from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from wishes.models import Profile


# Create your views here.
def home(request):
    template_name = 'home/index.html'

    context = {

    }
    return render(request, template_name, context)


def search(request):
    query = request.GET.get('q')
    profiles = Profile.objects.none()
    if query:
        queries = query.split()
        for q in queries:
            profiles |= Profile.objects.filter(
                Q(user__username__icontains=q) |
                Q(street_address1__icontains=q) |
                Q(street_address2__icontains=q) |
                Q(town_or_city__icontains=q) |
                Q(county__icontains=q) |
                Q(postcode__icontains=q) |
                Q(country__icontains=q)
            )
    return render(request, 'home/search.html', {'profiles': profiles})