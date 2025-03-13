from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile) #To pupolated with the profil info
    orders = profile.orders.all() #To get the orders

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }
    
    return render(request, template, context)