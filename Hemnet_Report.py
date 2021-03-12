#Importing the library
from fpdf import FPDF

#importing all the libraries from Hemnet_Plots
from Hemnet_Plots import *

#Defining the variables from the imported functions 
min_date=min_date()
max_date=max_date()
properties=total_properties()
mean_price=mean_price()
top_county=top_county()
avg_increase=average_increase()
second_top_county=second_top_county()
second_average_increase=second_average_increase()
top_broker=top_broker()
top_turnover=top_turnover()

#Defining the Width and Heigth
HEIGHT=270
WIDTH=210

#Creating the class

class PDF(FPDF):
    def create_title(self):
        self.set_font('Times','B',20)
        #fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        self.image('Hemnet Band.png',x=65,y=5,w=WIDTH-130,h=18)
        self.ln(20)
        self.cell(190, 10, 'Summary',align='C')
        self.set_font('Times','',10)
        self.ln(5)
        self.cell(190,17,f'There were more than {properties} properties purchased across Sweden between {min_date} and {max_date}.',align='C')
        self.ln(7)
        self.cell(190,17,f'During this period of time the average final price was SEK {mean_price}.',align='C')
        self.ln(7)
        self.cell(190,17,f'{top_county} was the region with the highest average price increase ({avg_increase} %) followed by {second_top_county} ({second_average_increase} %).',align='C')
        self.ln(7)
        self.cell(190,17,f'{top_broker} is the broker that generated the most revenue with SEK {top_turnover} in revenues',align='C')

        
    def create_report(self,filename='Hemnet Report.pdf'):
        self.add_page()
        self.create_title()
        
        transactions_evolution('Transactions Evolution.png')
        self.image('Transactions Evolution.png',10,80,w=200)
        self.ln(30)
        box_plots('boxplots.png')
        self.image('boxplots.png',10,160,w=200)
        self.add_page()
        self.ln(5)
        final_price_evolution('Average Final Price.png')
        self.image('Average Final Price.png',10,10,w=200)
        self.ln(5)
        final_price_per_county('Bar Plots - Top 3 Counties.png')
        self.image('Bar Plots - Top 3 Counties.png',10,90,w=200)
        self.ln(10)
        top_10_brokers('Top 10 Brokers.png')
        self.image('Top 10 Brokers.png',20,182,h=110,w=140)
        
        
        
        
        self.output(filename)
        
            
pdf=PDF()
pdf.create_report()
        