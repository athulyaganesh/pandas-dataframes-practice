import pandas as pd
import numpy as np
'''
Instructions to run program:
1) Please ensure you have library openpyxl library (through pip3)
2) Make sure you have the .xlsx file and this .py file in the same directory
3) run using python main.py
Thats it! This code is functional for any number of customers, and any number of entries! 
'''

df = pd.read_excel('data.xlsx') # Read from the excel file 
df_list = np.split(df, df[df.isnull().all(1)].index) #create different dataframes for different customers 
output={'Customer Id':[],'MM/YYYY':[],'Minimum Balance':[],'Maximum Balance':[],'Ending Balance':[]} #output dictionary 
for i in range(len(df_list)): #iterate through each dataframe
    customerX = df_list[i].dropna()
    customerX['Running Balance'] = customerX['Amount'].cumsum() #creatin a cumulative sum column 

    customerID = str(customerX['Customer Id'].iloc[0]) #getting the customer id
    mini = str(customerX['Running Balance'].min()) #finding minimum balance
    maxi = str(customerX['Running Balance'].max()) #finding maximum balance
    endi = str(customerX['Running Balance'].iloc[-1]) #finding the ending balance

    fulldate = str(customerX['Date'].iloc[0].month)+"/"+str(customerX['Date'].iloc[0].year) #date formatting 

    #add all to the output dictionary 
    output['Customer Id'].append(customerID)
    output['MM/YYYY'].append(fulldate)
    output['Minimum Balance'].append(mini)
    output['Maximum Balance'].append(maxi)
    output['Ending Balance'].append(endi) 


output = pd.DataFrame.from_dict(output) #convert to dataframe and print
print(output)

