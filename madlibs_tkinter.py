import tkinter as tk
import random

# Random story templates
templates = [
    "Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb}.",
    "In the land of {place}, a {adjective} {noun} decided to {verb} all day long.",
    "The {adjective} {noun} went to {place} and started to {verb} unexpectedly!",
    "At {place}, a {noun} became very {adjective} and tried to {verb} bravely."
]

def generate_story():
    noun = noun_entry.get()
    verb = verb_entry.get()
    adjective = adjective_entry.get()
    place = place_entry.get()

    if noun and verb and adjective and place:
        template = random.choice(templates)
        story = template.format(noun=noun, verb=verb, adjective=adjective, place=place)
        story_label.config(text=story, fg='gold')
    else:
        story_label.config(text='⚠ Please fill all fields!', fg='red')

# Main Window
root = tk.Tk()
root.title('MadLibs by Tanzeel')
root.geometry('600x400')
root.configure(bg='#1e1e2f')

# Title
title = tk.Label(root, text='✨ MadLibs Story Generator ✨', font=('Segoe UI', 16, 'bold'), bg='#1e1e2f', fg='gold')
title.pack(pady=10)

# Inputs
frame = tk.Frame(root, bg='#1e1e2f')
frame.pack(pady=10)

tk.Label(frame, text='Noun:', bg='#1e1e2f', fg='white').grid(row=0, column=0, padx=5, pady=5)
noun_entry = tk.Entry(frame, width=25)
noun_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text='Verb:', bg='#1e1e2f', fg='white').grid(row=1, column=0, padx=5, pady=5)
verb_entry = tk.Entry(frame, width=25)
verb_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text='Adjective:', bg='#1e1e2f', fg='white').grid(row=2, column=0, padx=5, pady=5)
adjective_entry = tk.Entry(frame, width=25)
adjective_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text='Place:', bg='#1e1e2f', fg='white').grid(row=3, column=0, padx=5, pady=5)
place_entry = tk.Entry(frame, width=25)
place_entry.grid(row=3, column=1, padx=5, pady=5)

# Button
generate_btn = tk.Button(root, text='Generate Story', command=generate_story, bg='gold', fg='black', font=('Segoe UI', 12, 'bold'))
generate_btn.pack(pady=10)

# Story Output
story_label = tk.Label(root, text='', wraplength=550, justify='center', bg='#1e1e2f', fg='white', font=('Segoe UI', 12))
story_label.pack(pady=20)

# Run app
root.mainloop()
