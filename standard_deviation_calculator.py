from statistics import median, mode
import math
import tkinter as tk
from tkinter import Entry, Button, Label, messagebox
import matplotlib.pyplot as plt

user_entered_list = []
labels = []
count = 0
pixel_count = 50

def standard_deviation(list):
    added_sum = 0
    deviation_list = []
    deviation_counter = 0
    for i in list:
        added_sum += float(i)
    mean = float(added_sum/len(list))
    print(f"Mean: {mean}")
    for i in list:
        deviation = float(i) - mean
        squared = deviation * deviation
        deviation_list.append(squared)
    for i in deviation_list:
        deviation_counter += i
    dev_result = deviation_counter / len(deviation_list)
    final_result = math.sqrt(dev_result)
    print(f"standard deviation: {final_result}")
    create_labels()
    median_1 = median(user_entered_list)
    mode_1 = mode(user_entered_list)
    range_1 = max(user_entered_list) - min(user_entered_list)

    plt_name_list = []
    track = 0
    for num in range(len(user_entered_list)):
        plt_name_list.append(num + 1)

    print(len(plt_name_list))
    print(len(user_entered_list))

    SD_label.config(text=f"Standard Deviation: {round(final_result, 3)}")
    mean_label.config(text=f"Mean: {round(mean, 3)}")
    sample_label.config(text=f"Sample Size: {len(deviation_list)}")
    median_label.config(text=f"Median: {median_1}")
    mode_label.config(text=f"Mode: {mode_1}")
    range_label.config(text=f"Range: {range_1}")

    sort_list = sorted(user_entered_list)
    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_geometry("500x500+300+160")
    plt.bar(plt_name_list, sort_list, color="red")
    plt.scatter(plt_name_list, sort_list)
    plt.show()


def add_to_list(*args):
    if len(text_box.get()) == 0:
        messagebox.showerror(title="Try Again", message="Please Enter A Number")
    else:
        num = int(text_box.get())
        user_entered_list.append(num)
        print(user_entered_list)
        add_labels(i=num)
        create_labels()
        text_box.delete(0, "end")

def add_labels(i):
    global labels
    labels.append(Label(text=i, background="black", fg="white", font=("Helvetica", 13)))
    print(labels)

def create_labels():
    global labels, pixel_count
    for i in labels:
        i.place(x=60, y=pixel_count)
        pixel_count += 20
    pixel_count = 50

def reset():
    user_entered_list.clear()
    create_labels()
    for i in labels:
        i.config(text="")
    labels.clear()
    sample_label.config(text="Sample Size: ")
    SD_label.config(text="Standard Deviation: ")
    mean_label.config(text="Mean: ")
    median_label.config(text="Median: ")
    mode_label.config(text="Mode: ")
    range_label.config(text="Range: ")
    plt.close()

root = tk.Tk()
root.geometry("500x500+800+160")
root.config(background="black")
root.title("Standard Deviation Calculator")

text_box = Entry(root, width=7, font=("Helvetica", 20))
text_box.place(x=200, y=200)

button = Button(text="Enter", font=("Helvatica", 15), command=add_to_list)
button.place(x=225, y=250)

label = Label(text="", font=("Helvetica", 15), fg="white", bg="black")
label.place(x=40, y=20)

label_numbers = Label(text="Entered Numbers:", background="black", fg="white", font=("Helvetica", 12))
label_numbers.place(x=10, y=15)

mean_label = Label(root, text="Mean: ", background="black", fg="white", font=("Helvetica", 14))
mean_label.place(x=350, y=15)

SD_label = Label(root, text="Standard Deviation: ", background="black", fg="white", font=("Helvetica", 14))
SD_label.place(x=238, y=90)

sample_label = Label(root, text="Sample Size: ", background="black", fg="white", font=("Helvetica", 14))
sample_label.place(x=290, y=115)

median_label = Label(root, text="Median: ", background="black", fg="white", font=("Helvetica", 14))
median_label.place(x=337, y=40)

mode_label = Label(root, text="Mode: ", background="black", fg="white", font=("Helvetica", 14))
mode_label.place(x=349, y=65)

range_label = Label(root, text="Range: ", background="black", fg="white", font=("Helvetica", 14))
range_label.place(x=340, y=140)

instruction_label = Label(root, text="To find standard deviation, for every number entered, press enter.\nOnce all numbers are entered click calculate", background="black", fg="white", font=("Helvetica", 12))
instruction_label.place(x=30, y=400)

calculate = Button(root, text="Calculate", font=("Helvatica", 15), command=lambda: standard_deviation(list=user_entered_list))
calculate.place(x=208, y=300)

reset_1 = Button(text="Reset", font=("Helvatica", 15), bg="red", fg="white", command=reset)
reset_1.place(x=222, y=350)

root.bind('<Return>', add_to_list)

root.mainloop()



