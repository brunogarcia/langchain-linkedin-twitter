from flask import Flask, request, jsonify

from ice_breaker import ice_break

app = Flask(__name__)


@app.route("/summary", methods=["POST"])
def process():
    name = request.form["name"]
    person_info = ice_break(name=name)

    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topics_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
