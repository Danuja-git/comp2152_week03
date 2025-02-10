"""
Author: Danuja Shankar
Assignment: #1
"""

# String variable
gym_member = "Alex Alliton"

# Float variable
preferred_weight_kg = 20.5

# Integer variable
highest_reps = 25

# Boolean variable
membership_active = True

# Dictionary with string keys and tuple values
workout_stats = {
    "Alex": (30, 45, 20),  # (yoga, running, weightlifting)
    "Jamie": (40, 30, 50),
    "Taylor": (25, 60, 35)
}

for friend, stats in workout_stats.items():
    total_minutes = sum(stats)
    workout_stats[f"{friend}_Total"] = total_minutes

# 2D list with workout minutes for each friend
workout_list = [list(stats) for stats in workout_stats.values() if isinstance(stats, tuple)]

yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running Minutes:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)

for friend, stats in workout_stats.items():
    if isinstance(stats, int) and stats >= 120:
        print(f"Great job staying active, {friend}!")

        friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    print(f"{friend_name}'s workout minutes: {workout_stats[friend_name]}")
    print(f"Total workout minutes: {workout_stats[f'{friend_name}_Total']}")
else:
    print(f"Friend {friend_name} not found in the records.")

    totals = {friend: total for friend, total in workout_stats.items() if isinstance(total, int)}
max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

print(f"Friend with the highest total workout minutes: {max_friend} ({totals[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend} ({totals[min_friend]} minutes)")