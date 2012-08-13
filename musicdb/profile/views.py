from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ProfileForm

def view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.profile)

        if form.is_valid():
            request.profile.save(request)

            messages.success(request, "Your settings were saved successfully.")

            return redirect('profile:view')

    else:
        form = ProfileForm(instance=request.profile)

    return render(request, 'profile/view.html', {
        'form': form,
    })
