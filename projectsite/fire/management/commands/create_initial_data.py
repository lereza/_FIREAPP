from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_locations(30)
        self.create_incidents(30)
        self.create_fire_stations(30)
        self.create_firefighters(30)
        self.create_fire_trucks(30)
        self.create_weather_conditions(30)

    def create_locations(self, count):
        for _ in range(count):
            Locations.objects.create(
                name=fake.city(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for locations created successfully.'))

    def create_incidents(self, count):
        locations = Locations.objects.all()
        for _ in range(count):
            Incident.objects.create(
                location=random.choice(locations),
                date_time=fake.date_time_this_year(),
                severity_level=random.choice(['Minor Fire', 'Moderate Fire', 'Major Fire']),
                description=fake.sentence()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for incidents created successfully.'))

    def create_fire_stations(self, count):
        for _ in range(count):
            FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for fire stations created successfully.'))

    def create_firefighters(self, count):
        fire_stations = FireStation.objects.all()
        for _ in range(count):
            Firefighters.objects.create(
                name=fake.name(),
                rank=random.choice(['Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief']),
                experience_level=random.choice(['Beginner', 'Intermediate', 'Advanced', 'Expert', 'Master']),
                station=random.choice(fire_stations)
            )
            self.stdout.write(self.style.SUCCESS('Initial data for firefighters created successfully.'))

    def create_fire_trucks(self, count):
        fire_stations = FireStation.objects.all()
        for _ in range(count):
            FireTruck.objects.create(
                truck_number=f"Truck-{fake.random_number(digits=4)}",
                model=random.choice(['Pierce Arrow XT', 'E-ONE Cyclone II', 'Rosenbauer Panther', 'Smeal Spartan', 'Seagrave Marauder II', 'KME Predator', 'American LaFrance Eagle', 'Ferrara Inferno', 'Sutphen Monarch', 'HME Ahrens-Fox']),
                capacity=f"{fake.random_int(min=500, max=1500)} gallons",
                station=random.choice(fire_stations)
            )
            self.stdout.write(self.style.SUCCESS('Initial data for fire trucks created successfully.'))

    def create_weather_conditions(self, count):
        fake = Faker()
        incidents = Incident.objects.all()
        for _ in range(count):
            WeatherConditions.objects.create(
                incident=random.choice(incidents),
                temperature=fake.random_int(min=-20, max=50),
                humidity=fake.random_int(min=20, max=80),
                wind_speed=fake.random_int(min=5, max=30),
                weather_description=fake.sentence()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for weather conditions created successfully.'))

