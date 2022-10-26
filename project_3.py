




class Game:

    def __init__(self):
        while True :
            print('''welcome , choose game number ...
            1 : divided by game
            2 : remove duplicate game  ''')
            user_choice = int(input("Enter Game Number : "))



            if user_choice == 1 :
                x = int(input(' Enter First Number : '))
                y = int(input(' Enter Second Number : '))
                self.divided_by(x,y)



            elif user_choice == 2 :
                sentence = input(' Enter your Sentence : ')
                self.NO_duplicate(sentence)



            play_again = input(' press y to play again , n to exit : ')
            if play_again == 'n':
                print('Goodbye ...')
                break
              
    



    def divided_by(self,x,y):
        for n in range(0,101):
            if n%x == 0 and n%y == 0 :
                print(n)



    def NO_duplicate(self,sentence):
        words = []
        for x in sentence.split(' '):
            if x not in words:
                words.append(x)
        print(' '.join(words))
 


g1 = Game()
