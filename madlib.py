
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!


"""
Once upon a time there was a(n) [adjective] princess who was imprisoned in a(n) [adjective2] [big noun]. 
The [big noun] was guarded by a fearsome [animal].
One day after eating her breakfast ([food]), she found herself feeling very [emotion], and decided to escape.
Using a [noun], a [noun], [number][plural noun], and her expert [hobby] skills, she managed to outwit the [animal] and begin her journey home.
"""

req = "Provide a"
adj1 = input(req + "n adjective: ")
adj2 = input(req + " different adjective: ")
bignoun = input(req + " large object: ")
animal = input(req + "n animal: ")
food = input(req + " food: ")
emotion = input(req + "n emotion: ")
noun2 = input(req + "n object: ")
noun3 = input(req + " different object: ")
plnoun = input(req + " third object: ")
numb = input(req + " number: ")
hobby = input(req + " hobby: ")

print(f"\nOnce upon a time there was a(n) {adj1} princess who was imprisoned in a(n) {adj2} {bignoun}. \nThe {bignoun} was guarded by a fearsome {animal}.\nOne day after eating her favourite breakfast - {food} - she found herself feeling very {emotion}. She decided it was finally time to escape.\nUsing a {noun2}, a {noun3}, {numb} {plnoun}s, and her expert {hobby} skills, she managed to outwit the {animal} and begin her journey home.")














































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")