from registration.backends.simple.views import RegistrationView
from django.shortcuts import render, redirect

# my new registration view, subclassing RegistrationView
# from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request):
        # the named URL that we want to redirect to after
        # successful registration
        return '/'