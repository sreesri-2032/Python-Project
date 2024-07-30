import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
nltk.download('vader_lexicon')

#analyzes the given review
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

# Extracts the excel sheet of reviews
df=pd.read_csv("C:\\Users\\sriha\\Downloads\\B0BSRVL2VV.csv")

positive_reviews=neutral_reviews=negative_reviews=0
for row in df.itertuples():
    sentiment_scores=analyze_sentiment(str(row[5]))
    if sentiment_scores['compound']>=0.05:
        positive_reviews+=1
    elif sentiment_scores['compound']>=-0.05:
        neutral_reviews+=1
    else:
        negative_reviews+=1

print(f"positive reviews={positive_reviews} ,negative reviews={negative_reviews} ,neutral reviews={neutral_reviews}")
# Plotting graphs
x=[ "positive_reviews" , "neutral_reviews" , "negative_reviews" ]
y=[ positive_reviews , neutral_reviews , negative_reviews ]

plt.bar( x[0], y[0], color='green')
plt.bar( x[1], y[1], color='blue')
plt.bar( x[2], y[2], color='red')

plt.xlabel('Type of reviews')
plt.ylabel('No.of reviews')
plt.title('Reviews')
plt.legend()
plt.show()