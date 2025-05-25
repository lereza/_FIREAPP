from django.contrib import admin
from django.urls import path

from fire.views import (
    HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, fire_incidents,
    LocationsList, LocationsCreateView, LocationsUpdateView, LocationsDeleteView,
    FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView,
    IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView,
    FirefightersList, FirefightersCreateView, FirefightersUpdateView, FirefightersDeleteView,
    FireTruckList, FireTruckCreateView, FireTruckUpdateView, FireTruckDeleteView,
    WeatherConditionsList, WeatherConditionsCreateView, WeatherConditionsUpdateView, WeatherConditionsDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('dashboard_chart/', ChartView.as_view(), name='dashboard-chart'),
    path('pieChart/', PieCountbySeverity, name='pie-chart'),
    path('lineChart/', LineCountbyMonth, name='line-chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='multiline-chart'),
    path('multiBarChart/', multipleBarbySeverity, name='multi-bar-chart'),
    path('stations/', map_station, name='map-station'),
    path('incidents_map/', fire_incidents, name='fire-incidents'),

    path('locations/', LocationsList.as_view(), name='locations-list'),
    path('locations/add/', LocationsCreateView.as_view(), name='locations-add'),
    path('locations/<pk>/', LocationsUpdateView.as_view(), name='locations-update'),
    path('locations/<pk>/delete/', LocationsDeleteView.as_view(), name='locations-delete'),

    path('incidents/', IncidentList.as_view(), name='incident-list'),
    path('incidents/add/', IncidentCreateView.as_view(), name='incident-add'),
    path('incidents/<pk>/', IncidentUpdateView.as_view(), name='incident-update'),
    path('incidents/<pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),

    path('firestations/', FireStationList.as_view(), name='firestation-list'),
    path('firestations/add/', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestations/<pk>/', FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestations/<pk>/delete/', FireStationDeleteView.as_view(), name='firestation-delete'),

    path('firefighters/', FirefightersList.as_view(), name='firefighters-list'),
    path('firefighters/add/', FirefightersCreateView.as_view(), name='firefighters-add'),
    path('firefighters/<pk>/', FirefightersUpdateView.as_view(), name='firefighters-update'),
    path('firefighters/<pk>/delete/', FirefightersDeleteView.as_view(), name='firefighters-delete'),

    path('firetrucks/', FireTruckList.as_view(), name='firetruck-list'),
    path('firetrucks/add/', FireTruckCreateView.as_view(), name='firetruck-add'),
    path('firetrucks/<pk>/', FireTruckUpdateView.as_view(), name='firetruck-update'),
    path('firetrucks/<pk>/delete/', FireTruckDeleteView.as_view(), name='firetruck-delete'),

    path('weather/', WeatherConditionsList.as_view(), name='weather-list'),
    path('weather/add/', WeatherConditionsCreateView.as_view(), name='weather-add'),
    path('weather/<pk>/', WeatherConditionsUpdateView.as_view(), name='weather-update'),
    path('weather/<pk>/delete/', WeatherConditionsDeleteView.as_view(), name='weather-delete'),
]
