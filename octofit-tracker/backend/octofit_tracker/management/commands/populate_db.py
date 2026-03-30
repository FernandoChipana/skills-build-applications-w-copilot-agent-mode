from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='medium'),
            Workout.objects.create(name='Swimming', description='Swim 1km', difficulty='hard'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='run', duration=25, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
