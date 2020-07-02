# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

from faker import Faker

faker = Faker()

df=pd.DataFrame(columns={'Name','Address','DOB','credit_card_number'},index=range(0,201))

for index,row in df.iterrows():
    df['Name'].iloc[index]=faker.name()
    df['Address'].iloc[index]=faker.address()
    df['DOB'].iloc[index]=faker.date_of_birth()
    df['credit_card_number'].iloc[index] =faker.credit_card_number()
    
df.to_csv('data.csv')
    
    
    
    
txt=faker.text()*10

txt.split('/n')