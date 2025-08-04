import random
def generate_random_number():
    return random.randint(1, 100)

def generate_random_name():

    names = ["Alice", "Jane", "Luke", "Lyn", "Ethan"]

    return random.choice(names)

def main():
    print("Welcome to the Random Name Generator!")
    random_number = generate_random_number()
    random_name = generate_random_name()

    print("Random number generated:", random_number)

    print("Random number generated:", random_name)
    print("This is a random name generator.")

if __name__ == "__main__":
    main()

