import json
import pickle
import os
import numpy as np
import pandas as pd

__data_columns = None
__model = None
__credit_mix =None
__occupation = None
__preprocessor = None

def get_estimated_price(
            var,occupation,credit_mix
        ):
    print('inside')
    try:
        occu_index = __data_columns.index(occupation.lower())
        cmix = __data_columns.index(credit_mix.lower())
    except:
        occu_index=-1
        cmix=-1
    df =pd.DataFrame()
    x=np.zeros(len(__data_columns))
    for i in range(len(var)):
        x[i]=var[i]
    if occu_index>=0:
        x[occu_index]=1
    if cmix>=0:
        x[cmix]=1
    #print("***********************")
    #print(x)
    clm = list(__data_columns)
    df = pd.DataFrame([x],columns=clm)
    #df.columns=__data_columns
    #print(*df.columns)
    #df1=__preprocessor.transform(df)
    z=__model.predict([x])[0]
    dict =['Poor','Standard','Good']
    return dict[z]
    
def get_credit_mix():
    return __credit_mix
def get_occupation_names():
    return __occupation

def load_saved_artifacts():
    print("Loading saved artifacts")
    global __data_columns
    global __credit_mix
    global __occupation
    
    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __occupation =__data_columns[17:33]
        __credit_mix = __data_columns[34:]
    global __model
    if __model is None:
        with open("server/artifacts/credit_ccore_classifier_model.pickle", 'rb') as f:
            __model = pickle.load(f)

    global __preprocessor
    if __preprocessor is None:
        with open("server/artifacts/preprocessor.pickle", 'rb') as f:
            __preprocessor = pickle.load(f)
    print("Artifacts loading completed")

if __name__ =="__main__":
    load_saved_artifacts()
    print(get_estimated_price(np.arange(35),2,3))