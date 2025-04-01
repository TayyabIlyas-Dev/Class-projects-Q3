#  for stylish  ui in browser
# import streamlit as st
# import random

# st.title("🎭 Mad Libs Story")

# name = st.text_input("Enter your name:")
# place = st.text_input("Enter a place:")
# animal = st.text_input("Enter an animal:")

# stories = [
#     "{name} went to {place} for an adventure. There, they met a {animal} who showed them a secret path.",
#     "One fine day, {name} visited {place}. Suddenly, a {animal} appeared and led them to a hidden treasure!",
#     "At {place}, {name} found a lost {animal}. Together, they explored the mysterious caves nearby."
# ]

# if st.button("Generate Story"):
#     if name and place and animal:
#         story = random.choice(stories).format(name=name, place=place, animal=animal)
#         st.success(story)
#     else:
#         st.error("Please fill in all fields!")

# only for console

import random

name = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

if name and place and animal:
    stories = [
        f"{name} went to {place} for an adventure. While exploring, a {animal} appeared and led them to a hidden cave full of glowing crystals.",
        f"One day, {name} was wandering in {place} when a friendly {animal} approached. It seemed to know a secret way through the forest.",
        f"At {place}, {name} found a lost {animal}. Together, they walked through the hills and discovered an ancient ruin filled with mysteries."
    ]

    print("\nYour Story from Mad Libs:")
    print(random.choice(stories))
else:
    print("Please enter valid inputs!")
