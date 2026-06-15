import csv
import os


def save_score(wpm, accuracy, correct_words, wrong_words, time_taken):
    file_name = "scores.csv"

    file_exists = os.path.isfile(file_name)
    file_empty = (not file_exists) or (os.path.getsize(file_name) == 0)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        if file_empty:
            writer.writerow(["WPM", "Accuracy", "Correct", "Wrong", "Time"])

        writer.writerow([
            round(wpm, 2),
            round(accuracy, 2),
            correct_words,
            wrong_words,
            round(time_taken, 2)
        ])


def show_statistics():
    if not os.path.isfile("scores.csv"):
        print("\nNo statistics available.")
        return

    with open("scores.csv", "r") as file:
        reader = csv.DictReader(file)

        total_games = 0
        total_wpm = 0
        highest_wpm = 0
        best_accuracy = 0

        for row in reader:
            total_games += 1

            wpm = float(row["WPM"])
            accuracy = float(row["Accuracy"])

            total_wpm += wpm
            highest_wpm = max(highest_wpm, wpm)
            best_accuracy = max(best_accuracy, accuracy)

    if total_games == 0:
        print("\nNo statistics available.")
        return

    average_wpm = total_wpm / total_games

    print("\n========== Statistics ==========")
    print(f"Games Played : {total_games}")
    print(f"Highest WPM  : {highest_wpm:.2f}")
    print(f"Average WPM  : {average_wpm:.2f}")
    print(f"Best Accuracy: {best_accuracy:.2f}%")
    print("================================")