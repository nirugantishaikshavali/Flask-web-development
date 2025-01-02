from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    "id": 1,
    "title": "Software Engineer",
    "location": "New York, NY",
    "salary": "$120,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "San Francisco, CA",
}, {
    "id": 3,
    "title": "Product Manager",
    "location": "Seattle, WA",
    "salary": "$130,000"
}, {
    "id": 4,
    "title": "UX Designer",
    "location": "Austin, TX",
    "salary": "$110,000"
}, {
    "id": 5,
    "title": "DevOps Engineer",
    "location": "Boston, MA",
    "salary": "$125,000"
}]


@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
