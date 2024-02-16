import smtplib
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6cornWlSihBXox7C0sKR6b'
Bootstrap5()

G_MAIL = "99testabdullah@gmail.com"
G_PASSWORD = "rpmy puhd qwpp ffrj"


@app.route('/', methods=["GET", "POST"])
def introduce():
    return render_template('resume.html')


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(G_MAIL, G_PASSWORD)
        connection.sendmail(G_MAIL, G_MAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
