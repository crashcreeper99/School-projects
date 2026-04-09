# Programmers:  Lamar
# Course:  CS151, Professor Ebert
# Due Date: March 25, 2026
# Programming Assignment:  PA-3
# Problem Statement: Write some art use a main menu
# Data In: lines,rep_times,text, and art choice
# Data Out: Art based on inputs
# Credits: class and internet

# Name: face_maker
# Purpose: find what feeling of face art wanted by input
# Parameters: None
# Return: art of a face
def face_maker():
    feeling = input("what face you feeling type in Happy, Sad, or Mad?").strip().lower()
    while feeling != "happy" and feeling != "mad" and feeling != "sad":
      print("invaid feeling option")
      feeling = input("what face you feeling type in Happy, Sad, or Mad?").lower().strip()
    if feeling == "happy":
        print(f"( ͡ᵔ ͜ʖ ͡ᵔ )")
    elif feeling == "sad":
        print(f"( ╯︵╰,)")
    elif feeling == "mad":
        print(f"(ㆆ _ ㆆ)")
# Name: animal_maker
# Purpose: find what type of animal art wanted by input
# Parameters: animal
# Return: art of a animal
def animal_maker(animal):
    while animal != "cat" and animal != "dog" and animal != "frog":
      print("invaid animal")
      animal =  input("what animal do you want to frog cat or dog?").strip().lower()
    if animal == "cat":
        print(f"Art by Joan Stark")
        print(r"       \    /\ ")
        print(r"        )  ( ')")
        print(r"       (  /  ) ")
        print(r"jgs     \(__)| ")

    elif animal == "dog":
        print(f"Razza - a mix of Lab and Chow")
        print(r"       / \__")
        print(r"      (    @\___")
        print(r"      /         O")
        print(r"     /   (_____/")
        print(r"    /_____/   U")
    elif animal == "frog":
        print("Art by Joan Stark")
        print("         ()-()")
        print("       .-(___)-.")
        print("        _<   >_")
        print(r"jgs     \/   \/")
# Name: rep_text
# Purpose: repetion of a text base off a input
# Parameters: text,rep_times,and lines_rep
# Return: art of a repetion text
def rep_text(text,rep_times,lines_rep):
    sum_text=""
    for i in range(rep_times):
        sum_text += text
    for lines in range(lines_rep):
        print(sum_text)
# Name: menu
# Purpose: menu to get the art you want from option
# Parameters: none
# Return: art of your choice
def menu():
  art = input("what art do you want a Pattern, animal, or face?").strip().lower()
  while art != "pattern" and art != "animal" and art != "face" :
      print("invaild option")
      art = input("what art do you want a Pattern, animal, or face?").strip().lower()
  if art == "face":
    face_maker()
  elif art == "pattern":
     text = input("what text do you want use for pattern?").lower()
     rep_times = int(input("how long do you want the pattern to be:"))
     lines_rep = int(input("how many lines do you want the pattern to be:"))
     while rep_times < 0 and lines_rep < 0 :
       print("invaid number needs to be greater than 0")
       rep_times = int(input("how long do you want the pattern to be:"))
       lines_rep = int(input("how many lines do you want the pattern to be:"))
     rep_text(text,rep_times,lines_rep)

  elif art == "animal":
    animals=input("what animals do you want to frog, cat, or dog?").strip().lower()
    animal_maker(animals)
menu()
