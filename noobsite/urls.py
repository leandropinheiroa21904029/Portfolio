from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('cmbyn/', views.cmbyn_view),
    path('achilles/', views.achilles_view),
    path('rwrb/', views.rwrb_view),
]