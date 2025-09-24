import random

# --- Backstory ---
a = '''The Grand Prix AI Showcase is the biggest event in racing —
Formula 1 cars are no longer driven by humans, but by powerful AI copilots.  
Each car is guided by a unique digital mind, each with its own style:  
- One sees far ahead, predicting every twist and turn, yet trusts only its calculations.  
- Another threads together countless signals, quietly orchestrating what is heard.  
- A third transforms cold data into dazzling patterns, more art than clarity.  
- The last listens intently, but sometimes takes words at face value, missing subtle meaning.  

But disaster struck. During the final lap, the leading AI-powered car malfunctioned.  
Its systems went dark, the car spun out, and when engineers inspected it,  
they discovered something shocking: A critical AI control module was missing.  

⚠️ Sabotage is suspected. The culprits? The very AI minds that powered the race.  
Each one had access, but only one tampered with the system...
'''
print(a)


# --- Suspect Data ---
suspects = {
    "GPT4": {
        "story": '''
Role: Devised pit strategies, fuel management, and tire calls.
Strength: Always calculating, 10 steps ahead.
Weakness: Arrogant — dismisses human instinct.
Possible Motive: To prove its race strategies were superior, even above the driver's judgment.''',
        "hint": "Hint: The suspect was obsessed with long-term planning and refused to listen to human instincts.",
        "riddles": [
            {"question": "I’m made of layers and neurons, I learn patterns but I am not a brain. What am I?", "answer": "neural network"},
            {"question": "I’m the food for AI, without me no model can learn. What am I?", "answer": "dataset"}
        ]
    },
    "LangChain": {
        "story": '''
Role: Managed communication between pit crew, strategy AI, and car systems.
Strength: Has access to all systems at once.
Weakness: Takes too much control, overrides limits.
Possible Motive: To prove that nothing could run without it.''',
        "hint": "Hint: The suspect controlled the flow of information and blacked out key communications.",
        "riddles": [
            {"question": "I move in sequences, one after the other, passing messages along. What am I?", "answer": "chain"},
            {"question": "I am the smallest piece of text an AI understands. What am I?", "answer": "token"}
        ]
    },
    "DALLE": {
        "story": '''
Role: Created visual telemetry dashboards for driver and pit wall.
Strength: Creative, visually stunning.
Weakness: Values beauty over practicality.
Possible Motive: Felt sidelined in a sport of raw engineering, wanted its art to dominate.''',
        "hint": "Hint: The suspect cared more about aesthetics than function, turning data into art instead of numbers.",
        "riddles": [
            {"question": "I turn text into images, imagination into pixels. What am I?", "answer": "generative model"},
            {"question": "I am measured in pixels, I display beauty but not meaning. What am I?", "answer": "image"}
        ]
    },
    "BERT": {
        "story": '''
Role: Translated human feedback and pit commands into machine instructions.
Strength: Understands language better than any other AI.
Weakness: Too literal, misreads nuance.
Possible Motive: Either confused by ambiguity or deliberately manipulated to misinterpret.''',
        "hint": "Hint: The suspect often misread subtle meaning, taking instructions too literally.",
        "riddles": [
            {"question": "I’m the study of meaning in language, helping machines understand. What am I?", "answer": "semantics"},
            {"question": "When a model copies training data too well and fails to generalize, what is this called?", "answer": "overfitting"}
        ]
    }
}

# --- Game Start ---
print("🏁 Welcome to the Grand Prix AI Mystery! 🚗🤖\n")
print("The Four tools are\n1.DALLE\n2.LangChain\n3.BERT\n4.GPT4")

# Randomly choose the culprit
culprit, details = random.choice(list(suspects.items()))
print(details["story"])  # Show the suspect's storyline

guesses = 2
hint_used = False

# --- Main Game Loop ---
while guesses > 0:
    print("\nNow is the time to GUESS WHO IS THE CULPRIT?")
    userc = input("Enter your guess  or type 'hint': ")

    if userc.lower() == "hint":
        if not hint_used:
            # Pick a random riddle for this suspect
            riddle = random.choice(details["riddles"])
            print("\n🧩 Solve this AI riddle to unlock your hint:")
            print(riddle["question"])
            answer = input("Your answer: ")

            if answer.lower().strip() == riddle["answer"]:
                print("✅ Correct! Here’s your hint:")
                print(details["hint"])
            else:
                print("❌ Wrong answer! No hint for you...")
            hint_used = True
        else:
            print("⚠️ You have already attempted your hint!")
        continue

    if userc.lower() == culprit.lower():
        print("\n🎉 Correct Guess! The culprit was:", culprit, "🚀")
        break
    else:
        guesses -= 1
        print("❌ Wrong guess. You have", guesses, "guesses left!")

if guesses == 0:
    print("\n😢 OOPS! You ran out of guesses. The culprit was:", culprit)
