import pandas as pd
from model.pick import model
def predict_output(user_df:dict):
    user_data=pd.DataFrame([user_df])
    predict_class=model.predict(user_data)[0]
    return predict_class