class User:
    """
    Класс для представления пользователя.
    
    Attributes:
        name (str): Имя пользователя.
        workouts (list): Список тренировок.
    """

    def __init__(self, name):
        """
        Инициализация нового пользователя.
        
        Args:
            name (str): Имя пользователя.
        """
        self.name = name
        self.workouts = []

    def add_workout(self, workout):
        """
        Добавляет тренировку в список тренировок.
        
        Args:
            workout (Workout): Тренировка для добавления.
        """
        self.workouts.append(workout)

    def get_progress(self):
        """Возвращает статистику прогресса пользователя."""
        total_calories = sum(workout.calories for workout in self.workouts)
        return total_calories