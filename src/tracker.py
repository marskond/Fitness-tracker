class Workout:
    """
    Класс для представления тренировки.
    
    Attributes:
        workout_type (str): Тип тренировки.
        duration (int): Длительность тренировки в минутах.
        calories (int): Сожженные калории.
    """

    def __init__(self, workout_type, duration, calories):
        """
        Инициализация новой тренировки.
        
        Args:
            workout_type (str): Тип тренировки.
            duration (int): Длительность тренировки в минутах.
            calories (int): Сожженные калории.
        """
        self.workout_type = workout_type
        self.duration = duration
        self.calories = calories

    def __str__(self):
        """Возвращает строковое представление тренировки."""
        return f"{self.workout_type} - {self.duration} мин, {self.calories} калорий"