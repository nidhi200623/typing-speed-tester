import time
import random
import os



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
    print(f"Correct characters: {correct_chars}")
    print(f"Wrong characters: {wrong_chars}")
    return typing_speed



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
    correct_chars = sum(1 for t, u in zip(test_sentence, user_input) if t == u)
    wrong_chars = sum(1 for t, u in zip(test_sentence, user_input) if t != u)
    total_chars = len(test_sentence)
    return (correct_chars / total_chars) * 100, correct_chars, wrong_chars
 
highest_wpm = 0
play_again = "y"

while play_again == "y":

    current_wpm = typing_test()

    if current_wpm > highest_wpm:
        highest_wpm = current_wpm

    play_again = input("\nDo you want to play again? (y/n): ").lower()

print(f"\nHighest WPM: {highest_wpm:.2f}")
print("Thanks for playing!")