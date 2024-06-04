import datetime

class ProductivityTracker:
    def __init__(self):
        self.activities = {
            "Study": [0] * 7,
            "Read": [0] * 7,
            "Write": [0] * 7,
            "Meditate": [0] * 7,
            "Programming": [0] * 7,
            "Career": [0] * 7,
            "Exercise": [0] * 7,
            "Eye exercise": [0] * 7
        }
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.today_index = datetime.datetime.now().weekday()

    def mark_activity(self, activity, day):
        if activity in self.activities and 0 <= day < 7:
            self.activities[activity][day] = 1
        else:
            print("Invalid activity or day")

    def display_progress(self):
        print("Productivity Tracker: ")
        print("{:<15}".format("Task"), end="")
        for day in self.days:
            print("{:<15}".format(day), end="")
        print()

        for activity, progress in self.activities.items():
            print("{:<15}".format(activity), end="")
            for status in progress:
                print("{:<10}".format("W" if status else "X"), end="")
            print()

if __name__== "__main__":
    tracker = ProductivityTracker()

    while True:
        print("\n1. Mark activity")
        print("2. Display progress")
        print("3. Quit")

        choice = input("Chose an option: ")

        if choice == "1":
            activity = input("Enter activity name: ")
            day = int(input(f"Enter day(0 for Sunday, 6 for Saturday): "))
            tracker.mark_activity(activity, day)
        elif choice == "2":
            tracker.display_progress()
        elif choice == "3":
            break
        else:
            print("Invalid chice. Please try again.")
