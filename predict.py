from preprocessing import Preprocessing,process_input
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
#using preprocessed data predict y and calculate accuracy 
X_train,X_test,y_train,y_test = Preprocessing()

print(X_train.shape,X_test.shape,len(y_train),len(y_test))

input_vector = process_input("This is the new answer abilities")
print(input_vector.shape)