import random      

class Wordle:
    """A data type representing a game of Wordle.
    """

    def createList(self):
        """Opens a txt file of 5 letter words and creates a global variable of list type containing every word in the a.txt file.
        """
        global fileToList
        wordFile = open("a.txt", "r")

        data = wordFile.read()
        fileToList = data.split("\n")
        wordFile.close()

    def createListAI(self):
        """Opens the a.txt file and creates a global variable of list type containing every word in the a.txt file for use by the AI.
        """
        global fileToListAI
        wordFile = open("a.txt", "r")

        data = wordFile.read()
        fileToListAI = data.split("\n")
        wordFile.close()

    def pickWord(self):
        """Picks a word randomly from the list made in createList.
        """
        pick = random.choice(fileToList)
        return pick
    
    def answerWord(self):
        """Picks a word randomly from the list made in createList and sets that as the variable corresponding to a win.
        """
        global win
        win = self.pickWord()
        return win

    def allowGuess(self, guess):
        """Accepts a str guess and returns true if that string is exactly 5 characters and false otherwise.
        """
        if len(guess) != 5:
            return False
        else: return True

    def winsForPlayer(self, guess):
        """Accepts a str guess and returns true if that string is identical to the word that is randomly selected to be the winning word.
        """
        if guess == win:
            return True
        else: 
            return False
        
    def checkWords(self, guess):
        """Accepts a str guess and checks if letters within the word are in the answer and returns a string containing (_/?/!).
           _ if the letter was not in the answer, ? if the letter was in the answer but in the wrong spot 
           and ! if the letter is in the right spot.
        """
        g = guess
        w = win
        score = ['_', '_', '_', '_', '_']
        guess = list(g)
        answer = list(w)
        count = []

        for i in range(len(score)):
            if g[i] == w[i]:
                score[i] = '!'

        for i in range(len(score)):
            if score[i] == '!':
                count.append(i)

        x = len(count) - 1
        while x >= 0:
            answer.pop(count[x])
            x -= 1

        for i in range(len(score)):
            if guess[i] in answer:
                if score[i] == '!':
                    pass
                else: score[i] = '?'

        sco = ""

        for i in range(len(score)):
            sco += score[i]

        print(sco)

    def checkWordAI(self, guess):
        """Accepts a str guess and checks if letters within the word are in the answer and returns a list containing (_/?/!).
           _ if the letter was not in the answer, ? if the letter was in the answer but in the wrong spot 
           and ! if the letter is in the right spot.
        """
        g = guess
        w = win
        score = ['_', '_', '_', '_', '_']
        guess = list(g)
        answer = list(w)
        count = []

        for i in range(len(score)):
            if g[i] == w[i]:
                score[i] = '!'

        for i in range(len(score)):
            if score[i] == '!':
                count.append(i)

        x = len(count) - 1
        while x >= 0:
            answer.pop(count[x])
            x -= 1

        for i in range(len(score)):
            if guess[i] in answer:
                if score[i] == '!':
                    pass
                else: score[i] = '?'
        
        return score

    def aiCompare(self):
        """Picks a random word from the master list of words and returns a list of possible guesses for the AI to use.
        """
        global final2
        answer = 'oaval'
        word = []
        guess = self.pickWord()
        word[:0] = guess
        returns = self.checkWordAI(guess)
        save1 = []
        save2 = []
        save3 = []
        save4 = []
        save_ = []
        save__ = []
        final = []
        final2 = []
        count = 0
        w = ""
    
        for i in range(len(returns)):
            if returns[i] == '!':
                save1.append(word[i])
                save2.append(i)

        for i in range(len(returns)):
            if returns[i] == '?':
                save3.append(word[i])
                save4.append(i)


        for i in range(len(returns)):
            if returns[i] == '_':
                save_.append(word[i])
                save__.append(i)

 

        for i in range(len(fileToListAI)):
            x = []
            x = list(fileToListAI[i])

            if len(save2) > 0:
                if x[save2[0]] == save1[0]:
                    final.append(fileToListAI[i])

        if len(save1) > 0:
            save1.remove(save1[0])
            save2.remove(save2[0])

        for i in range(len(save1)):
            if x[save2[i]] == save1[i]:
                final.remove(final[i])

        if len(final) > 0:
            for i in range(len(final)):
                counts = len(save3)
                y = list(final[i])
                if counts == 0:
                    pass
                elif counts == 1:
                    if save3[0] in y and y[save4[0]] != save3[0]:
                        final2.insert(0, final[i])
                elif counts == 2:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1]:
                        final2.insert(0, final[i])
                elif counts == 3:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2]:
                        final2.insert(0, final[i])
                elif counts == 4:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2] and save3[3] in y and y[save4[3]] != save3[3]:
                        final2.insert(0, final[i])
                elif counts == 5:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2] and save3[3] in y and y[save4[3]] != save3[3] and save3[4] in y and y[save4[4]] != save3[4]:
                        final2.insert(0, final[i])
        else:
            for i in range(len(fileToListAI)):
                counts = len(save3)
                y = list(fileToListAI[i])
                if counts == 0:
                    pass
                elif counts == 1:
                    if save3[0] in y and y[save4[0]] != save3[0]:
                        final2.insert(0, fileToListAI[i])
                elif counts == 2:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1]:
                        final2.insert(0, fileToListAI[i])
                elif counts == 3:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2]:
                        final2.insert(0, fileToListAI[i])
                elif counts == 4:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2] and save3[3] in y and y[save4[3]] != save3[3]:
                        final2.insert(0, fileToListAI[i])
                elif counts == 5:
                    if save3[0] in y and y[save4[0]] != save3[0] and save3[1] in y and y[save4[1]] != save3[1] and save3[2] in y and y[save4[2]] != save3[2] and save3[3] in y and y[save4[3]] != save3[3] and save3[4] in y and y[save4[4]] != save3[4]:
                        final2.insert(0, fileToListAI[i])

    def aiMove(self):
        """Takes either the aiCompare list or the full list of words and makes a guess for the AI.
        """
        if len(final2) > 0:
            answer = random.choice(final2)
            return answer
        else:
            answerr = random.choice(fileToList)
            return answerr

    def hostGame(self):
        """Runs a game of wordle between two separate human players.
        """
        print('Welcome to two-player Wordle!')
        print('')
        self.createList()
        self.answerWord()
        player1Guesses = []
        player2Guesses = []
        while True:

            player1 = input("\n Player 1 Guess: ")
            self.checkWords(player1)
            player1Guesses += [player1]
            print(player1Guesses)

            while self.allowGuess(player1) == False:
                print ("Please enter only a 5 letter word, try again.")
                player1 = input("\n Player 1 Guess: ")

            if self.winsForPlayer(player1):
                print("\n Player 1 Wins!")
                break

            player2 = input("\n Player 2 Guess: ")
            self.checkWords(player2)
            player2Guesses += [player2]
            print(player2Guesses)

            while self.allowGuess(player2) == False:
                print ("Please enter only a 5 letter word, try again.")
                player2 = input("\n Player 1 Guess: ")
        
            if self.winsForPlayer(player2):
                print("\n Player 2 Wins!")
                break
    
    def hostGameAI(self):
        """Runs a game of wordle between two AI players
        """
        
        print('Welcome to AI Wordle!')
        print('')
        self.createList()
        self.createListAI()
        self.answerWord()
        player1Guesses = []
        player2Guesses = []
        while True:
            self.aiCompare()
            player1 = self.aiMove()
            player1Guesses += [player1]
            print('AI1Guesses', player1Guesses)
            if self.winsForPlayer(player1):
                print("\n Player 1 Wins!")
                break
            
            self.aiCompare()
            player2 = self.aiMove()
            player2Guesses += [player2]
            print('AI2Guesses', player2Guesses)
            if self.winsForPlayer(player2):
                print("\n Player 2 Wins!")

    def hostGameAIPlayer(self):
        """Runs a game of wordle between a player and AI
        """
        
        print('Welcome to Wordle!')
        print('')
        self.createList()
        self.createListAI()
        self.answerWord()
        player1Guesses = []
        player2Guesses = []
        while True:
            
            player1 = input("\n Player 1 Guess: ")
            self.checkWords(player1)
            player1Guesses += [player1]
            print('Player1Guesses', player1Guesses)

            while self.allowGuess(player1) == False:
                print ("Please enter only a 5 letter word, try again.")
                player1 = input("\n Player 1 Guess: ")

            self.aiCompare()
            player2 = self.aiMove()
            player2Guesses += [player2]
            print('AI2Guesses', player2Guesses)
            if self.winsForPlayer(player2):
                print("\n AI Wins!")