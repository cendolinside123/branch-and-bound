#! /usr/bin/env python3
import os, sys

sys.path.append(os.path.join(sys.path[0].replace('Controller',''), 'Confiq\\'))
sys.path.append(os.path.join(sys.path[0].replace('Controller',''), 'Models\\'))

# sys.path.insert(0, os.path.join(sys.path[0].replace('Controller',''), 'Models\\'))
# sys.path.insert(0, os.path.join(sys.path[0].replace('Controller',''), 'Confiq\\'))

from Nodes import Nodes as Model_Nodes
from Rules import Rules

class BranchAndBound:
    def __init__(self):
        self.node = None
    
    def doCalculation(self):
        # Create first node


        y_1 = Rules.getInstance().valueOfY_firstRule

        z_1 = Rules.getInstance().totalValue_firstRule

        y_2 = Rules.getInstance().valueOfY_secondRule

        z_2 = Rules.getInstance().totalValue_secondRule

        if Rules.getInstance().valueOfX_secondRule > Rules.getInstance().valueOfX_firstRule :
            if Rules.getInstance().valueOfX_firstRule == 1 : 
                y_1 = Rules.getInstance().valueOfY_firstRule * Rules.getInstance().valueOfX_secondRule

                z_1 = Rules.getInstance().totalValue_firstRule * Rules.getInstance().valueOfX_secondRule
            else :
                if Rules.getInstance().valueOfX_secondRule % Rules.getInstance().valueOfX_firstRule != 0 :
                    y_1 = Rules.getInstance().valueOfY_firstRule * Rules.getInstance().valueOfX_secondRule
                    z_1 = Rules.getInstance().totalValue_firstRule * Rules.getInstance().valueOfX_secondRule

                    y_2 = Rules.getInstance().valueOfY_secondRule * Rules.getInstance().valueOfX_firstRule
                    z_2 = Rules.getInstance().totalValue_secondRule * Rules.getInstance().valueOfX_firstRule

                else :
                    aConversionValue = Rules.getInstance().valueOfX_secondRule / Rules.getInstance().valueOfX_firstRule

                    y_1 = Rules.getInstance().valueOfY_firstRule * aConversionValue
                    z_1 = Rules.getInstance().totalValue_firstRule * aConversionValue

        elif Rules.getInstance().valueOfX_secondRule < Rules.getInstance().valueOfX_firstRule :
            if Rules.getInstance().valueOfX_secondRule == 1 : 
                y_2 = Rules.getInstance().valueOfY_secondRule * Rules.getInstance().valueOfX_secondRule

            else :
                if Rules.getInstance().valueOfX_firstRule % Rules.getInstance().valueOfX_secondRule != 0 :
                    y_1 = Rules.getInstance().valueOfY_firstRule * Rules.getInstance().valueOfX_secondRule
                    z_1 = Rules.getInstance().totalValue_firstRule * Rules.getInstance().valueOfX_secondRule

                    y_2 = Rules.getInstance().valueOfY_secondRule * Rules.getInstance().valueOfX_firstRule
                    z_2 = Rules.getInstance().totalValue_secondRule * Rules.getInstance().valueOfX_firstRule

                else :
                    aConversionValue = Rules.getInstance().valueOfX_firstRule / Rules.getInstance().valueOfX_secondRule

                    y_2 = Rules.getInstance().valueOfY_secondRule * aConversionValue
                    z_2 = Rules.getInstance().totalValue_secondRule * aConversionValue

        elif Rules.getInstance().valueOfX_secondRule == Rules.getInstance().valueOfX_firstRule : 
            y_1 = Rules.getInstance().valueOfY_firstRule
            z_1 = Rules.getInstance().totalValue_firstRule

            y_2 = Rules.getInstance().valueOfY_secondRule
            z_2 = Rules.getInstance().totalValue_secondRule

        getY_Value = abs(z_1 - z_2) / abs(y_1 - y_2)

        getX_Value = (Rules.getInstance().totalValue_firstRule - (Rules.getInstance().valueOfY_firstRule * getY_Value)) / Rules.getInstance().valueOfX_firstRule
        totalValue = (Rules.getInstance().valueOfX * getX_Value) + (Rules.getInstance().valueOfY * getY_Value)

        self.node = Model_Nodes(0,getX_Value,getY_Value,totalValue)

        doLoopForCreateTree = True 

        numberOfChildNode = 1
        parrentNode = 0
        startGetConstraintFrom = "y"

        while doLoopForCreateTree :

            getParentValue = {'x':self.node.getValueOfSelectedNode(parrentNode)['x'],'y':self.node.getValueOfSelectedNode(parrentNode)['y']}
            getMaxValue = max(getParentValue.keys(), key=(lambda k: getParentValue[k]))

            if self.number_of_digits_post_decimal(getParentValue['x']) != None and self.number_of_digits_post_decimal(getParentValue['y']) != None :
                getMaxValue = max(getParentValue.keys(), key=(lambda k: getParentValue[k]))
            else :
                if self.number_of_digits_post_decimal(getParentValue['x']) != None and self.number_of_digits_post_decimal(getParentValue['y']) == None :
                    getMaxValue = 'x'

                elif self.number_of_digits_post_decimal(getParentValue['x']) == None and self.number_of_digits_post_decimal(getParentValue['y']) != None :
                    getMaxValue = 'y'

            # if self.number_of_digits_post_decimal(getParentValue[getMinValue]) == None :
            #     if getMinValue == 'x' : 
            #         getMinValue = 'y'
            #     elif getMinValue == 'y':
            #         getMinValue = 'x'


            if startGetConstraintFrom == "x" :
                getX_Value_right = int(getParentValue[getMaxValue])

                getY_Value_right = (Rules.getInstance().totalValue_secondRule - (Rules.getInstance().valueOfX_secondRule * getX_Value_right)) / Rules.getInstance().valueOfY_secondRule

                getZ_Value_right = (Rules.getInstance().valueOfX * getX_Value_right) + (Rules.getInstance().valueOfY * getY_Value_right)

                if getZ_Value_right > self.node.getValueOfSelectedNode(0)['z'] :
                    self.node.setNodesRight(numberOfChildNode,getX_Value_right,getY_Value_right,getZ_Value_right,parrentNode,"infeasible")
                
                else :
                    self.node.setNodesRight(numberOfChildNode,getX_Value_right,getY_Value_right,getZ_Value_right,parrentNode)


                getX_Value_left = int(getParentValue[getMaxValue]) + 1

                getY_Value_left = (Rules.getInstance().totalValue_firstRule - (Rules.getInstance().valueOfX_firstRule * getX_Value_left)) / Rules.getInstance().valueOfY_firstRule

                getZ_Value_left = (Rules.getInstance().valueOfX * getX_Value_left) + (Rules.getInstance().valueOfY * getY_Value_left)

                if getZ_Value_left > self.node.getValueOfSelectedNode(0)['z'] :
                    self.node.setNodesLeft(numberOfChildNode + 1,getX_Value_left,getY_Value_left,getZ_Value_left,parrentNode,"infeasible")
                
                else :
                    self.node.setNodesLeft(numberOfChildNode + 1,getX_Value_left,getY_Value_left,getZ_Value_left,parrentNode)

            elif startGetConstraintFrom == "y":
                getY_Value_right = int(getParentValue[getMaxValue]) + 1

                getX_Value_right = (Rules.getInstance().totalValue_secondRule - (Rules.getInstance().valueOfY_secondRule * getY_Value_right)) / Rules.getInstance().valueOfX_secondRule

                getZ_Value_right = (Rules.getInstance().valueOfX * getX_Value_right) + (Rules.getInstance().valueOfY * getY_Value_right)

                if getZ_Value_right > self.node.getValueOfSelectedNode(0)['z'] :
                    self.node.setNodesRight(numberOfChildNode,getX_Value_right,getY_Value_right,getZ_Value_right,parrentNode,"infeasible")
                
                else :
                    self.node.setNodesRight(numberOfChildNode,getX_Value_right,getY_Value_right,getZ_Value_right,parrentNode)


                getY_Value_left = int(getParentValue[getMaxValue])

                getX_Value_left = (Rules.getInstance().totalValue_firstRule - (Rules.getInstance().valueOfY_firstRule * getY_Value_left)) / Rules.getInstance().valueOfX_firstRule

                getZ_Value_left = (Rules.getInstance().valueOfX * getX_Value_left) + (Rules.getInstance().valueOfY * getY_Value_left)

                if getZ_Value_left > self.node.getValueOfSelectedNode(0)['z'] :
                    self.node.setNodesLeft(numberOfChildNode + 1,getX_Value_left,getY_Value_left,getZ_Value_left,parrentNode,"infeasible")
                
                else :
                    self.node.setNodesLeft(numberOfChildNode + 1,getX_Value_left,getY_Value_left,getZ_Value_left,parrentNode)
            
            if getZ_Value_right > getZ_Value_left :

                if self.node.getValueOfSelectedNode(numberOfChildNode + 1)['status'] != "infeasible" and self.number_of_digits_post_decimal(getZ_Value_left) != None:
                    parrentNode = numberOfChildNode  + 1
                else :
                    if self.node.getValueOfSelectedNode(numberOfChildNode)['status'] != "infeasible" and self.number_of_digits_post_decimal(getZ_Value_right) != None:
                        parrentNode = numberOfChildNode
                    else :
                        doLoopForCreateTree = False
                        break
                
            elif getZ_Value_right < getZ_Value_left:

                if self.node.getValueOfSelectedNode(numberOfChildNode)['status'] != "infeasible" and self.number_of_digits_post_decimal(getZ_Value_right) != None:
                    parrentNode = numberOfChildNode
                else :
                    doLoopForCreateTree = False
                    break
            
            numberOfChildNode = numberOfChildNode + 2

            
            
            if startGetConstraintFrom == "x" :
                startGetConstraintFrom = "y"
            elif startGetConstraintFrom == "y":
                startGetConstraintFrom = "x"
            
            # if numberOfChildNode == 7 :
            #     doLoopForCreateTree = False
            #     break
            
            


        self.node.showDetail()
    
    def number_of_digits_post_decimal(self,x):  
        count = 0  
        residue = x -int(x)  
        if residue != 0:  
            multiplier = 1  
            while not (x*multiplier).is_integer():  
                count += 1  
                multiplier = 10 * multiplier  
            return count


if __name__ == "__main__":
    method = BranchAndBound()
    method.doCalculation()