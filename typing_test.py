import time
import random
import difflib

from utils import read_file, countdown
from statistics import save_score
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