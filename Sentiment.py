from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import SentimentScore

class SentimentModel:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        print ("Initializing Sentiment Model...")

    def analyze_sentiment(self, sentence):
        ''' return the polarity of the sentence '''
        return self.analyzer.polarity_scores(sentence)

    def get_sentence_sentiment(self, sentence):

        ''' This method returns the overall score  of Sentiment in sentence '''
        score = SentimentScore.SentimentScore()
        score.pos = 0
        score.neg = 0
        score.neu = 0
        for sent in sentence:
            sentiment_score = self.analyze_sentiment(sent)
            print (sent + str(sentiment_score))
            score.pos += sentiment_score['pos']
            score.neg += sentiment_score['neg']
            score.neu += sentiment_score['neu']

        return score
