import random

print("Welcome to the 'Who is the lucky one?' game!")
num_people = int(input("How many people are playing? "))

people = []
for i in range(num_people):
    name = input(f"Enter the name of person {i+1}: ")
    people.append(name)

payer = random.choice(people)

print(f"\n{payer} is the one who will pay the bill!")
