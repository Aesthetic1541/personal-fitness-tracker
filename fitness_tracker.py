import csv
import os
from datetime import datetime

class FitnessTracker:
    def __init__(self, filename='workouts.csv'):
        self.filename = filename
        self.workouts = []
        self.load_workouts()

    def load_workouts(self):
        """Load workouts from a CSV file."""
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    date, exercise, duration, calories = row
                    self.workouts.append({
                        'date': date,
                        'exercise': exercise,
                        'duration': float(duration),
                        'calories': float(calories)
                    })

    def save_workouts(self):
        """Save workouts to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for workout in self.workouts:
                writer.writerow([workout['date'], workout['exercise'], workout['duration'], workout['calories']])

    def add_workout(self, exercise, duration, calories):
        """Add a new workout."""
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.workouts.append({
            'date': date,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        })
        self.save_workouts()
        print(f"Workout added: {exercise}, Duration: {duration} mins, Calories: {calories}")

    def view_workouts(self):
        """View all logged workouts."""
        if not self.workouts:
            print("No workouts logged yet.")
            return
        print("Date\t\t\tExercise\tDuration (mins)\tCalories")
        print("-" * 60)
        for workout in self.workouts:
            print(f"{workout['date']}\t{workout['exercise']}\t{workout['duration']}\t{workout['calories']}")

def main():
    tracker = FitnessTracker()

    while True:
        print("\nPersonal Fitness Tracker")
        print("1. Add Workout")
        print("2. View Workouts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            exercise = input("Enter exercise name: ")
            duration = float(input("Enter duration in minutes: "))
            calories = float(input("Enter calories burned: "))
            tracker.add_workout(exercise, duration, calories)
        elif choice == '2':
            tracker.view_workouts()
        elif choice == '3':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()