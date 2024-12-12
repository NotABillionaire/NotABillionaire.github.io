#Tom
#12/12/2024
#First time using flask



from flask import Flask, request, render_template, redirect, url_for
import os
from hashlib import sha256
import linecache

app = Flask(__name__)

# Ensure files exist
if not os.path.exists("user.txt"):
    open("user.txt", "w").close()

if not os.path.exists("Hashed.txt"):
    open("Hashed.txt", "w").close()

@app.route('/')
def home():
    return render_template('home.html')  # Render the homepage

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        security_answer = request.form['security_answer']
        
        # Check if username exists
        with open("user.txt", "r") as file:
            for line in file:
                data = line.split(",")
                if data[0] == user:
                    return "Username already taken. Try again."
        
        # Add new user
        user_id = str(len(open("user.txt").readlines()) + 1)
        with open("user.txt", "a") as file:
            file.write(f"{user},{user_id}\n")
        
        # Hash the password and save it
        with open("Hashed.txt", "a") as file:
            hashed_password = sha256(password.encode('utf-8')).hexdigest()
            file.write(f"{hashed_password},{security_answer},{user_id}\n")
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = sha256(password.encode('utf-8')).hexdigest()

        user_id = None
        with open("user.txt", "r") as file:
            for line in file:
                data = line.split(",")
                if data[0] == username:
                    user_id = data[1].strip()
                    break
        
        if user_id:
            hashed_line = linecache.getline("Hashed.txt", int(user_id))
            if hashed_password in hashed_line:
                return f"Welcome, {username}!"
            else:
                return "Incorrect password. Try again."
        else:
            return "Username not found. Please sign up first."
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
