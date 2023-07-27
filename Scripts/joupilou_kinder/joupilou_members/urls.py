from django.urls import path
from . import views

urlpatterns = [
    path('joupilou_members/', views.index, name='index'),
    path('joupilou_members/index', views.index, name='index'),
    path('joupilou_members/about', views.about, name='about'),
    path('joupilou_members/clas', views.clas, name='clas'),
    path('joupilou_members/gallery', views.gallery, name='gallery'),
    path('joupilou_members/team', views.team, name='team'),
    path('joupilou_members/inscrit', views.inscrit, name='inscrit'),
    path('joupilou_members/resultat', views.resultat, name='resultat'),
    path('tri_results', views.vue_resultats, name='vue_resultats'),
    path('joupilou_members/contact', views.contact, name='contact'),
]