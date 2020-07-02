# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:36:08 2020

@author: PraveenKumar
"""

import pandas as pd
from fpdf import FPDF
from faker import Faker
import os
from pdf2image import convert_from_path

faker = Faker()

df=pd.DataFrame(columns={'Name','Address','DOB','credit_card_number'},index=range(0,201))

for index,row in df.iterrows():
    df['Name'].iloc[index]=faker.name()
    df['Address'].iloc[index]=faker.address()
    df['DOB'].iloc[index]=faker.date_of_birth()
    df['credit_card_number'].iloc[index] =faker.credit_card_number()

class CustomPDF(FPDF):
    
    def header(self):
        # Set up a logo
        self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        
        # Add an address
        self.cell(100)
        self.cell(0, 5, 'towardzDataScience', ln=1)
        self.cell(100)
        self.cell(0, 5, 'Bangalore,Karnataka', ln=1)
        self.cell(100)
        self.cell(0, 5, 'India', ln=1)
        
        # Line break
        self.ln(20)
        
    def footer(self):
        self.set_y(-10)
        
        self.set_font('Arial', 'I', 8)
        
        # Add a page number
        page = 'Thanks fo business with us !!' + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')
        
def create_pdf(pdf_path,Name,credit_card_number,DOB,Address):
    pdf = CustomPDF()
    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    Name,credit_card_number,DOB,Address=Name,credit_card_number,DOB,Address
    
    pdf.cell(0, 10, txt="Name : {}".format(Name), ln=1)
    pdf.cell(0, 10, txt="DOB :{}".format(DOB), ln=1)
    pdf.set_y(45.00125)
    pdf.cell(80)
    pdf.cell(0, 10, txt="Credit_card_number :{}".format(credit_card_number), ln=1)
    pdf.set_y(55.00125)
    pdf.cell(80)
    pdf.cell(0, 10, txt="Address :{}".format(Address), ln=1)
    # Line break
    pdf.ln(20)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    # Line break
    pdf.ln(20)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf.cell(0, 10, txt=faker.text(), ln=1)
    pdf_path='./Img_data/'+pdf_path
    
    pdf.output(pdf_path)
    imgFile=convert_from_path(pdf_path,poppler_path='C:/Apps/poppler/bin')
    imgPath=pdf_path.replace('.pdf','.png')
    print('imgPath',imgPath)
    for img in imgFile:
        img.save(imgPath, "PNG")
    
    
if __name__ == '__main__':
    cnt=0
    for index, row in df.iterrows():
        Name=row['Name']
        credit_card_number=row['credit_card_number']
        DOB=row['DOB']
        Address=row['Address']
        create_pdf('Invoice_%s.pdf' % cnt,Name,credit_card_number,DOB,Address)
        cnt+=1
        
        
        
        
        
        











