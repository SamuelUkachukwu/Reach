from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages
from wishes.models import Profile, Item
from .forms import ProfileForm


# Create your views here.
@login_required
def profile(request):
    """Renders the friends list page"""
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request):
    """Renders the edit profile page"""

    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
        )
    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit_profile.html', context)


@login_required
def follow(request, username):
    user = request.user
    follow_user = get_object_or_404(User, username=username)
    if user == follow_user:
        messages.error(request, "You can't follow yourself.")
        return redirect("profile", username=username)
    user_profile, created = Profile.objects.get_or_create(user=user)
    if not created:
        if follow_user in user_profile.followers.all():
            messages.error(request, "You are already following this user.")
            return redirect("profile", username=username)
    user_profile.followers.add(follow_user)
    messages.success(request, "You are now following {}".format(username))
    return redirect("profile", username=username)


@login_required
def unfollow(request, username):
    user = request.user
    unfollow_user = get_object_or_404(User, username=username)
    if user == unfollow_user:
        messages.error(request, "You can't unfollow yourself.")
        return redirect("profile", username=username)
    user_profile, created = Profile.objects.get_or_create(user=user)
    if not created:
        if unfollow_user not in user_profile.followers.all():
            messages.error(request, "You are not following this user.")
            return redirect("profile", username=username)
    user_profile.followers.remove(unfollow_user)
    messages.success(request, "You have unfollowed {}".format(username))
    return redirect("profile", username=username)


def follower_items(request, follower_id):
    profile = request.user.profile
    follower = User.objects.get(id=follower_id)
    if follower in profile.followers.all():
        follower_items = Item.objects.filter(user=follower)
        context = {
            'follower_items': follower_items,
            'follower': follower,
        }
        return render(request, 'profiles/follower_items.html', context)
    else:
        return redirect('followers_items')