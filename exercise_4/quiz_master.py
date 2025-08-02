import time  # For tracking time per question
import json  # For saving high scores persistently
import os    # To check if high score file exists

# Quiz Database structured as nested dictionaries by category and difficulty
QUESTIONS_DB = {
    "Science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 1},
            {"question": "Water freezes at what temperature (Celsius)?", "options": ["0", "32", "100", "50"], "answer": 0},
            {"question": "What gas do plants absorb?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 2},
            {"question": "How many legs does an insect have?", "options": ["6", "8", "4", "10"], "answer": 0},
            {"question": "Which vitamin is made when skin is exposed to sunlight?", "options": ["A", "B", "C", "D"], "answer": 3}
        ],
        "hard": [
            {"question": "What is the atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
            {"question": "Which element has the chemical symbol 'Fe'?", "options": ["Fluorine", "Iron", "Francium", "Fermium"], "answer": 1},
            {"question": "What part of the cell produces energy?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "answer": 1},
            {"question": "Which particle has a negative charge?", "options": ["Proton", "Electron", "Neutron", "Quark"], "answer": 1},
            {"question": "Which scientist proposed the theory of relativity?", "options": ["Newton", "Einstein", "Galileo", "Hawking"], "answer": 1}
        ]
    },
    # You can add "History" and "Sports" like Science
}

HIGH_SCORES_FILE = "high_scores.json"  # File to store persistent high scores

# Load high scores from a JSON file
def load_high_scores():
    if not os.path.exists(HIGH_SCORES_FILE):
        # If file doesn't exist, create an empty JSON file
        with open(HIGH_SCORES_FILE, 'w') as f:
            json.dump({}, f)
    with open(HIGH_SCORES_FILE, 'r') as f:
        return json.load(f)

# Save high scores back to the JSON file
def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, 'w') as f:
        json.dump(high_scores, f, indent=4)

# Function to visually show a text-based progress bar
def show_progress(current, total):
    percent = int((current / total) * 100)
    bars = '█' * (percent // 10)  # Each bar represents 10%
    spaces = '░' * (10 - len(bars))
    print(f"[{bars}{spaces}] {percent}% Complete\n")

# Main quiz function
def quiz():
    high_scores = load_high_scores()

    print("=== QUIZ MASTER ===")
    categories = list(QUESTIONS_DB.keys())
    print("Categories:", ", ".join(categories))

    category = input("Select a category: ").strip()
    if category not in QUESTIONS_DB:
        print("Invalid category selected.")
        return

    difficulty = input("Select difficulty (easy/hard): ").strip()
    if difficulty not in QUESTIONS_DB[category]:
        print("Invalid difficulty selected.")
        return

    questions = QUESTIONS_DB[category][difficulty]
    total_questions = len(questions)
    score = 0  # Initialize player score
    wrong_answers = []  # Track questions answered incorrectly

    # Iterate over all questions
    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}/{total_questions}: {q['question']}")
        show_progress(idx, total_questions)

        # Display options A, B, C, D
        for i, opt in enumerate(q["options"]):
            print(f"{chr(65 + i)}) {opt}", end="    ")
        print()

        # Start timing the response
        start_time = time.time()
        user_answer = input("Your answer: ").strip().upper()
        elapsed = time.time() - start_time  # Calculate time taken to answer

        # Convert A-D to index (0-3)
        answer_index = ord(user_answer) - 65

        # Check if user answer is correct
        if 0 <= answer_index < len(q["options"]) and answer_index == q["answer"]:
            print("✅ Correct! (+10 points)")
            score += 10
        else:
            correct_opt = q["options"][q["answer"]]
            print(f"❌ Wrong! Correct Answer: {correct_opt}")
            # Save incorrect question for review
            wrong_answers.append((q["question"], q["options"], q["answer"]))

        print(f"Time: {elapsed:.2f} seconds\n")

    print(f"FINAL SCORE: {score}/{total_questions * 10} ({score // 10}/{total_questions} correct)")

    # Check if user beat their high score and update it
    key = f"{category}_{difficulty}"
    if key not in high_scores or score > high_scores[key]:
        high_scores[key] = score
        save_high_scores(high_scores)
        print(f"🎉 New personal best in {category} ({difficulty})!")
    else:
        print(f"Your best score in {category} ({difficulty}) is: {high_scores[key]}")

    # Show review of wrong answers after quiz
    if wrong_answers:
        print("\nReview of incorrect answers:")
        for q, options, correct_idx in wrong_answers:
            print(f"Q: {q}")
            for i, opt in enumerate(options):
                tag = "✅" if i == correct_idx else " "
                print(f"{tag} {chr(65 + i)}) {opt}")
            print()

if __name__ == "__main__":
    quiz()
