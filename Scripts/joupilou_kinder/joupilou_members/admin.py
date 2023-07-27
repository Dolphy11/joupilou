from django.contrib import admin
from .models import *
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom','gender','parent_name',
                    'phone_parent','email_parent','address','date_birth',
                    'classes','created_at','updated_at') 

class NoteAdmin(admin.ModelAdmin):
    list_display = ('children', 'classes', 'Dessin', 'Ecriture', 'Chant', 'Cumule')
    list_filter = ('classes',)
    search_fields = ('children__nom', 'children__prenom')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "children":
            kwargs["queryset"] = Children.objects.annotate(num_notes=models.Count('note')).filter(num_notes__lt=1)
            return super().formfield_for_foreignkey(db_field, request,**kwargs)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['nom_prenom', 'email', 'objet']
    search_fields = ['nom_prenom', 'email', 'objet']

admin.site.register(Children,ChildrenAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Message, MessageAdmin)