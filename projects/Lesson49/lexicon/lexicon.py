Direction = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
Verbs = ["go", "stop", "kill", "eat"]
Stop = ["the", "in", "of", "from", "at", "it"]
Nouns = ["door", "bear", "princess", "cabinet"]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
        
class Lexicon(object):
    def __init__(self):
        self.ingredients = []

    def scan(self, sentence):
        self.ingredients = []
        words = sentence.split()
        for word in words:
            lowerWord = word.lower()
            if lowerWord in Direction:
                self.ingredients.append(('direction', word))
            elif lowerWord in Verbs:
                self.ingredients.append(('verb', word))
            elif lowerWord in Stop:
                self.ingredients.append(('stop', word))
            elif lowerWord in Nouns:
                self.ingredients.append(('noun', word))
            else:
                num = convert_number(lowerWord)
                if None != num:
                    self.ingredients.append(('number', num))
                else:
                    self.ingredients.append(('error', word))        
        return self.ingredients

lexicon = Lexicon()