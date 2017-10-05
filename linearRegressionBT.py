#coding: utf8
from __future__ import division, print_function, unicode_literals
import numpy as np 
from numpy import genfromtxt
import csv
import pickle
import pandas as pd

class LinearRegression(object):
    def __init__(self):
        wT= []
    def load_raw_data(self, path, skip=1):
        raw_data = genfromtxt(path, delimiter=',', skip_header=skip, dtype=float)
        return raw_data
    def split_raw_data(self, raw_data, ratio=0.8):
        size = raw_data.shape[0]
        index = size*ratio
        train_set = raw_data[0:index,:]
        test_set = raw_data[index:,:]
        model_set = [train_set, test_set]
        return model_set
    def fit(self, data_set, target_set):
        #data_set(n,d)
        #target_set(n,1)
        data_set_bar = self.bar_data(data_set)#(n,d+1)
        A = np.dot(data_set_bar.T, data_set_bar)#xT.x(d+1,d+1)
        b = np.dot(data_set_bar.T, target_set)#xT.y(d+1,1)
        self.wT = np.dot(np.linalg.pinv(A),b)#A+.b(d+1,1)
    def save_model(self, path):
        model_path = open(path,'wb')
        pickle.dump(self.wT, model_path)
        model_path.close()
    def load_model(self, path):
        model = open(path, 'r')
        self.wT = pickle.load(model)
        model.close()
    # mo rong vector du lieu 
    def bar_data(self, data):
        one = np.ones((data.shape[0],1))
        data_bar = np.concatenate((one, data), axis=1)
        return data_bar
    def predict(self, predict_data):
        predict_data_bar = self.bar_data(predict_data)
        predict = np.dot(predict_data_bar, self.wT)
        print(predict)
        return predict
   
if __name__ == '__main__':
    ln = LinearRegression()
    data = ln.load_raw_data("1-prostate-training-data.csv")
    data_set = data[:,:-1]
    target_set = data[:,-1]
    ln.fit(data_set, target_set)
    ln.save_model("model.txt")
    del ln
    ln1 = LinearRegression()
    ln1.load_model("model.txt")
    test_data = ln1.load_raw_data("20141869-test.csv", skip=0)
    test = test_data[:,:-1]
    predict = ln1.predict(test)
    predict = np.array([predict]).T
    output = np.concatenate((test, predict), axis=1)
    output = np.array(output, dtype='f8')
    # save output predict ra file
    op_predict = pd.DataFrame(output)
    op_predict.to_csv("20141869.csv")
    
    