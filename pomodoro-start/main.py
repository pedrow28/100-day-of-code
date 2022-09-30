from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#365e18"
YELLOW = "#f7f5dd"
BACKGROUND_COLOR = "#fbf2cf"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=GREEN)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"  # Adding strings
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

# Getting the image
canvas = Canvas(width=200, height=224, bg=BACKGROUND_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Getting image
canvas.create_image(100, 112, image=tomato_img)
# Crating the variable to define the text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

# Label Timer
label = Label(text="Timer", fg=GREEN, bg=BACKGROUND_COLOR, font=(FONT_NAME, 30, "bold"))
label.grid(column=2, row=0)

# Start Button

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=2)

# Reset Button

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)

# Check pomodoro count

check = Label(fg=GREEN, bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, "bold"))
check.grid(column=2, row=3)

window.mainloop()