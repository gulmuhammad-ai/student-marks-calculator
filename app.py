from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        english = float(request.form["english"])
        math = float(request.form["math"])
        science = float(request.form["science"])

        total = english + math + science
        percentage = total / 3

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"

        return f"""
        <h1>Student Result</h1>
        <p>Student Name: {name}</p>
        <p>Total Marks: {total}</p>
        <p>Percentage: {percentage:.2f}%</p>
        <p>Grade: {grade}</p>
        <br>
        <a href="/">Calculate another result</a>
        """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)