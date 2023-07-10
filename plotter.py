import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import re 

df= pd.read_csv("Pokemon.csv") 
top_frame = df.head(5) #Reads the first five items at the top 
bottom_frame = df.tail(5) # Reads the first five items from the bottom 

columns = df.columns #Returns a list of the columns  

get_names = df["Name"] 

name_total_hp = df[["Name" , "Total" , "HP"]]

# Get item at a particular index 
item_one = df.iloc[1] 

#Get items within an index range but the last index is not inclusive 
any_item = df.iloc[1:5]

specific_item = df.iloc[0 , 5] #Get the data at row 2 and column 4 
print(specific_item)
#loop over each item and do someting 

for index,row in df.iterrows():
    #print(row) 
    # Get an item by key 
    name = row["Name"] 
    print(index , name)
    if index == 2: break 

# select a specific rows with particular matching data 
fire = df.loc[df["Type 1"] == "Fire"] 

describe = df.describe() #Performs and return descriptive statistics results 

sorter = df.sort_values(["Name"] , ascending=False) #This change will not affect our df 

# print(df.head(5)) 
# print(sorter.head(5)) 

#Add new column 

df["Summation"] = df.iloc[:,5:11].sum(axis=1) 



#Save to csv 
# df.to_csv("example.csv" , index=False)

#Filtering 

filtered = df.loc[(df["Type 1"] == "Fire") & (df["Total"] > 400) & (df["Type 2"] =="Dragon") ] 

filtered.reset_index(drop=True , inplace=True) #Resets the index and uses newer ones 



#Searching for strings 
filtered = df.loc[(df["Name"].str.contains("Mega"))] #Returns names that has Mega 

filtered = df.loc[(df["Name"].str.contains("^pi[a-z]*" , flags=re.I , regex=True))] 


#Modify values conditionally 

filtered.loc[(df["Name"] == "Pidgeot" , "Type 2")] = "Number" 
print(filtered)


