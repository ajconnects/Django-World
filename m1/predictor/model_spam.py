
import pandas as pd

data = {
    "text": [
        "free money now",
        "Your invoice",
        "Cheap viagra",
        "Re: your resume",
        "Best knives in the world",
        "Re: meeting cancelled",
        "You won!",
        "Re: Your last call",
        "Re: New meeting. Let organize a meeting now!",
    ],
    "label": [
        "spam", "ham", "spam", "ham", "spam", "ham", "spam", "ham", "ham"
    ],
}
df = pd.DataFrame(data)
print(df)

# Text vectorization
#vectorizer = CountVectorizer()
#x = vectorizer.fit_transform(df["text"])

df