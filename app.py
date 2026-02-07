from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>My Chat Bot</h2>
    <form method="post" action="/chat">
        <input name="msg" placeholder="Type message" />
        <button>Send</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form["msg"]

    # 👇 your bot logic here
    bot_reply = f"You said: {user_msg}"

    return f"""
    <p><b>You:</b> {user_msg}</p>
    <p><b>Bot:</b> {bot_reply}</p>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run()
