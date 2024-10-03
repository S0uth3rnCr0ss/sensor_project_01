from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url = "mongodb+srv://Biswal:armag3dd0n@cluster0.148sx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url)

database_name = "Sensor_data"
Collection_name = "Wafer_Fault"

#dataset path
df = pd.read_csv("C:\Users\abhin\OneDrive\Desktop\Python\projects\cv_projects\fault_Detection\fault_detection\notebook\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

#converting list into json
json_record = list(json.loads(df.T.to_json()).values())

client[database_name][Collection_name].insert_many(json_record)