from fastapi import FastAPI,HTTPException,Path
import json
from fastapi.responses import JSONResponse
from pyd.pydantic_info import userinput
from model.pick import model,version
from predict.predictions import predict_output
app=FastAPI()
@app.get("/")
def home():
    return {"message":"satisfaction score predict api"}

@app.get("/health")
def health():
    return {"version":version}


#post requiest
@app.post("/predict")
def create_pred(data:userinput):
    input_df={
     "age":data.age,
     "service":data.service,
     "arrival_year":data.arrival_year,
     "arrival_month":data.arrival_month,
     "arrival_day":data.arrival_day,
     "departure_year":data.departure_year,
     "departure_month":data.departure_month,
     "departure_day":data.departure_day }

    try:
       prediction=predict_output(input_df)
       return JSONResponse (status_code=200,content={"my predict satisfaction score":prediction})
    except Exception as e:
        return JSONResponse(status_code=404,content=str(e))
