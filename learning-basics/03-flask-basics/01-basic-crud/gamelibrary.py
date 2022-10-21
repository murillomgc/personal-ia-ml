from flask import Flask, render_template, request, redirect, session, flash, url_for


class Game:
    def __init__(self, name, genre, console):
        self.name = name
        self.genre = genre
        self.console = console


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


game1 = Game("Super Mario Bros", "Platform", "NES")
game2 = Game("The Legend of Zelda", "Adventure", "N64")
game3 = Game("Pokemon", "RPG", "GameBoy")
games = [game1, game2, game3]

user1 = User("admin", "admin")
user2 = User("user", "user")
user3 = User("guest", "guest")
users = {user1.username: user1, user2.username: user2, user3.username: user3}


app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    return render_template("list.html", title="Games", games_list=games)


@app.route("/newgame")
def new():
    if "logged_user" not in session or session["logged_user"] == None:
        return redirect(url_for("login"))
    else:
        return render_template("newgame.html", title="New Game")


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    genre = request.form["genre"]
    console = request.form["console"]

    games.append(Game(name, genre, console))

    return redirect(url_for("index"))


@app.route("/login")
def login():
    return render_template("login.html", title="Login")


@app.route("/auth", methods=["POST"])
def auth():
    if request.form["user"] in users:
        user = users[request.form["user"]]
        if user.password == request.form["password"]:
            session["logged_user"] = user.username
            flash(user.username + " logged in successfully!!")
            return redirect("/")
        else:
            flash("Invalid user or password!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["logged_user"] = None
    flash("Logged out successfully!")
    return redirect(url_for("index"))


app.run(debug=True)
