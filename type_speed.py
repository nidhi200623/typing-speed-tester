import time
import random
import os
import csv
import difflib

def typing_test():
    sentences = read_file("sentences.txt")
    test_sentence = random.choice(sentences).strip()
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    countdown()
    start_time = time.time()
    user_input = input("\nStart typing here: ")
    end_time = time.time()
    time_taken = end_time - start_time
    words_count = len(user_input.split())
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_count}")
    typing_speed = (words_count / time_taken) * 60
    print(f"Typing speed: {typing_speed:.2f} words per minute")
    accuracy_score, correct_chars, wrong_chars = accuracy(test_sentence, user_input)
    print(f"Accuracy: {accuracy_score:.2f}%")
    print(f"Correct words: {correct_chars}")
    print(f"Wrong words: {wrong_chars}")
    save_score(typing_speed, accuracy_score, correct_chars, wrong_chars, time_taken)
    return typing_speed

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

def read_file(file_name):
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, file_name)

    with open(file_path, "r") as file:
        sentences = file.readlines()

    return sentences


def countdown():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!\n")



def accuracy(test_sentence, user_input):

    matcher = difflib.SequenceMatcher(None, test_sentence, user_input)

    accuracy_score = matcher.ratio() * 100

    original_words = test_sentence.split()
    typed_words = user_input.split()

    correct_words = sum(
        1 for original, typed in zip(original_words, typed_words)
        if original == typed
    )

    wrong_words = max(len(original_words), len(typed_words)) - correct_words

    return accuracy_score, correct_words, wrong_words
def save_score(wpm, accuracy, correct_words, wrong_words, time_taken):

    file_name = "scores.csv"

    # Check if file exists
    file_exists = os.path.isfile(file_name)

    # Check if file is empty
    file_empty = (not file_exists) or (os.path.getsize(file_name) == 0)

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        # Write header if file doesn't exist OR is empty
        if file_empty:
            writer.writerow(["WPM", "Accuracy", "Correct", "Wrong", "Time"])

        writer.writerow([
            round(wpm, 2),
            round(accuracy, 2),
            correct_words,
            wrong_words,
            round(time_taken, 2)
        ])
highest_wpm = 0
play_again = "y"

while play_again == "y":

    current_wpm = typing_test()

    if current_wpm > highest_wpm:
        highest_wpm = current_wpm

    play_again = input("\nDo you want to play again? (y/n): ").lower()

show_statistics()
print("\nThanks for playing!")