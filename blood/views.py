from django.shortcuts import render

def home(request):
    return render(request, 'blood/home/home.html')

def map(request):
    return render(request, 'blood/map/map.html')

def profile(request):
    return render(request, 'blood/profile/profile.html')

def rewards(request):
    return render(request, 'blood/rewards/rewards.html')