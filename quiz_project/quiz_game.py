import json
import random

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def run_quiz(questions):
    score = 0

    for question in questions:
        print(question['prompt'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (1, 2, 3, or 4): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if question['options'][int(user_answer) - 1].startswith(question['answer']):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}\n")
        else:
            print("Invalid input. Please enter a number between 1 and 4.\n")

    return score

def main():
    questions = load_questions('questions.json')  # Update the file path
    random.shuffle(questions)

    print("\nWelcome to the Quiz Game!")
    print("----------------------------")
    
    player_score = run_quiz(questions)

    print(f"\nYour score: {player_score}/{len(questions)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
