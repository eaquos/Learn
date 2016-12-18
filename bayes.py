"""
written by Charlie Tahar / December 2016

given
pS = P(C) Probability of something happens
pTP = True Positive (Sensitivity), P(Pos|C) Probability of the test result is Positive when something really there
pFN = False Negative (Specitivity), P(Neg|~C) Probability of the test result is Negative when something isn't there
we could calculate the Positive and Negative of the test probability
and get the pPos and pNeg value
Using bayes rule, we could get the probability of a test giving True Positive or False Negative

*Additional
True Positive = The test show True and Right
False Positive = The test show False and Wrong

True Negative = The test show True and Wrong
False Negative = The test show False and Right
"""
#General Definition
def q(p):
    return 1-p
#End of General Definition

#Calculate the positive probability
def pPos(pS,pTP,pFN):
    return (pS*pTP + q(pS)*q(pFN))

#Calculate the negative probability
def pNeg(pS,pTP,pFN):
    return (pS*q(pTP) + q(pS)*pFN)

#Calculate the True Positive probability
def bTP(pS,pTP,pPos):
    return (pS*pTP/pPos)

def bFP(pS,pTP,pNeg):
    return (pS*q(pTP)/pNeg)

#Main program
def bayes():
    #Description and input
    print("This program will calculate Bayes Rule for simple cases")
    print("Please enter the Probability of the Case is True (pS): ")
    pS = float(input())
    print("Please enter the Probability of the Test is True Positive (Sensitivity, p(Pos|S)): ")
    pTP = float(input())
    print("Please enter the Probability of the Test is False Negative (Specitivity, p(Neg|~S)): ")
    pFN = float(input())

    #Calculate process
    p_S = q(pS)
    pFP = q(pTP)
    pTN = q(pFN)
    pPositive = pPos(pS,pTP,pFN)
    pNegative = pNeg(pS,pTP,pFN)
    bTruePositive = bTP(pS,pTP,pPositive)
    bFalsePositive = bFP(pS,pTP,pNegative)
    #End of Calculate process

    #Output
    print( "Probability of Case is True: ", round(pS,2))
    print( "Probability of Case is False: ", round(p_S,2))
    print( "Probability of Test result True Positive (The test show True and Right): ", round(pTP,2))
    print( "Probability of Test result False Positive (The test show False and Wrong): ", round(pFP,2))
    print( "Probability of Test result True Negative (The test show True and Wrong): ", round(pTN,2))
    print( "Probability of Test result False Negative (The test show False and Right): ", round(pFN,2))
    print()
    print( "Probability of Test is Positive: ", round(pPositive,2))
    print( "Probability of Test is Negative: ", round(pNegative,2))
    print()
    print( "Probability of Case True when the Test is Positive : ", round(bTruePositive,2))
    print( "Probability of Case False when the Test is Positive: ", round(bFalsePositive,2))
    return None
