#! /usr/bin/env python3

from collections import deque

class Nodes:
    
    lastPosition = None

    space = ""

    def __init__ (self,number,xValue,yValue,zValue,status = "-"):
        self.numberNode = number
        self.xValue = float(xValue)
        self.yValue = float(yValue)
        self.zValue = float(zValue)
        self.status = status
        self.left = None
        self.right = None

    def setNodesLeft(self,number,xValue,yValue,zValue,parent,status = "-"):

        if self.numberNode == parent :
            self.left = Nodes(number,xValue,yValue,zValue,status)
        

        if self.left != None:
            self.left.setNodesLeft(number,xValue,yValue,zValue,parent,status)
        
        if self.right != None :
            self.right.setNodesLeft(number,xValue,yValue,zValue,parent,status)

    def setNodesRight(self,number,xValue,yValue,zValue,parent,status = "-"):
        # if self.right == None:
        #     self.right = Nodes(number,xValue,yValue)
        # else:
        #     self.right.setNodeRight(number,xValue,yValue)

        if self.numberNode == parent :
            self.right = Nodes(number,xValue,yValue,zValue,status)
        

        if self.left != None:
            self.left.setNodesRight(number,xValue,yValue,zValue,parent,status)
            #self.left = Nodes(number,xValue,yValue)
        
        if self.right != None :
            self.right.setNodesRight(number,xValue,yValue,zValue,parent,status)

    def getValueOfSelectedNode(self,node):

        if self.numberNode == node:
            #print({'NumberNode': self.numberNode,'x': self.xValue, 'y': self.yValue, 'z': self.zValue, 'status': self.status})
            return {'NumberNode': self.numberNode,'x': self.xValue, 'y': self.yValue, 'z': self.zValue, 'status': self.status}
        
        result = None

        if self.left != None:
            result = self.left.getValueOfSelectedNode(node)

        # if self.right != None:
        #     self.right.getValueOfSelectedNode(node)
        
        if result == None and self.right != None:
            result = self.right.getValueOfSelectedNode(node)
        
        return result
        
        
    
    def getLastValueOfNodeLeft_X(self):

        global lastPosition

        def callBack(value):
            return value

        def callBack_Numeric(value):
            return value

        lastPosition = int(self.xValue)

        if self.left == None:
            if lastPosition == None:
                return callBack("empty")
            else:
                return callBack_Numeric(float(lastPosition))
        else:
            
            return self.left.getLastValueOfNodeLeft_X()

    def getLastValueOfNodeLeft_Y(self):

        global lastPosition

        def callBack(value):
            return value
        
        def callBack_Numeric(value):
            return value

        lastPosition = int(self.yValue)

        if self.left == None:
            if lastPosition == None:
                return callBack("empty")
            else:
                return callBack_Numeric(float(lastPosition))
        else:
            
            return self.left.getLastValueOfNodeLeft_Y()

    
    def showDetail(self,indent = 0):

        space = ''

        if indent :
            
            for _ in range(indent):
                space += " "
            print(space + "Number of node :" + str(self.numberNode))
            print(space + "X value :" + str(self.xValue))
            print(space + "Y value :" + str(self.yValue))
            print(space + "Z value :" + str(self.zValue))
            print(space + "status :" + self.status)
        else:
            print("Number of node :" + str(self.numberNode))
            print("X value :" + str(self.xValue))
            print("Y value :" + str(self.yValue))
            print("Z value :" + str(self.zValue))
            print("status :" + self.status)

        if self.left != None :
            print(space + "Left :")
            self.left.showDetail(indent + 4)

        if self.right != None :
            print(space + "Right :")
            self.right.showDetail(indent + 4)

    def getRoot(self):
        return self



if __name__ == "__main__":

    setParentNode = Nodes(0,1,1,1)

    setParentNode.setNodesLeft(1,0,1,1,0)
    setParentNode.setNodesRight(2,1,1,1,0)
    
    setParentNode.setNodesLeft(3,0,2,1,1)
    setParentNode.setNodesRight(4,1,1,1,1)

    setParentNode.setNodesLeft(5,1,2,1,3)
    setParentNode.setNodesRight(6,1,2,1,3)

    setParentNode.setNodesLeft(-2,1,2,1,2)
    setParentNode.setNodesRight(-1,1,2,1,2)
    
    
    setParentNode.showDetail()
    print(setParentNode.getValueOfSelectedNode(-1))

