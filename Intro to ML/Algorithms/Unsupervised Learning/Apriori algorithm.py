import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = [
        ['I1',['G1', 'G2', 'G5', 'G3']],
        ['I2',['G2', 'G4', 'G2', 'G4', 'G2', 'G4']],
        ['I3',['G2', 'G3', 'G2']],
        ['I4',['G1', 'G2', 'G4', 'G1', 'G2', 'G5']],
        ['I5',['G1', 'G3', 'G1', 'G2', 'G3', 'G5']],
        ['I6',['G2', 'G3', 'G1', 'G2', 'G5', 'G3', 'G2']],
        ['I7',['G1', 'G3', 'G3', 'G2']],
        ['I8',['G1', 'G2', 'G3', 'G5']],
        ['I9',['G1', 'G2', 'G3', 'G5']],
        ['I10',['G1', 'G2', 'G5', 'G3', 'G3']],
        ['I11',['G2', 'G4', 'G3', 'G3']],
        ['I12',['G2', 'G3', 'G2', 'G5', 'G3', 'G2']],
        ['I13',['G1', 'G2', 'G4']],
        ['I14',['G1', 'G3', 'G1', 'G2', 'G5']],
        ['I15',['G2', 'G3', 'G4', 'G2', 'G4']],
        ['I16',['G1', 'G3', 'G4', 'G2', 'G4']],
        ['I17',['G1', 'G2', 'G3', 'G5', 'G1', 'G2', 'G5']],
        ['I18',['G1', 'G2', 'G3', 'G1', 'G2']],
        ['IЯ9',['G1', 'G2', 'G3', 'G5']],
        ['I20',['G1', 'G2', 'G3', 'G5']]
        ]



