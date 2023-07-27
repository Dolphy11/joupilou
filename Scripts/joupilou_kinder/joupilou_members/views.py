from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .models import Message
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login


def index(request):
    template = loader.get_template('views/index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('views/about.html')
    return HttpResponse(template.render())

# def contact(request):
#     template = loader.get_template('views/contact.html')
#     return HttpResponse(template.render())

def clas(request):
    template = loader.get_template('views/clas.html')
    return HttpResponse(template.render())

def gallery1(request):
    template = loader.get_template('views/gallery.html')
    return HttpResponse(template.render())

def team(request):
    template = loader.get_template('views/team.html')
    return HttpResponse(template.render())

def inscrit(request):
    all_child = Children.objects.all()
    template = loader.get_template('views/inscrit.html')
    context = {
        'all_child': all_child,
    }
    return HttpResponse(template.render(context, request))

def resultat(request):
    all_note = Note.objects.all()
    template = loader.get_template('views/resultat.html')
    for note in all_note:
        if note.Cumule >= 6:
            note.mention = "Accepter"
        else:
            note.mention = "Refuser"
    context = {
        'all_note': all_note,
    }
    return HttpResponse(template.render(context, request))


def vue_resultats(request):
    selection = request.GET.get('radio', 'all')
    if selection == 'Accepter':
        all_note = Note.objects.filter(Cumule__gte=6)  # Supposons que 'Cumule' est le champ pour la moyenne
    elif selection == 'Refuser':
        all_note = Note.objects.filter(Cumule__lt=6)
    else:
        all_note = Note.objects.all()  # Sélection "Tous"

    for note in all_note:
        if note.Cumule >= 6:
            note.mention = "Accepter"
        else:
            note.mention = "Refuser"
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'views/tri_result.html', {'all_note': all_note})
    
    return render(request, 'views/resultat.html', {'all_note': all_note})

def contact1(request):
    if request.method == 'POST':
        nom_prenom = request.POST.get('name')
        email = request.POST.get('email')
        objet = request.POST.get('subject')
        message = request.POST.get('message')

        message_obj = Message(nom_prenom=nom_prenom, email=email, objet=objet, message=message)
        message_obj.save()

        messages.success(request, 'Message soumis avec succès et stocké dans la base de données !')
        return redirect('contact1')

    return render(request, 'views/contact1.html')














def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Utilisation de la fonction auth_login
            return redirect('/admin/')  # Redirection vers le portail d'administration
        else:
            # Gérer le cas d'identification invalide ici (par exemple, afficher un message d'erreur)
            pass

    return render(request, 'views/login.html')

def logout_and_redirect(request):
    logout(request)  # Utilisez correctement la fonction logout
    return redirect('custom_login')

def custom_login(request):
    return render(request, 'views/login.html')
