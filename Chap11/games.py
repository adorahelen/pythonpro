## Games
# Demonstrates Module Creation

class Player (object):
    """ A Player for a game """
    def __init__ (self, name, score = 0):
        self.name = name
        self.score = score

    def __str__ (self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no (question):
    """ Ask a yes or no question """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number (question, low, high):
    """ Ask for a number within a range """
    response = None
    while response not in range (low, high):
        response = int(input(question))
    return response
    
    # this statement is true if the program is run directly
    # and false if imported as a module
if __name__ == "__main__":
    print ("You ran this module directly (and did not 'import' it).")
    input ("\n\nPress Enter to exit")
