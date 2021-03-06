from time import strftime, gmtime

from gensim.models import Word2Vec
import numpy as np


class SentenceLevel:
    def __init__(self,cleanedData):
        self.sentences = cleanedData
        self.wordMatrix = self.getWordMatrix(cleanedData)
        self.saveMatrix = self.save(self.wordMatrix)
        self.docInput = self.getDocInput(self.wordMatrix)

    def getWordMatrix(self,cleanedData):
        model = Word2Vec(cleanedData, size=100, window=2, min_count=1)
        print(model)
        model.init_sims(replace=True)
        return model

    def save(self,model):
        timeStamp = strftime("%d%b_%H_%M_%S", gmtime())
        model.wv.save_word2vec_format('Output/WV' + timeStamp + '.word2vec.txt', binary=False)
        model.wv.save_word2vec_format('Output/WV' + timeStamp + '.word2vec.bin', binary=True)

    def getDocInput(self,model):
        docinput = np.zeros((len(self.sentences),10,100))
        for i in np.arange(len(self.sentences)):
            for j in np.arange(len(self.sentences[i])):
                docinput[i,j]=model.wv[self.sentences[i][j]]
        return docinput
