from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
# Declaring some global variables
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # To access the global variable in local scope
    global REPS
    # window.after is the timer module provided by tkInter
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)

    if REPS == 8:
        countdown(long_break_sec)
        label.config(text="Long Break", fg=RED)

    if REPS == 2 or REPS == 4 or REPS == 6:
        countdown(short_break_sec)
        label.config(text="Short Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global REPS, TIMER
    # math.floor will return the largest integer <=x
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # arguments are time, function to call, arguments, calling the same function again
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=2, row=1)

# Canvas is a special method in tkInter to draw pictures and make use of that.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
button.grid(column=1, row=3)

button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
button.grid(column=3, row=3)

check_mark = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)

window.mainloop()
