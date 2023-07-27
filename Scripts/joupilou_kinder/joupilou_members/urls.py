from django.urls import path
from . import views

urlpatterns = [
    path('joupilou_members/', views.index, name='index'),
    path('joupilou_members/index', views.index, name='index'),
    path('joupilou_members/about', views.about, name='about'),
    path('joupilou_members/clas', views.clas, name='clas'),
    path('joupilou_members/team', views.team, name='team'),
    path('joupilou_members/inscrit', views.inscrit, name='inscrit'),
    path('joupilou_members/resultat', views.resultat, name='resultat'),
    path('tri_results', views.vue_resultats, name='vue_resultats'),

    path('joupilou_members/contact1', views.contact1, name='contact1'),
    path('joupilou_members/gallery1', views.gallery1, name='gallery1'),
    path('joupilou_members/login', views.user_login, name='user_login'),  # Renommage de l'URL pour éviter le conflit
    path('joupilou_members/login/', views.custom_login, name='custom_login'),   
    path('admin/logout/', views.logout_and_redirect, name='admin_logout'),
]