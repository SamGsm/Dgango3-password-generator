import random
import string
from django.shortcuts import render


def home(request):                              # Create a function that returns a value from the home.html markup file
    return render(request, 'generator/home.html')


def password(request):                     # Create a function that returns a value from the password.html markup file
    thepassword = ''
    characters = list(string.ascii_lowercase)   # Assign lowercase alphabet to variable

    if request.GET.get('uppercase'):            # Return variable from home.html alphabet lowercase + uppercase
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):              # Return variable from home.html lowercase alphabet + special characters
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):              # Return variable from home.html lowercase alphabet + numbers
        characters.extend(list(string.digits))

    length = int(request.GET.get('length'))     # Return variable from home.html value from 'select' block

    for x in range(length):                     # Run a loop adding random characters to a variable for a given length
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):                # Create a function that returns a value from the about.html markup file
    return render(request, 'generator/about.html')
