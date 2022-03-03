from os import name
from django.urls import path
from django.urls.conf import include
from apps.vaccinecenter.views import (CoronaVaccineCenterIndex,
                                        AddCoronaVaccineCenter,
                                        UpdateCoronaVaccineCenter,
                                        DeleteCoronaVaccineCenter,
                                        CovidStatusIndex)


urlpatterns = [
    path('list/',CoronaVaccineCenterIndex.as_view(),name='vaccinecenter_index'),
    path('covidlist/',CovidStatusIndex.as_view(),name='covidlist_index'),
    path('create/',AddCoronaVaccineCenter.as_view(),name='create_vaccinecenter'),
    path('<int:pk>/update/',UpdateCoronaVaccineCenter.as_view(),name='update_vaccinecenter'),
    path('<int:pk>/delete_confirm/',DeleteCoronaVaccineCenter.as_view(),name='delete_vaccinecenter'),
    
]
