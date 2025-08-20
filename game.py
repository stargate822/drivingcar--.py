_______________________________________________________________________________________
#!/usr/bin/env python3
"""Simple Quiz Game 🎮
A fun multiple-choice quiz with questions about Python, movies, and general knowledge.
Displays scores at the end and allows the user to play again.
"""

import random

def display_welcome():
    """Display welcome message and game instructions."""
    print("🎮 Welcome to the Simple Quiz Game! 🎮")
    print("=" * 40)
    print("Answer the multiple-choice questions by typing the letter (a, b, c, or d)")
    print("Good luck and have fun!")
    print()

def get_questions():
    """Return a list of quiz questions with answers."""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
            "answer": "c",
            "category": "Geography"
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2020?",
            "options": ["a) 1917", "b) Parasite", "c) Joker", "d) Once Upon a Time in Hollywood"],
            "answer": "b",
            "category": "Movies"
        },
        {
            "question": "What does 'len()' function do in Python?",
            "options": ["a) Creates a list", "b) Returns the length of an object", "c) Sorts a list", "d) Converts to string"],
            "answer": "b",
            "category": "Python"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["a) Steven Spielberg", "b) Martin Scorsese", "c) Christopher Nolan", "d) Quentin Tarantino"],
            "answer": "c",
            "category": "Movies"
        },
        {
            "question": "Which Python keyword is used to define a function?",
            "options": ["a) function", "b) def", "c) define", "d) func"],
            "answer": "b",
            "category": "Python"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["a) Saturn", "b) Earth", "c) Jupiter", "d) Neptune"],
            "answer": "c",
            "category": "Science"
        },
        {
            "question": "Which movie features the quote 'May the Force be with you'?",
            "options": ["a) Star Trek", "b) Star Wars", "c) Guardians of the Galaxy", "d) Interstellar"],
            "answer": "b",
            "category": "Movies"
        },
        {
            "question": "What is the correct way to create a list in Python?",
            "options": ["a) list = {1, 2, 3}", "b) list = (1, 2, 3)", "c) list = [1, 2, 3]", "d) list = <1, 2, 3>"],
            "answer": "c",
            "category": "Python"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["a) Gold", "b) Oxygen", "c) Silver", "d) Iron"],
            "answer": "b",
            "category": "Science"
        },
        {
            "question": "What year was the first iPhone released?",
            "options": ["a) 2006", "b) 2007", "c) 2008", "d) 2009"],
            "answer": "b",
            "category": "Technology"
        }
    ]
    return questions

def ask_question(question_data, question_num, total_questions):
    """Ask a single question and return whether the answer was correct."""
    print(f"Question {question_num}/{total_questions} - {question_data['category']}")
    print(f"{question_data['question']}")
    print()
    
    for option in question_data['options']:
        print(f"  {option}")
    print()
    
    while True:
        user_answer = input("Your answer (a/b/c/d): ").lower().strip()
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        print("Please enter a valid option (a, b, c, or d)")
    
    correct = user_answer == question_data['answer']
    
    if correct:
        print("✅ Correct! Well done!")
    else:
        # compute index 0..3 from 'a'..'d'
        idx = ord(question_data['answer']) - ord('a')
        correct_option = question_data['options'][idx]
        print(f"❌ Incorrect. The correct answer was: {correct_option}")
    
    print("-" * 50)
    return correct

def display_final_score(score, total_questions):
    """Display the final score with encouraging message."""
    percentage = (score / total_questions) * 100 if total_questions else 0
    
    print("🎉 QUIZ COMPLETED! 🎉")
    print("=" * 30)
    print(f"Your final score: {score}/{total_questions} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("🏆 Outstanding! You're a quiz master!")
    elif percentage >= 70:
        print("🌟 Great job! You did really well!")
    elif percentage >= 50:
        print("👍 Good effort! Keep learning!")
    else:
        print("📚 Don't worry, practice makes perfect!")
    
    print()

def play_quiz():
    """Main quiz game logic. Returns (score, total_questions)."""
    questions = get_questions()
    random.shuffle(questions)  # Randomize question order
    
    score = 0
    total_questions = len(questions)
    
    print(f"Starting quiz with {total_questions} questions...\n")
    
    for i, question in enumerate(questions, 1):
        if ask_question(question, i, total_questions):
            score += 1
        print()  # Extra spacing between questions
    
    display_final_score(score, total_questions)
    return score, total_questions

def main():
    """Main game loop with replay functionality."""
    display_welcome()
    
    games_played = 0
    total_score = 0
    total_questions_all = 0
    
    while True:
        score, this_game_questions = play_quiz()
        games_played += 1
        total_score += score
        total_questions_all += this_game_questions
        
        # Show overall statistics if multiple games played
        if games_played > 1:
            avg_percentage = (total_score / total_questions_all) * 100 if total_questions_all else 0
            print(f"📊 Overall Statistics:")
            print(f"Games played: {games_played}")
            print(f"Total score: {total_score}/{total_questions_all} ({avg_percentage:.1f}%)")
            print()
        
        while True:
            play_again = input("Would you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes', 'n', 'no']:
                break
            print("Please enter 'y' for yes or 'n' for no")
        
        if play_again in ['n', 'no']:
            break
        
        print("\n" + "="*50)
        print("Starting a new game!")
        print("="*50 + "\n")
    
    print("Thanks for playing the Simple Quiz Game! 🎮")
    print("Come back anytime for more fun!")

if __name__ == "__main__":
    main()
