from browser import document, html, window

# Simulate the files with localStorage
file = "user_data"

# A utility function to get data from localStorage
def get_data():
    data = window.localStorage.getItem(file)
    if not data:
        return {}
    return eval(data)

# A utility function to save data to localStorage
def save_data(data):
    window.localStorage.setItem(file, str(data))

# Main function to start login/signup process
def start(event=None):
    document["output"].clear()
    L = document["login_signup"].value.lower()
    if L == "signup":
        Signup1()
    elif L == "login":
        login1()
    else:
        document["output"].text = "Please enter 'Login' or 'Signup'"

# Code for Signup
def Signup1():
    document["output"].clear()
    user = document["username"].value
    data = get_data()

    if user in data:
        document["output"].text = "This username is already taken. Try login."
        return

    password = document["password"].value
    # Hashing the password (simple simulation)
    password_hashed = sha256(password.encode('utf-8')).hexdigest()
    
    # Store new user
    data[user] = {
        "password": password_hashed,
        "security_question": document["security_question"].value
    }
    
    save_data(data)
    document["output"].text = "Account created successfully. Please login now."

# Code for Login
def login1():
    document["output"].clear()
    user = document["username"].value
    password = document["password"].value
    data = get_data()

    if user not in data:
        document["output"].text = "Username not found"
        return

    password_hashed = sha256(password.encode('utf-8')).hexdigest()

    if data[user]["password"] == password_hashed:
        document["output"].text = f"Hello {user}, welcome to your account.
    else:
        document["output"].text = "Incorrect password. Please try again."

# Bind the start function to button click event
document["start_button"].bind("click", start)



