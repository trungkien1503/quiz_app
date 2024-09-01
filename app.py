from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

def load_questions():
    with open('questions.json') as f:
        return json.load(f)

@app.route('/')
def index():
    questions = load_questions()
    return render_template('index.html', questions=questions, enumerate=enumerate)

@app.route('/submit', methods=['POST'])
def submit():
    questions = load_questions()
    correct_answers = 0
    for i, question in enumerate(questions):
        selected_option = request.form.get(f'question-{i}')
        print(f"Question {i}: {question['question']}")
        print(f"Selected Option: {selected_option}")
        print(f"Correct Answer: {question['answer']}")
        if selected_option == question['answer']:
            correct_answers += 1
    print(f"Total Correct Answers: {correct_answers}")
    return render_template('result.html', correct_answers=correct_answers, total_questions=len(questions))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
