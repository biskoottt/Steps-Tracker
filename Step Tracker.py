#Yusuf Chowdhury MIS310 Individual Assignment 6

def main():

    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    def record_daily_steps():
        step_total = 0
        days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        for day in days:
            steps = int(input(f"Enter steps taken on {day}: "))
            step_total += steps

        return step_total

    def evaluate_weekly_performance(step_total, goal):
        avg_steps = step_total / 7

        print(f"\n--- Weekly Performance Summary ---")
        print(f"Your average daily steps for the week: {avg_steps:.2f}")

        if avg_steps > goal:
            print(f"Great job! You went over your daily steps goal of {goal} steps on average!")
        elif avg_steps == goal:
            print(f"Well done! You met your daily steps goal of {goal} steps on average!")
        else:
            print(f"Keep it up! You almost met your daly steps goal of {goal} steps on average.")
    goal = set_steps_goal()

    step_total = record_daily_steps()
    evaluate_weekly_performance(step_total, goal)

main()