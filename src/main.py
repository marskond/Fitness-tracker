import tkinter as tk
from tkinter import messagebox
from src.user import User
from src.tracker import Workout

class FitnessTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness Tracker")
        
        self.user = None
        
        # Ввод имени пользователя
        self.label_name = tk.Label(master, text="Введите ваше имя:")
        self.label_name.pack()
        
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        
        self.button_start = tk.Button(master, text="Начать", command=self.start)
        self.button_start.pack()

    def start(self):
        user_name = self.entry_name.get()
        self.user = User(user_name)
        self.entry_name.config(state='disabled')
        self.button_start.config(state='disabled')
        
        self.create_workout_interface()

    def create_workout_interface(self):
        self.label_action = tk.Label(self.master, text="Выберите действие:")
        self.label_action.pack()

        self.button_add_workout = tk.Button(self.master, text="Добавить тренировку", command=self.add_workout)
        self.button_add_workout.pack()

        self.button_show_progress = tk.Button(self.master, text="Показать статистику", command=self.show_progress)
        self.button_show_progress.pack()

        self.button_exit = tk.Button(self.master, text="Выйти", command=self.master.quit)
        self.button_exit.pack()

    def add_workout(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Добавить тренировку")

        tk.Label(add_window, text="Тип тренировки:").pack()
        workout_type_entry = tk.Entry(add_window)
        workout_type_entry.pack()

        tk.Label(add_window, text="Длительность (мин):").pack()
        duration_entry = tk.Entry(add_window)
        duration_entry.pack()

        tk.Label(add_window, text="Сожженные калории:").pack()
        calories_entry = tk.Entry(add_window)
        calories_entry.pack()

        tk.Button(add_window, text="Добавить", command=lambda: self.save_workout(workout_type_entry.get(), duration_entry.get(), calories_entry.get(), add_window)).pack()

    def save_workout(self, workout_type, duration, calories, window):
        try:
            duration = int(duration)
            calories = int(calories)
            workout = Workout(workout_type, duration, calories)
            self.user.add_workout(workout)
            messagebox.showinfo("Успех", "Тренировка добавлена!")
            window.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные данные.")

    def show_progress(self):
        total_calories = self.user.get_progress()
        messagebox.showinfo("Статистика", f"Общее количество сожженных калорий: {total_calories}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()