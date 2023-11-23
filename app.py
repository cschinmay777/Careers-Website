from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    "id": "1",
    "title" : "Python Developer",
    "location" : "New York",
    "salary" :"10,00,000",
  },
  {
    "id": "2",
    "title" : "Java Developer",
    "location" : "Mumbai",
    "salary" :"15,00,000",
  },
  {
    "id": "3",
    "title" : "Cpp Developer",
    "location" : "Pune",
    "salary" :"20,00,000",
  }
]

@app.route("/")
def helloWorld():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
