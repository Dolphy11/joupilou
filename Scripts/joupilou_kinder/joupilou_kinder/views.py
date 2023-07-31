from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from typing import Any

# create a custom logout view

class CustLogoutView(LogoutView):
    def dispatch(self, request, *args:Any, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('index'))
     