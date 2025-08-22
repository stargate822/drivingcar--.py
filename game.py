#!/usr/bin/env python3
"""
Simple Quiz Game 🎮
A fun multiple-choice quiz with questions about Python, movies, and general knowledge.
"""


import random

# ---------------------------
# Function definitions
# ---------------------------

def display_welcome():
    """Display welcome message and game instructions."""
    print("🎮 Welcome to the Simple Quiz Game! 🎮")
    print("=" * 40)
    print("Answer the multiple-choice questions by typing the letter (a, b, c, or d)")
    print("Good luck and have fun!\n")

def get_questions():
    """Return a list of quiz questions with answers."""
    return [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 5"],
            "answer": "b"
        },
        {
            "question": "Which movie won the Best Picture Oscar in 1994?",
            "options": ["a) Forrest Gump", "b) Pulp Fiction", "c) The Shawshank Redemption", "d) Speed"],
            "answer": "a"
        },
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Paris", "c) Madrid", "d) Rome"],
            "answer": "b"
        }
    ]

def ask_question(question_data, question_num, total_questions):
    """Ask a single question and return whether the answer was correct."""
    print(f"Question {question_num}/{total_questions}")
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer: ").lower().strip()
    if answer == question_data["answer"]:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer was {question_data['answer']}.\n")
        return False

def display_final_score(score, total_questions):
    """Display the final score with encouraging message."""
    print("=" * 40)
    print(f"🎯 Your Final Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    if percentage == 100:
        print("🏆 Perfect! You're a quiz master!")
    elif percentage >= 70:
        print("👍 Great job!")
    else:
        print("💪 Keep practicing, you'll get better!")
    print("=" * 40 + "\n")

def play_quiz():
    """Main quiz game logic."""
    questions = get_questions()
    random.shuffle(questions)
    score = 0
    total_questions = len(questions)
    print(f"Starting quiz with {total_questions} questions...\n")
    for i, question in enumerate(questions, 1):
        if ask_question(question, i, total_questions):
            score += 1
    display_final_score(score, total_questions)
    return score, total_questions

def main():
    """Main game loop with replay functionality."""
    display_welcome()
    games_played = 0
    total_score = 0
    total_questions = 0
    while True:
        score, questions_count = play_quiz()
        games_played += 1
        total_score += score
        total_questions += questions_count

        if games_played > 1:
            avg_percentage = (total_score / total_questions) * 100
            print(f"📊 Overall Statistics:")
            print(f"Games played: {games_played}")
            print(f"Total score: {total_score}/{total_questions} ({avg_percentage:.1f}%)\n")

        play_again = input("Would you like to play again? (y/n): ").lower().strip()
        if play_again in ['n', 'no']:
            break
        print("\n" + "="*50)
        print("Starting a new game!")
        print("="*50 + "\n")

    print("Thanks for playing the Simple Quiz Game! 🎮")
    print("Come back anytime for more fun!")

# ---------------------------
# Run the game
# ---------------------------
if __name__ == "__main__":
    main()


