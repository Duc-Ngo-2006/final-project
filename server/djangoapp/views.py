from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcut import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create an `about` view to render the About page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'static/About.html', context)

# Create a `contact` view to render the Contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'static/Contact.html', context)