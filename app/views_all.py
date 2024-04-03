from app import app, USERS, CONTESTS


@app.route("/")
def index():
    response = (
        f"<h1>Hello World!</h1><br>"
        f"<h2>users:</h2><br>{'<br>'.join([user.to_string() for user in USERS])}<br>"
        f"<h2>contests:</h2><br>{'<br>'.join([contest.to_string() for contest in CONTESTS])}<br>"
    )
    return response
