from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conference, Registration
from .forms import ReviewForm
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.urls import reverse

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})


def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    reviews = conference.review_set.all()
    user_registration = None
    if request.user.is_authenticated:
        user_registration = Registration.objects.filter(user=request.user, conference=conference).first()

    context = {
        'conference': conference,
        'reviews': reviews,
        'registration': user_registration
    }
    return render(request, 'conference_detail.html', context)


@login_required
def register_for_conference(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.conference = conference
            registration.save()
            return redirect('conference_detail', conference_id=conference.id)
    else:
        form = RegistrationForm()
    return render(request, 'register_for_conference.html', {'form': form, 'conference': conference})


@login_required
def add_review(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.conference = conference
            review.save()
            return redirect('conference_detail', conference_id=conference.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'conference': conference})


def participant_list(request):
    registrations = Registration.objects.select_related('conference', 'user').all()
    return render(request, 'participant_list.html', {'registrations': registrations})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successful!')
            return redirect('success_page')
        else:
            messages.error(request, 'You have already registered.')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_registration(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    registration = get_object_or_404(Registration, user=request.user, conference=conference)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('conference_detail', conference_id=conference.id)
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'edit_registration.html', {'form': form, 'conference': conference})


@login_required
def delete_registration(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    registration = get_object_or_404(Registration, user=request.user, conference=conference)
    registration.delete()
    return redirect('conference_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('conference_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})

def home(request):
    return render(request, 'home.html')

@login_required
def edit_registration(request, conference_id):
    registration = get_object_or_404(Registration, conference_id=conference_id, user=request.user)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect(reverse('conference_detail', args=[conference_id]))
    else:
        form = RegistrationForm(instance=registration)

    return render(request, 'edit_registration.html', {'form': form, 'conference': registration.conference})

@login_required
def delete_registration(request, conference_id):
    registration = get_object_or_404(Registration, conference_id=conference_id, user=request.user)

    if request.method == 'POST':
        registration.delete()
        return redirect(reverse('conference_list'))

    return render(request, 'delete_registration.html', {'conference': registration.conference})