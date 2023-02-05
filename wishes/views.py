from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WishForm
from .models import Item


# Create your views here.
@login_required
def wishes(request):
    """Renders the profile page"""
    user = request.user
    wishlist = Item.objects.filter(user=user)

    if request.method == 'POST':
        wish_form = WishForm(request.POST, request.FILES)
        if wish_form.is_valid():
            form = wish_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse('wishes'))
        else:
            messages.error(request, 'Error adding the product. \
                Verify that all fields are filled in accurately.')
    else:
        wish_form = WishForm()

    template_name = 'wishes/wishes.html'
    context = {
        'wishlist': wishlist,
        'wish_form': wish_form,
    }
    return render(request, template_name, context)


@login_required
def edit_wish(request, item_id):
    """ Render the Edit_wish template"""

    wish = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        wish_form = WishForm(request.POST, request.FILES, instance=wish)
        if wish_form.is_valid():
            wish_form.save()
            return redirect(reverse('wishes'))
    else:
        wish_form = WishForm(instance=wish)

    template_name = 'wishes/edit_wishes.html'
    context = {
        'wish_form': wish_form,
        'wish': wish,
    }
    return render(request, template_name, context)


@login_required
def delete_wish(request, item_id):
    """This function deletes a selected wish"""
    wish = get_object_or_404(Item, pk=item_id)
    wish.delete()
    return redirect('wishes')