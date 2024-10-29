import unittest
from src.tracker import Workout
from src.user import User

class TestWorkout(unittest.TestCase):

    def test_workout_initialization(self):
        workout = Workout("Бег", 30, 300)
        self.assertEqual(workout.workout_type, "Бег")
        self.assertEqual(workout.duration, 30)
        self.assertEqual(workout.calories, 300)

    def test_workout_string_representation(self):
        workout = Workout("Плавание", 45, 400)
        self.assertEqual(str(workout), "Плавание - 45 мин, 400 калорий")

class TestUser(unittest.TestCase):

    def test_user_initialization(self):
        user = User("Мария")
        self.assertEqual(user.name, "Мария")
        self.assertEqual(user.workouts, [])

    def test_add_workout(self):
        user = User("Мария")
        workout = Workout("Силовая тренировка", 60, 500)
        user.add_workout(workout)
        self.assertIn(workout, user.workouts)

    def test_get_progress(self):
        user = User("Мария")
        workout1 = Workout("Бег", 30, 300)
        workout2 = Workout("Плавание", 45, 400)
        user.add_workout(workout1)
        user.add_workout(workout2)
        self.assertEqual(user.get_progress(), 700)

if __name__ == '__main__':
    unittest.main()