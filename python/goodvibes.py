def intro():
    print("Welcome to Moodbot! I'm a bot designed to explore your feelings from home")
    print("Please input the letter of the option you want to enter!")

def options():
    print("\nHow can we help today?......")
    print("\na: Mood Check ")
    print("b: Mood Insights")
    print("c: Mood Journal")
    print("d: Mood Services")
    print("x: Exit")



def main():
    options()
    choice = input("\nEnter your choice: ").lower()
    if choice=="a":
        a()
    elif choice=="b":
        b()
    elif choice == "c":
        c()
    elif choice == "d":
        d()
    elif choice == "x":
        quit()
    else:
        print("Sorry option does not exist!")
        main()
    

def a():
    print("\nAre you feeling....")
    print("\na) Lonely")
    print("b) Depressed")
    print("c) Angry")
    print("d) Stressed")
    print("\no: Back to Options")
    print("x: Exit")

    choice = input("\nEnter your choice: ").lower()
    if choice == "a":
        lonely()
    elif choice == "b":
        depressed()
    elif choice == "c":
        angry()
    elif choice == "d":
        stressed()
    elif choice == "o":
        main()
    elif choice == "x":
        quit()
    else:
        print("Sorry option does not exist!")
        a()



def b():
    print("\n| Angry | Dissapointed | Happy | Tired | Stressed | Sad | Lonely | ")
    choice = input("Type what mood you felt today: ").upper()
    moods =[]
    moods.append(choice)

    insights = input("Would you like to see your mood insights?: ").lower()
    if insights[0] == "y":
        insight()
    else:
        main()

def c():
    pass


def d():
    pass


def insight():
    print("You felt lonely 40% this week. How about checking out our tips!")



def lonely():
    print("\nHere are some tips to help:")
    print("1: Take breaks from social media")
    print("2: Engage in a project you are passionate about")
    print("3: Check in on your friends")
    print("4: Engage in volunteering activities")
    print("5: Share your feelings in our mood journal")

    print("\nHere are some youtube recommendations on feeling lonely...")
    print("TEDX how to get rid of loneliness -  https://youtu.be/vZT-bB66iIk")
    print("The simple cure for loneliness - https://youtu.be/KSXh1YfNyVA")
    print("All the lonely people - https://youtu.be/j-Gil9l8yIE")
    print("\nHere are some website links: ")
    print("https://letstalkloneliness.co.uk/")
    print("https://www.nhs.uk/every-mind-matters/")
    print("https://www.redcross.org.uk/stories/disasters-and-emergencies/uk/coronavirus-six-facts-about-loneliness")
    
    


def depressed():
    print("\nHere are some tips to help:")
    print("1: Cook a healthy meal and celebrate with pictures! ")
    print("2: Exercise outdoors ")
    print("3: Learn to changr negative behaviours")
    print("4: Enroll in a behavioural cognitive therapy course")
    print("5: Create a wellbeing toolbox")

    print("\nHere are some youtube recommendations on feeling depressed...")
    print("Conquering depression - https://youtu.be/Rv9SwZWVkOs")
    print("What is depression - https://youtu.be/z-IR48Mb3W0 ")
    print("Don't suffer from depression in silence - https://youtu.be/shG0ezBeeJc")

    print("\nHere are some website links: https://www.mind.org.uk/information-support/types-of-mental-health-problems/depression/self-care/")
    

def angry():
    print("\nHere are some tips to help:")
    print("1: Breathing/Counting techniques ")
    print("2: Visualisation exercises")
    print("3: Try yoga to calm down")
    print("4: Make entries in a mood journal")
    print("5: Go outdoors")

    
    print("\nHere are some youtube recommendations on feeling angry...")
    

    print("\nHere are some website links: ")

def stressed():
    print("\nHere are some tips to help:")
    print("1: Try guided meditation")
    print("2: Engage in physical exercise")
    print("3: Go outdoors")
    print("4: Make a plan to acheive a goal")
    print("5: Share your feelings in our mood journal")

    print("\nHere are some youtube recommendations on feeling stressed...")
    print("How to cope with anxiety - https://youtu.be/WWloIAQpMcQ")
    print("How to replace anxiety with purpose - https://youtu.be/crUusAyzPxo")
    print("How to eliminate self doubt - https://youtu.be/v1ojZKWfShQ")
    print("Guided meditation: https://youtu.be/P-8ALcF8AGE ")
    print("Self love: https://youtu.be/86m4RC_ADEY")
    print("Morning meditation: https://youtu.be/rvaqPPjtxng ")
    print("Positive attitudes: https://youtu.be/j734gLbQFbU")


    print("\nHere are some website links: ")




intro()
main()
