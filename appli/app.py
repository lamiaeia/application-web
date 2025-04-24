from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle
with open("C:/Users/HP/Desktop/ia/appli/model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = ""
    if request.method == "POST":
        try:
            features = [
                float(request.form["CreditScore"]),
                int(request.form["Geography"]),
                int(request.form["Gender"]),
                float(request.form["Age"]),
                int(request.form["Tenure"]),
                float(request.form["Balance"]),
                int(request.form["NumOfProducts"]),
                int(request.form["HasCrCard"]),
                int(request.form["IsActiveMember"]),
                float(request.form["EstimatedSalary"]),
            ]
            prediction = model.predict([features])[0]
            prediction = "Client va quitter (Exited)" if prediction == 1 else "Client va rester"
        except:
            prediction = "Erreur dans les données envoyées."
    return render_template("index.html", prediction=prediction)
# Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
