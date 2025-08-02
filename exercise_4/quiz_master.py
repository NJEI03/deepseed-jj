import time
import json
import os

# Sample Questions Database (3 categories, Easy/Hard, 5 questions each)
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
    "History": {
        "easy": [
            {"question": "Who was the first President of the USA?", "options": ["Lincoln", "Jefferson", "Washington", "Adams"], "answer": 2},
            {"question": "In which year did WW2 end?", "options": ["1945", "1939", "1918", "1965"], "answer": 0},
            {"question": "The Great Wall of China was built to protect against?", "options": ["Romans", "Mongols", "Persians", "Vikings"], "answer": 1},
            {"question": "Who discovered America?", "options": ["Magellan", "Columbus", "Drake", "Cook"], "answer": 1},
            {"question": "Which Egyptian pharaoh had a famous tomb?", "options": ["Tutankhamun", "Ramses", "Cleopatra", "Akhenaten"], "answer": 0}
        ],
        "hard": [
            {"question": "Who was known as the 'Iron Lady'?", "options": ["Angela Merkel", "Margaret Thatcher", "Indira Gandhi", "Golda Meir"], "answer": 1},
            {"question": "The Battle of Hastings took place in?", "options": ["1066", "1215", "1415", "1603"], "answer": 0},
            {"question": "Who was the first emperor of Rome?", "options": ["Nero", "Caesar", "Augustus", "Caligula"], "answer": 2},
            {"question": "The Cold War was between USA and?", "options": ["Germany", "China", "USSR", "Japan"], "answer": 2},
            {"question": "Which treaty ended WW1?", "options": ["Versailles", "Trianon", "St. Germain", "Neuilly"], "answer": 0}
        ]
    },
    "Sports": {
        "easy": [
            {"question": "How many players in a football (soccer) team?", "options": ["9", "10", "11", "12"], "answer": 2},
            {"question": "Tennis is played with how many sets (men's Grand Slam)?", "options": ["3", "5", "7", "9"], "answer": 1},
            {"question": "Which sport is known as the 'king of sports'?", "options": ["Basketball", "Football", "Cricket", "Tennis"], "answer": 1},
            {"question": "How many holes in a standard golf course?", "options": ["9", "12", "15", "18"], "answer": 3},
            {"question": "Which country hosted the 2016 Summer Olympics?", "options": ["China", "Brazil", "UK", "Russia"], "answer": 1}
        ],
        "hard": [
            {"question": "Who has won the most FIFA World Cups?", "options": ["Germany", "Italy", "Brazil", "Argentina"], "answer": 2},
            {"question": "In which year was the NBA founded?", "options": ["1946", "1956", "1966", "1976"], "answer": 0},
            {"question": "Which cricketer is known as 'The Wall'?", "options": ["Tendulkar", "Ponting", "Dravid", "Lara"], "answer": 2},
            {"question": "Who holds the record for most Olympic gold medals?", "options": ["Bolt", "Phelps", "Lewis", "Ledecky"], "answer": 1},
            {"question": "Which country invented table tennis?", "options": ["UK", "China", "Japan", "Germany"], "answer": 0}
        ]
    }
}

HIGH_SCORES_FILE = "high_scores.json"

# Load high scores from file (create if doesn't exist)
def load_high_scores():
    if not os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, 'w') as f:
            json.dump({}, f)
    with open(HIGH_SCORES_FILE, 'r') as f:
        return json.load(f)

# Save high scores to file
def save_high_scores(high_scores):
    with open(HIGH_SCORES_FILE, 'w') as f:
        json.dump(high_scores, f, indent=4)

# Display progress bar
def show_progress(current, total):
    percent = int((current / total) * 100)
    bars = '█' * (percent // 10)
    spaces = '░' * (10 - len(bars))
    print(f"[{bars}{spaces}] {percent}% Complete\n")

def quiz():
    high_scores = load_high_scores()

    print("=== QUIZ MASTER ===")
    categories = list(QUESTIONS_DB.keys())
    print("Categories:", ", ".join(categories))

    # Select category
    category = input("Select a category: ").strip()
    if category not in QUESTIONS_DB:
        print("Invalid category.")
        return

    # Select difficulty
    difficulty = input("Select difficulty (easy/hard): ").strip()
    if difficulty not in QUESTIONS_DB[category]:
        print("Invalid difficulty.")
        return

    questions = QUESTIONS_DB[category][difficulty]
    total_questions = len(questions)
    score = 0
    wrong_answers = []

    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}/{total_questions}: {q['question']}")
        show_progress(idx, total_questions)

        for i, opt in enumerate(q["options"]):
            print(f"{chr(65 + i)}) {opt}", end="    ")
        print()

        start_time = time.time()
        user_answer = input("Your answer: ").strip().upper()
        elapsed = time.time() - start_time

        try:
            answer_index = ord(user_answer) - 65
            if answer_index == q["answer"]:
                print(f"✅ Correct! (+10 points)")
                score += 10
            else:
                correct_opt = q["options"][q["answer"]]
                print(f"❌ Wrong! Correct Answer: {correct_opt}")
                wrong_answers.append((q["question"], q["options"], q["answer"]))
        except:
            print("❌ Invalid input. Question skipped.")

        print(f"Time: {elapsed:.2f} seconds\n")

    print(f"FINAL SCORE: {score}/{total_questions * 10} ({score // 10}/{total_questions} correct)")

    # Check and update high score
    key = f"{category}_{difficulty}"
    if key not in high_scores or score > high_scores[key]:
        high_scores[key] = score
        save_high_scores(high_scores)
        print(f"🎉 New personal best in {category} ({difficulty})!")
    else:
        print(f"Your best score in {category} ({difficulty}) is: {high_scores[key]}")

    # Show summary of wrong answers
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
