from django.shortcuts import render

# Create your views here.
def wishes(request):
    """Renders the wishes list page"""
    context = {}
    return render(request, 'wishes/wishes.html', context)