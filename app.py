from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # This will load index.html from a "templates" folder

@app.route('/play')
def play():
    user_choice = request.args.get("choice")
    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    
    if user_choice not in choices:
        return "Invalid choice! Use /play?choice=R, /play?choice=P, or /play?choice=S."

    computer_choice = random.choice(["R", "P", "S"])

    # Determine winner
    result = "It's a tie!" if user_choice == computer_choice else (
        "You win!" if (user_choice == "R" and computer_choice == "S") or 
                     (user_choice == "P" and computer_choice == "R") or 
                     (user_choice == "S" and computer_choice == "P") 
        else "Computer wins!"
    )

    return render_template("result.html", user=choices[user_choice], computer=choices[computer_choice], result=result)

if __name__ == "__main__":
    app.run(debug=True)


