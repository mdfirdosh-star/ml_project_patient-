from typing import Dict,Annotated
from pydantic import BaseModel,Field

class userinput(BaseModel):
    age:Annotated[int,Field(...,description="enter the age",example=30)]
    service:Annotated[int,Field(...,description="enter the service",example=3)]
    arrival_year:Annotated[int,Field(...,description="enter the arrival_year",example=2025)]
    arrival_month:Annotated[int,Field(...,description="enter the arrival_month",example=2)]
    arrival_day:Annotated[int,Field(...,description="enter the arrival_day",example=15)]
    departure_year:Annotated[int,Field(...,description="enter the departure_year",example=2025)]
    departure_month:Annotated[int,Field(...,description="enter the departure_month",example=3)]
    departure_day:Annotated[int,Field(...,description="enter the departure_day",example=30)]
