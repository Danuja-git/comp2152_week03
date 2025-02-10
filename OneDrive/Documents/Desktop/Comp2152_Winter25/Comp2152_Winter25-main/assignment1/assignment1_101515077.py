"""
Author: Danuja Shankar
Assignment: #1
"""

gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True

workout_stats = {
    "Alex": (30, 45, 20),  # (yoga, running, weightlifting)
    "Jamie": (40, 30, 50),
    "Taylor": (25, 60, 35),
    "Tyler": (25, 60, 31),
    "Brain": (25, 60, 30),
    "Susan": (25, 60, 25),
}

# Compute total workout minutes separately
total_minutes_dict = {friend: sum(stats) for friend, stats in workout_stats.items()}

# Add total minutes to workout_stats
for friend, total in total_minutes_dict.items():
    workout_stats[f"{friend}_Total"] = total

# List of only the (yoga, running, weightlifting) tuples
workout_list = [list(stats) for stats in workout_stats.values() if isinstance(stats, tuple)]

# Extract Yoga and Running minutes
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running Minutes:", yoga_running)

# Extract Weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)

# Print active users
for friend, total_minutes in total_minutes_dict.items():
    if total_minutes >= 120:
        print(f"Great job staying active, {friend}!!")

# Get user input
name = input("Enter Friend Name: ")
if name in workout_stats and isinstance(workout_stats[name], tuple):
    print(f"Yoga workout minutes: {workout_stats[name][0]}.")
    print(f"Running workout minutes: {workout_stats[name][1]}.")
    print(f"Weight lifting minutes: {workout_stats[name][2]}.")
    print(f"{name}'s total workout minutes: {total_minutes_dict[name]}.")

else:
    print(f"Friend {name} not found in the records.")

# Find the friend with max and min workout minutes
max_friend = max(total_minutes_dict, key=total_minutes_dict.get)
min_friend = min(total_minutes_dict, key=total_minutes_dict.get)

# Print results
print(f"Friend with the highest total workout minutes: {max_friend} ({total_minutes_dict[max_friend]} minutes).")
print(f"Friend with the lowest total workout minutes: {min_friend} ({total_minutes_dict[min_friend]} minutes).")
