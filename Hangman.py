class Hangman:
    def __init__(self, STR = str):
        self.word = STR
        self.wordList =  list(self.word)
        self.n = len(self.wordList)
        self.solution = ['_']*self.n
        self.nonLetters = []
        self.round = 0
        self.burn = 2*(self.n)
        return self.playHangman()
    def printProgress(self):
        return print('Your current progress: ',self.solution)
    def printRound(self):
        return print('Current round: ',self.round)    
        return self
    def Messages(self):
        return ['You won !!', 'You lost !!!!!']
    def printWinLose(self):
        if self.round <= self.burn and self.solution == self.wordList:
            self.printRound()
            print(self.Messages()[0])
        else:
            self.printRound()
            print(self.Messages()[1])
    def solustionHas(self, s):
        for j in range(self.n):
            if s == self.wordList[j]:
                self.solution[j] = s
                self.printProgress()
            else:
                continue
        return self
    def solustionHasNot(self, s):
        self.nonLetters.append(s)
        self.printProgress()
        self.burn -= 1
        return self  
    def solutionChangeUsing(self, s):
        print('Used letters: ',self.nonLetters)
        if s in self.wordList:
            self.solustionHas(s)
        elif s not in self.wordList and s not in self.nonLetters:
            self.solustionHasNot(s)
        else:
            pass
        return self
    def startOfRound(self):
        print('End of turn ',self.round)
        return self
    def endOfRound(self):
        self.printRound()
        self.round += 1
        return self  
    def playHangman(self):
        while self.round in range(2*self.burn) and self.solution != self.wordList and len(self.nonLetters) <= self.burn:
            self.startOfRound()
            s = str(input('Give a letter: '))
            self.solutionChangeUsing(s)
            self.endOfRound()
        self.printWinLose()