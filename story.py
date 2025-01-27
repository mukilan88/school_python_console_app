import random

def main():
    print("Welcome to the Story Generator!")
    
    # Get user inputs
    name = input("Enter your name: ")
    friend = input("Enter your best friend's name: ")
    place = input("Enter a magical place: ")

    # Story templates
    stories = [
        f"One day, {name} and {friend} found a secret portal to {place}. Inside, they discovered a hidden treasure, but it was guarded by a fierce dragon!",
        f"In {place}, {name} and {friend} encountered a talking cat who asked for help to find its lost magical wand.",
        f"{name} and {friend} were on a school trip when they accidentally traveled to {place}, where they met a wizard who needed their help."
    ]

    # Choose a random story
    story = random.choice(stories)
    print("\nHere's your story:")
    print(story)

    # Option to save the story
    save = input("\nDo you want to save the story? (yes/no): ").lower()
    if save == "yes":
        with open("story.txt", "w") as file:
            file.write(story)
        print("Your story has been saved!")
    else:
        print("Goodbye!")

main()
