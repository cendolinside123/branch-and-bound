#!/usr/bin/env python3

import os, sys
sys.path.insert(0, os.path.join(sys.path[0], 'Controller'))

from BranchAndBound import BranchAndBound

if __name__ == "__main__":
    run = BranchAndBound()
    run.doCalculation()