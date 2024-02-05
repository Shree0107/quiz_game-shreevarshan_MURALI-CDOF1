import json
import random
import os

def load_questions(file_path):
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file '{file_path}'. Make sure the file is valid JSON.")
        exit(1)

def run_quiz(questions):
    score = 0

    for question in questions:
        print(question.get('prompt', 'No prompt available'))
        for i, option in enumerate(question.get('options', []), 1):
            print(f"{i}. {option}")

        while True:
            user_answer = input("Your answer (1, 2, 3, or 4): ")

            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= 4:
                    if question['options'][user_answer - 1].startswith(question.get('answer', '')):
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is {question.get('answer', 'unknown')}\n")
                else:
                    print("Invalid input. Please enter a number between 1 and 4.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue
            else:
                break

    return score

def main():
    print("""

█▀█ █░█ █ ▀█ █ █ █
▀▀█ █▄█ █ █▄ ▄ ▄ ▄
    """)

    script_directory = os.path.dirname(os.path.realpath(__file__))
    questions_path = os.path.join(script_directory, 'questions.json')
    questions = load_questions('questions.json')  # Update the file path
    if not questions:
        print("No questions loaded. Exiting.")
        exit(1)

    random.shuffle(questions)

    print("Welcome to the Quiz Game!")
    print("----------------------------")

    player_score = run_quiz(questions)

    print(f"\nYour score: {player_score}/{len(questions)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()


