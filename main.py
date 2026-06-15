from typing_test import typing_test
from statistics import show_statistics


highest_wpm = 0
play_again = "y"

while play_again == "y":
    current_wpm = typing_test()

    highest_wpm = max(highest_wpm, current_wpm)

    play_again = input("\nDo you want to play again? (y/n): ").lower()

show_statistics()

print("\nThanks for playing!")