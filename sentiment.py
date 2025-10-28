from textblob import TextBlob

text = input("Enter your review: ")
blob = TextBlob(text)

if blob.sentiment.polarity > 0:
    print("😊 Positive")
elif blob.sentiment.polarity < 0:
    print("😠 Negative")
else:
    print("😐 Neutral")
