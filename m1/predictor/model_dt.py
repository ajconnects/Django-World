from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Sample dataset
data = {
    "Age": [25, 30, 35, 40, 45],
    "Income": [5000, 6000, 7000, 8000, 9000],
    "Purchases": [5, 3, 2, 4, 1],
    "WillBuy": ["No", "No", "Yes", "Yes", "Yes"],
}
table = pd.DataFrame(data)
print(table)

# Feature columns and target column
features = table[["Age", "Income", "Purchases"]]
target = table["WillBuy"]

# Train Decision Tree model
def train_dt_model():
    model = DecisionTreeClassifier(random_state=0)
    model.fit(features, target)
    return model

# Function to make predictions
def make_prediction2(model, age, income, purchases):
    input_data = pd.DataFrame(
        {"Age": [age], "Income": [income], "Purchases": [purchases]}
    )
    prediction = model.predict(input_data)
    return prediction[0]