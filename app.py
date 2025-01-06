from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load vocabulary
vocabulary = pd.read_csv('vocabulary.csv')
questions = vocabulary.to_dict('records')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Check the user's answer
        question = request.form['question']
        user_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        is_correct = user_answer.strip().lower() == correct_answer.strip().lower()

        return render_template('quiz.html', question=None, is_correct=is_correct, correct_answer=correct_answer)

    # Randomly select a question
    question = random.choice(questions)
    return render_template('quiz.html', question=question, is_correct=None)


if __name__ == '__main__':
    app.run(debug=True)
