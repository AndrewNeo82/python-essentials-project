"""
import time to set quiz time length and
random to randomise question selection
"""
import time
import random


TIME_LIMIT = 60
MAX_QUESTIONS = 5


class Question:
    """
     Structure for questions containing the question, options, and answers.
     """
    def __init__(self, question, options, answer):
        """_summary_

        Args:
            question (string): _description_
            options ([string]): _description_
            answer (int): Index of correct option from the given list.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self):
        """
        Ask the question and collect the user's answer.
        """
        print(self.question)
        for option in self.options:
            print(option)

        user_answer = get_user_answer()
        return user_answer == self.answer


def get_user_answer():
    """
    Get the user's answer and ensure it is valid (A, B, C, or D).
    """
    while True:
        user_answer = input("Your answer is (A, B, C, or D): ").upper()
        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        else:
            print("Invalid choice. Please select A, B, C, or D.")


questions = {
    "easy": [
        Question("What is the capital of France?",
                 ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
                 "A"),
        Question("Which planet is known as the Red Planet?",
                 ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                 "B"),
        Question("Who painted the Mona Lisa?",
                 ["A) Van Gogh", "B) da Vinci", "C) Picasso", "D) Monet"],
                 "B"),
        Question("What is the largest mammal in the world?",
                 ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Lion"],
                 "B"),
        Question("Which gas do plants primarily use for photosynthesis?",
                 ["A) Oxygen", "B) Argon", "C) Hydrogen", "D) Carbon Dioxide"],
                 "D"),
        Question("What is the capital of Japan?",
                 ["A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok"],
                 "B"),
        Question("Which famous scientist developed the theory of relativity?",
                 ["A) Newton", "B) Galileo", "C) Einstein", "D) Hawking"],
                 "C"),
        Question("Which ocean is the largest on Earth?",
                 ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
                 "C"),
        Question("What is the main function of the heart?",
                 ["A) Pump Blood", "B) Digestion", "C) Produce Hormones",
                  "D) Filter waste"],
                 "A"),
        Question("What is the process by which plants make their own food?",
                 ["A) Respiration", "B) Transpiration",
                  "C) Photosynthesis", "D) Combustion"],
                 "C"),
    ],
    "hard": [
        Question("In which year was the Python programming language released?",
                 ["A) 1989", "B) 1991", "C) 2000", "D) 2005"],
                 "B"),
        Question("What is the smallest prime number?",
                 ["A) 0", "B) 1", "C) 2", "D) 3"],
                 "C"),
        Question("Which philosopher is known for Critique of Pure Reason?",
                 ["A) Nietzsche", "B) Kant", "C) Kierkegaard", "D) Rousseau"],
                 "B"),
        Question("What is the largest species of shark?",
                 ["A) Great White", "B) Hammerhead",
                  "C) Whale Shark", "D) Tiger Shark"],
                 "A"),
        Question("In which year did the Berlin Wall fall?",
                 ["A) 1985", "B) 1989", "C) 1991", "D) 1995"],
                 "B"),
        Question("Which novel features the character Big Brother?",
                 ["A) Brave New World", "B) 1984",
                  "C) Fahrenheit 451", "D) The Giver"],
                 "B"),
        Question("What is the rarest blood type among humans?",
                 ["A) A", "B) B", "C) AB", "D) O Negative"],
                 "D"),
        Question("Which artist painted The Persistence of Memory?",
                 ["A) Salvador Dali", "B) Pablo Picasso",
                  "C) Vincent Van Gogh", "D) Monet"],
                 "A"),
        Question("What is the largest organ in the human body?",
                 ["A) Liver", "B) Brain", "C) Skin", "D) Heart"],
                 "C"),
        Question("Which particle carryies the electromagnetic force?",
                 ["A) Proton", "B) Neutron", "C) Electron", "D) Photon"],
                 "D"),
    ]
}


def play_quiz(difficulty, username):
    """
    Plays the quiz. Randomizes the order of the questions.
    """
    questions_list = questions[difficulty]
    random.shuffle(questions_list)
    questions_list = questions_list[:MAX_QUESTIONS]  # Use the constant here
    score = 0

    total_questions = len(questions_list)

    print("\n" + "="*60)
    print(f"Quiz started for {TIME_LIMIT} seconds...")
    start_time = time.time()

    for question in questions_list:
        # Check the time limit at the beginning of each iteration
        elapsed_time = time.time() - start_time
        remaining_time = TIME_LIMIT - int(elapsed_time)
        if remaining_time <= 0:
            print("Time's up!")
            break

        print("\n" + "="*60)
        print(f"Question: {questions_list.index(question) + 1}")
        print(f"Time remaining: {remaining_time} seconds")

        if question.ask():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\n" + "="*60)
    print(f"Quiz completed, {username}! Your score: {score}/{total_questions}")


def main():
    """
    The main game function, takes the player's username,
    gives the choice of difficulty, and handles invalid choices.
    """
    ascii_art = r"""
                        88
                        ""
 ,adPPYb,d8 88       88 88 888888888
a8"    `Y88 88       88 88      a8P"
8b       88 88       88 88   ,d8P'
"8a    ,d88 "8a,   ,a88 88 ,d8"
 `"YbbdP'88  `"YbbdP'Y8 88 888888888
         88
         88

Welcome to My Quiz Game!

You have 60 seconds to complete the quiz, there are 5 random questions.

Good Luck!
    """
    print(ascii_art)

    username = input("Enter your username: ")
    while True:
        print("\nSelect difficulty:")
        print("1. Easy")
        print("2. Hard")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_quiz("easy", username)
        elif choice == "2":
            play_quiz("hard", username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
