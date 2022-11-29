import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from movie.models import Movie


class MovieTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Movie.objects.create(title="Up", duration=123, owner=self.test_user)
        Movie.objects.create(title="It", duration=134, owner=self.test_user)

        movie_test_num = 20
        self.mock_titles = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(movie_test_num)
        ]
        self.mock_durations = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(movie_test_num)
        ]

        for mock_title, mock_duration in zip(self.mock_titles, self.mock_durations):
            Movie.objects.create(title=mock_title, duration=mock_duration, owner=self.test_user)

    def test_duration_model(self):
        """Durations creation are correctly identified"""
        up_movie = Movie.objects.get(title="Up")
        it_movie = Movie.objects.get(title="It")
        self.assertEqual(up_movie.owner.username, "testuser")
        self.assertEqual(it_movie.owner.username, "testuser")
        self.assertEqual(up_movie.duration, 123)
        self.assertEqual(it_movie.duration, 134)

    def test_movie_list(self):
        for mock_title, mock_duration in zip(self.mock_titles, self.mock_durations):
            movie_test = Movie.objects.get(title=mock_title)
            self.assertEqual(movie_test.owner.username, "testuser")
            self.assertEqual(movie_test.duration, mock_duration)