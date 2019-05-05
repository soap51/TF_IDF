import math
def computeTF(wordDict):
    tfDict = {}
    for text in wordDict.split():
        if(tfDict.get(text)== None):
            tfDict[text] = 1
        else:
            tfDict[text] = tfDict[text] + 1 
    for key , value in tfDict.items():        
        tfDict[key] = tfDict[key]/len(wordDict.split())      
    return tfDict
    
def computeIDF(documents):
    idfDict = {}
    for document in documents:
        for text in document.split():
            if(idfDict.get(text)== None):
                idfDict[text] = 1
            else:
                idfDict[text] = idfDict[text] + 1
    for key , value in idfDict.items():
        idfDict[key] = math.log10(len(documents) / idfDict[key])    
    return idfDict
    
    
    
tf_idf_s1 = computeTF("The car is driven on the road")
tf_idf_s1 = computeTF("The truck is driven on the highway")
idf = computeIDF(["The car is driven on the road", "The truck is driven on the highway"])