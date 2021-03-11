from blood.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet

# Cryptograph sensitive data to comply with LGPD
key = 'DTNZ1QTKsH3kuhRiyvjNiVB2mo0D74Aw0ivJtiU75qE='

def encrypt(**args):
    # Args
    full_name = str(args.get('full_name')).encode('utf_8')
    email = str(args.get('email')).encode('utf_8')

    f = Fernet(key)
    cipher_args = {}
    cipher_args['full_name'] = f.encrypt(full_name)
    cipher_args['email'] = f.encrypt(email)
    return cipher_args 

def decrypt(**args):
    decipher_args = {}

    try:
        # Args
        full_name = args.get('full_name').encode('utf_8')
        email = args.get('email').encode('utf_8')
        
        f = Fernet(key)
        decipher_args['full_name'] = f.decrypt(full_name).decode('utf_8')
        decipher_args['email'] = f.decrypt(email).decode('utf_8')
    except:
        pass

    return decipher_args 


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = encrypt(full_name = user.full_name).get('full_name').decode('utf_8')
            user.email = encrypt(email = user.email).get('full_name').decode('utf_8')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    return redirect('campaign')


def campaign(request):
    return render(request, 'blood/campaign/campaign.html')


@login_required
def map(request):
    return render(request, 'blood/map/map.html')


@login_required
def profile(request):
    return render(request, 'blood/profile/profile.html')


@login_required
def rewards(request):
    return render(request, 'blood/rewards/rewards.html')