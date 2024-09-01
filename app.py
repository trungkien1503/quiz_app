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
    results = []
    correct_answers = 0

    for i, question in enumerate(questions):
        selected_option = request.form.get(f'question-{i}')
        correct_option = question['answer']
        is_correct = selected_option == correct_option
        if is_correct:
            correct_answers += 1
        results.append({
            'question': question['question'],
            'selected_option': selected_option,
            'correct_option': correct_option,
            'is_correct': is_correct
        })

    return render_template('result.html', correct_answers=correct_answers, total_questions=len(questions), results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
