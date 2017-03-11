class SentimentScore:

    def __init__(self):
        self.pos = 0.0
        self.neg = 0.0
        self.neu = 0.0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ("pos : "+ str(self.pos) +" neg : "+ str(self.neg) + " neu : "+ str(self.neu))
