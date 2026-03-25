from flask import Flask, render_template, request
from quantum_key import generate_quantum_key
import random

app = Flask(__name__)

session_key = generate_quantum_key()


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    generated_key = generate_quantum_key()

    # sometimes force match (for demo)
    if random.randint(0, 1) == 1:
        generated_key = session_key

    if username == "admin" and password == "admin123":

        # make same length
        min_len = min(len(session_key), len(generated_key))

        s_key = session_key[:min_len]
        g_key = generated_key[:min_len]

        if s_key == g_key:
            return render_template(
                "success.html",
                key=g_key,
                session=s_key
            )
        else:
            return render_template(
                "fail.html",
                key=g_key,
                session=s_key
            )

    return render_template(
        "fail.html",
        key="Wrong Username/Password",
        session=session_key
    )


if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)