import customtkinter as ctk
import random
import time
import difflib

from utils import countdown, read_file
from statistics import save_score
from typing_test import accuracy
from tkinter import messagebox
from statistics import show_statistics

sentences = read_file("sentences.txt")
def load_highest_wpm():
    import csv
    import os

    if not os.path.isfile("scores.csv"):
        return 0

    highest = 0

    with open("scores.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                wpm = float(row["WPM"])
                highest = max(highest, wpm)
            except:
                pass

    return highest
current_sentence = ""
start_time = 0
highest_wpm = load_highest_wpm()

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create window
app = ctk.CTk()
app.title("Typing Speed Tester Pro")
app.geometry("800x650")

# Title Label
title = ctk.CTkLabel(
    app,
    text="🚀 Typing Speed Tester Pro",
    font=("Arial", 28, "bold")
)
#Title pack
title.pack(pady=20)
sentence_label = ctk.CTkLabel(
    app,
    text="Press Start to begin the test!",
    font=("Arial", 18),
    wraplength=700
)

sentence_label.pack(pady=20)
#Typing box
typing_box = ctk.CTkTextbox(
    app,
    width=700,
    height=100,
    font=("Arial", 18)
)
countdown_label = ctk.CTkLabel(app, text="", font=("Arial", 22, "bold"))
countdown_label.pack(pady=5)

typing_box.pack(pady=20)

#Add Statistics Labels
wpm_label = ctk.CTkLabel(
    app,
    text="⚡ WPM: 0",
    font=("Arial", 18)
)

wpm_label.pack(pady=5)


accuracy_label = ctk.CTkLabel(
    app,
    text="🎯 Accuracy: 0%",
    font=("Arial", 18)
)

accuracy_label.pack(pady=5)


highest_label = ctk.CTkLabel(
    app,
    text=f"🏆 Highest WPM: {highest_wpm:.2f}",
    font=("Arial", 18)
)
highest_label.pack(pady=5)


sentences = read_file("sentences.txt")

current_sentence = ""
start_time = 0

def start_test():
    global current_sentence

    current_sentence = random.choice(sentences).strip()

    sentence_label.configure(text="Get ready...")
    typing_box.delete("1.0", "end")
    typing_box.configure(state="disabled")

    countdown(3)


def countdown(count):
    global start_time

    if count > 0:
        countdown_label.configure(text=str(count))
        app.after(1000, countdown, count - 1)
    else:
        countdown_label.configure(text="Go!")

        sentence_label.configure(text=current_sentence)
        typing_box.configure(state="normal")
        typing_box.focus()

        start_time = time.time()

        app.after(1000, lambda: countdown_label.configure(text=""))
def view_statistics():
    import csv
    import os

    if not os.path.isfile("scores.csv"):
        messagebox.showinfo("Statistics", "No statistics available yet.")
        return

    total_games = 0
    total_wpm = 0
    highest_wpm_value = 0
    best_accuracy = 0

    with open("scores.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_games += 1

            wpm = float(row["WPM"])
            accuracy_value = float(row["Accuracy"])

            total_wpm += wpm
            highest_wpm_value = max(highest_wpm_value, wpm)
            best_accuracy = max(best_accuracy, accuracy_value)

    if total_games == 0:
        messagebox.showinfo("Statistics", "No statistics available yet.")
        return

    average_wpm = total_wpm / total_games

    messagebox.showinfo(
        "Typing Statistics",
        f"Games Played: {total_games}\n"
        f"Highest WPM: {highest_wpm_value:.2f}\n"
        f"Average WPM: {average_wpm:.2f}\n"
        f"Best Accuracy: {best_accuracy:.2f}%"
    )
#Adding buttons
button_frame = ctk.CTkFrame(app)


def submit_test():
    global highest_wpm

    end_time = time.time()

    user_input = typing_box.get("1.0", "end").strip()

    time_taken = end_time - start_time

    words_count = len(user_input.split())

    if time_taken == 0:
        return

    wpm = (words_count / time_taken) * 60

    accuracy_score, correct_words, wrong_words = accuracy(
        current_sentence,
        user_input
    )

    highest_wpm = max(highest_wpm, wpm)

    wpm_label.configure(
        text=f"⚡ WPM: {wpm:.2f}"
    )

    accuracy_label.configure(
        text=f"🎯 Accuracy: {accuracy_score:.2f}%"
    )

    highest_label.configure(
        text=f"🏆 Highest WPM: {highest_wpm:.2f}"
    )

    save_score(
        wpm,
        accuracy_score,
        correct_words,
        wrong_words,
        time_taken
    )
    messagebox.showinfo(
    "Test Completed",
    f"WPM: {wpm:.2f}\nAccuracy: {accuracy_score:.2f}%\nHighest WPM: {highest_wpm:.2f}"
    
)
    typing_box.delete("1.0", "end")
typing_box.configure(state="disabled")
sentence_label.configure(text="Press Start to begin the next test!")
countdown_label.configure(text="")

button_frame.pack(pady=20)


start_button = ctk.CTkButton(
    button_frame,
    text="Start Test",
    command=start_test
)
start_button.pack(side="left", padx=10)

submit_button = ctk.CTkButton(
    button_frame,
    text="Submit",
    command=submit_test
)

submit_button.pack(side="left", padx=10)

stats_button = ctk.CTkButton(
    button_frame,
    text="View Statistics",
    command=view_statistics
)

stats_button.pack(side="left", padx=10)

exit_button = ctk.CTkButton(
    button_frame,
    text="Exit",
    command=app.destroy
)

exit_button.pack(side="left", padx=10)

sentences = read_file("sentences.txt")

current_sentence = ""
start_time = 0



app.mainloop()