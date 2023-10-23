from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from decouple import config
import json

# Create your views here.

def index(request):
    return render(request,'index.html')



def profile(request):
    user=request.user

    auth0_user=user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    context={
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }


    return render(request,'profile.html',context)

#logout
# https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}

def logout(request):
    django_logout(request)

    domain=config('AUTH0_DOMAIN')
    client_id=config('AUTH0_CLIENT_ID')
    return_to='http://127.0.0.1:3000/'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")





