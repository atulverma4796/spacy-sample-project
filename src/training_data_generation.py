text = 'POLICY NUMBER:  1-TPM -NY-17-01234898  COMMERCIAL GENERAL LIABILITY   CG 20 37 04 13   THIS ENDORSEMENT CHANGES THE POLICY.  PLEASE READ IT CAREFULLY.  CG 20 37 04 13  © Insurance Services  Office, In c., 2012  Page 1 of 1   ADDITIONAL INSURED – OWNERS, LESSEES OR  CONTRACTORS – COMPLETED OPERATIONS  This endorsement modifies insurance provided under the following:  COMMERCIAL GENERAL LIABILITY COVERAGE PART PRODUCTS/COMPLETED OPERATIONS LIABILITY COVERAGE PART   SCHEDULE  Name Of Additional Insured Person(s)  Or Organiz ation(s)  Location And Description Of Completed Oper ations  As Required by Written Contract executed prior to any claim or “suit.”    As Required by Written Contract executed prior to any claim or “suit.”      Information required to complete this Schedule, if not shown above, will be shown in the Declarations.'


startText = 'Name Of Additional Insured Person(s)'
endText = 'Declarations.'

startindex = text.index(startText)
endindex = text.index(endText)
lengthOfEndText = len(endText)
endindex = endindex + lengthOfEndText
res = text[startindex: endindex]
print('startindex: ', startindex)
print('endindex: ', endindex)
print('res: ', res)