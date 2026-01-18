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

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    # Initialize scores if not present
    if 'dice_wins' not in session:
        session['dice_wins'] = 0
    if 'dice_losses' not in session:
        session['dice_losses'] = 0
    if 'dice_ties' not in session:
        session['dice_ties'] = 0

    outcome = None
    
    if request.method == 'POST':
        # Game Logic
        player_roll = random.randint(1, 6)
        cpu_roll = random.randint(1, 6)
        
        dice_icons = {
            1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'
        }
        
        player_icon = dice_icons[player_roll]
        cpu_icon = dice_icons[cpu_roll]
        
        result_message = ""
        result_class = ""
        
        if player_roll > cpu_roll:
            result_message = "You Win!"
            result_class = "win"
            session['dice_wins'] += 1
        elif cpu_roll > player_roll:
            result_message = "Computer Wins!"
            result_class = "lose"
            session['dice_losses'] += 1
        else:
            result_message = "It's a Tie!"
            result_class = "tie"
            session['dice_ties'] += 1
            
        outcome = {
            'player_roll': player_roll,
            'player_icon': player_icon,
            'cpu_roll': cpu_roll,
            'cpu_icon': cpu_icon,
            'message': result_message,
            'class': result_class
        }
     
    return render_template('dice.html', 
                           outcome=outcome,
                           wins=session['dice_wins'],
                           losses=session['dice_losses'],
                           ties=session['dice_ties'])

#==================== ROCK PAPER SCISSORS GAME ====================

@app.route('/rps', methods=['GET', 'POST'])
def rps():
    if request.method == 'POST':
        player_choice = request.form.get('choice')
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        
        result = None
        if player_choice == computer_choice:
            result = 'tie'
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = 'win'
        else:
            result = 'lose'
            
        return render_template('rock-paper-scissors.html', 
                               player_choice=player_choice,
                               computer_choice=computer_choice,
                               result=result)
                               
    return render_template('rock-paper-scissors.html', result=None)

#=================== NUMBER GUESSING GAME ==================

@app.route('/guess', methods=['GET', 'POST'])
def guess_number():
    if 'target_num' not in session or request.args.get('reset'):
        session['target_num'] = random.randint(1, 100)
        session['attempts'] = 0
        session['guess_message'] = "Guess a number between 1 and 100!"
        session['guess_status'] = "info" # info, success, warning, error
        session['game_won'] = False
        
        if request.args.get('reset'):
            return redirect(url_for('guess_number'))

    if request.method == 'POST':
        try:
            user_guess = int(request.form.get('guess'))
            session['attempts'] += 1
            target = session['target_num']
            
            if user_guess == target:
                session['guess_message'] = f"CORRECT! The number was {target}."
                session['guess_status'] = "success"
                session['game_won'] = True
            elif user_guess > target:
                session['guess_message'] = f"Too High! Try lower than {user_guess}."
                session['guess_status'] = "warning"
            else:
                session['guess_message'] = f"Too Low! Try higher than {user_guess}."
                session['guess_status'] = "warning"
                
        except ValueError:
            session['guess_message'] = "Please enter a valid number."
            session['guess_status'] = "error"

    return render_template('guess.html', 
                           message=session.get('guess_message'),
                           status=session.get('guess_status'),
                           attempts=session.get('attempts'),
                           game_won=session.get('game_won'))

if __name__ == '__main__':
    app.run(debug=True)





