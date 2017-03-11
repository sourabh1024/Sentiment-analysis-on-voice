import speech_recognition as sr

from os import path

class SpeechRecognition:
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "Data/amy.wav")

    def convert_to_audio(self):
        # Use the audio file as audio source
        # sr = speech_recognition()
        r = sr.Recognizer()
        with sr.AudioFile(self.AUDIO_FILE) as source:
            audio = r.record(source)
        return audio

    def recognize_sphinix_from_audio(self):
        ''' use sphinx to recognize text from voice '''
        try:
            return (sr.Recognizer().recognize_sphinx(audio_data=self.convert_to_audio(), language="en-US"))
        except Exception as ex:
            print("Sphinx error; {0}".format(ex))

    def recognize_google_from_audio(self):
        GOOGLE_API_KEY="AIzaSyA8SEIFogNEDM8vdhufYB85m6pqwFKEa1I"
        try:
            return (sr.Recognizer().recognize_google(audio_data = self.convert_to_audio(), language="en-US"))
        except Exception as ex:
            print ("Google error; {0}".format(ex))

    def get_text_from_audio(self, audio_path):
        ''' returns the text from voice from thevoice sample at path '''
        self.AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),audio_path)
        return self.recognize_sphinix_from_audio()
