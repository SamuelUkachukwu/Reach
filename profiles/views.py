from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def friends(request):
    """Renders the friends list page"""
    context = {}
    return render(request, 'profiles/friends.html', context)