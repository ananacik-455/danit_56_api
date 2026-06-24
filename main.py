import joblib
import flask
import numpy as np

app = flask.Flask(__name__)

model = joblib.load("model.pkl")

labels = {0: "set", 1: "vers", 2: "verg"}


@app.route('/predict', methods=["POST"])
def predict():

    data = flask.request.get_json()

    X = np.array([ [data["sep_l"],
          data["sep_w"],
          data["pet_l"],
          data["pet_w"]] ]) # 1 x 4
    prediction = model.predict(X)
    return flask.jsonify({"predicted_class": labels[prediction[0]]})#, predicted_label=labels[prediction[0]])

@app.route('/what_next', methods=["GET"])
def end():
    return flask.jsonify({"result":"THIS IS END OF LESSON"})  # , predicted_label=labels[prediction[0]])

# data = {"sep_l":7.1, "sep_w": 3.2, "pet_l":4.4, "pet_w":2.1}

if __name__ == "__main__":
    app.run(debug=True)