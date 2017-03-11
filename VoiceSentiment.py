import Sentiment
import SpeechRecognition
from nltk.tokenize import sent_tokenize

class VoiceSentiment:

    def __init__(self, audio_path):
        self.AUDIO_PATH = audio_path
        self.sentiment = Sentiment.SentimentModel()
        self.speechRecognition = SpeechRecognition.SpeechRecognition()

    def get_sentence_from_voice(self):
        text = self.speechRecognition.get_text_from_audio(audio_path= self.AUDIO_PATH)
        return sent_tokenize(text)

    def get_sentiment(self, sentence):
        return self.sentiment.get_sentence_sentiment(sentence)

    def get_voice_sentiment(self):
        sentence  = self.get_sentence_from_voice()
        print ("Text from voice : \n" + str(sentence))
        sentiment_score = self.get_sentiment(sentence)
        print("{:-<65} {}".format(sentence, str(sentiment_score)))


if __name__ == '__main__':
    AUDIO_PATH = "Data/Sample Order Taking - Customer Support Philippines.wav"
    voiceSentiment = VoiceSentiment(AUDIO_PATH)
    voiceSentiment.get_voice_sentiment()
