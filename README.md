# Quiz App

A simple web-based quiz application built with Flask and Bootstrap.

## Project Description

This project is a quiz application that allows users to answer multiple-choice questions. The questions are loaded from a JSON file, and the user's answers are submitted and evaluated to provide a score.

## Requirements

- Python 3.x
- Flask
- Bootstrap (via CDN)

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/quiz_app.git
    cd quiz_app
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install flask
    ```

4. **Run the Flask application:**
    ```sh
    python app.py
    ```

5. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

## File Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The main HTML template for the quiz.
- `templates/result.html`: The HTML template for displaying results.
- `questions.json`: The JSON file containing quiz questions and answers.

## Usage

1. Open the application in your web browser.
2. Answer the quiz questions.
3. Submit your answers to see your score.

## License

This project is licensed under the MIT License.
