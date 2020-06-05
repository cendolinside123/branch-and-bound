#!/usr/bin/env python3




# I follow the case base from this video: https://youtu.be/upcsrgqdeNQ
# Edit the vaiable if you want change the case value 


class Rules:
    # Z = 5 X + 6 Y
    # x + y <= 5
    # 4 X + 7 Y <= 28
    # X , Y >= 0 ,  X and Y are integer
    #valueOfX = 5
    #valueOfY = 6

    #valueOfX_firstRule = 1
    #valueOfY_firstRule = 1
    #totalValue_firstRule = 5

    #valueOfX_secondRule = 4
    #valueOfY_secondRule = 7
    #totalValue_secondRule = 28

    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Rules.__instance == None:
            Rules()
        return Rules.__instance


    def __init__(self):

        if Rules.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Rules.__instance = self

        self.valueOfX = 100
        self.valueOfY = 150

        self.valueOfX_firstRule = 8000
        self.valueOfY_firstRule = 4000
        self.totalValue_firstRule = 40000

        self.valueOfX_secondRule = 15
        self.valueOfY_secondRule = 30
        self.totalValue_secondRule = 200

if __name__ == "__main__":
    print(Rules.getInstance().valueOfX)
    print(Rules.getInstance().valueOfY)