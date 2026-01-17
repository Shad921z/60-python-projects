from flask import Flask, render_template, session, request, redirect, url_for
import random
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Necessary for session management

@app.route("/")
def index():
    return render_template('index.html')

#==================== HANGMAN GAME ====================

@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    # Initialize game if not in session or 'reset' requested
    if 'word' not in session or request.args.get('reset'):
        try:
            response = requests.get("https://random-words-api.kushcreates.com/api?language=en&category=programming_languages&type=lowercase&words=1")
            data = response.json()
            word = str(data[0]['word']).lower()
        except:
            word = "python" # Fallback
            
        session['word'] = word
        session['hidden_word'] = ["_" for _ in word]
        session['guesses'] = 6
        session['game_over'] = False
        session['win'] = False
        session['message'] = ""
        
        if request.args.get('reset'):
            return redirect(url_for('hangman'))

    if request.method == 'POST':
        guess = request.form.get('guess').lower()
        word = session['word']
        hidden_word = session['hidden_word']
        
        if not session['game_over'] and guess and len(guess) == 1 and guess.isalpha():
            if guess in word:
                found = False
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_word[i] = guess
                        found = True
                if found:
                    session['message'] = f"Good guess! '{guess}' is in the word."
                else:
                    session['message'] = f"You already guessed '{guess}'."
            else:
                session['guesses'] -= 1
                session['message'] = f"Sorry, '{guess}' is not in the word."

            session['hidden_word'] = hidden_word # Update session
            
            if "_" not in hidden_word:
                session['game_over'] = True
                session['win'] = True
                session['message'] = "Congratulations! You won!"
            
            if session['guesses'] <= 0:
                session['game_over'] = True
                session['win'] = False
                session['message'] = f"Game Over! The word was '{word}'."
                
    return render_template('hangman.html', 
                           hidden_word=session.get('hidden_word'), 
                           guesses=session.get('guesses'),
                           message=session.get('message'),
                           game_over=session.get('game_over'),
                           win=session.get('win'))

#==================== DICE ROLLER GAME ====================

@app.route('/dice')
def dice():
    # Simple logic to demonstrate python function
    die1 = random.randint(1, 6)
    return f"<h1>Dice Roller</h1><p>You rolled a {die1}!</p><a href='/'>Back</a> <a href='/dice'>Roll Again</a>"

#==================== ROCK PAPER SCISSORS GAME ====================

@app.route('/rps')
def rps():
    return "<h1>Rock Paper Scissors</h1><p>Assume you won!</p><a href='/'>Back</a>"




if __name__ == '__main__':
    app.run(debug=True)





