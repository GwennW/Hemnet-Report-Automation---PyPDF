
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import math

df=pd.read_excel(r'C:\Users\Gwenn\Updated Hemnet Dataset.xlsx')



df['date updated']=df['date'].dt.strftime('%B-%Y')


def mean_price():
    meanprice=math.ceil(df['Final Price'].mean())
    return meanprice


def top_county():
    top_counties=df.groupby('County').mean()['Price Variation'].sort_values(ascending=False).head(5).reset_index()
    top_county=top_counties['County'][0]
    return top_county


def second_top_county():
    top_counties=df.groupby('County').mean()['Price Variation'].sort_values(ascending=False).head(5).reset_index()
    second_top_county=top_counties['County'][1]
    return second_top_county


def average_increase():
    top_counties=df.groupby('County').mean()['Price Variation'].sort_values(ascending=False).head(5).reset_index()
    avg_variation=top_counties['Price Variation'][0]
    avg_variation=math.ceil(avg_variation)
    return avg_variation


def second_average_increase():
    top_counties=df.groupby('County').mean()['Price Variation'].sort_values(ascending=False).head(5).reset_index()
    second_avg_variation=top_counties['Price Variation'][1]
    second_avg_variation=math.ceil(second_avg_variation)
    return second_avg_variation


def top_broker():
    top_10_brokers=df.groupby('Broker').sum()['Final Price'].sort_values(ascending=False).head(10).reset_index()
    topbroker=top_10_brokers['Broker'][0]
    return topbroker

def top_turnover():
    top_10_brokers=df.groupby('Broker').sum()['Final Price'].sort_values(ascending=False).head(10).reset_index()
    revenue=top_10_brokers['Final Price'][0]
    return revenue

    

def total_properties():    
    return df['Address'].count()

def min_date():
    #df['date']=df['date'].dt.strftime('%Y-%m')
    return df['date updated'].min()
    
def max_date():
    max_date=max(df['date']) 
    max_date_converted=max_date.strftime('%B-%Y')
    return max_date_converted
    

def box_plots(filename):
    plt.figure(figsize=(15,10))
    sns.boxplot(x='Rooms',y='Price per sqm',data=df,palette='Blues')
    plt.title('Price per sqm Variation depending on number of rooms \n',fontname='Cambria',fontsize=20,fontstyle='italic')
    plt.xticks(fontname='Cambria')
    plt.yticks(fontname='Cambria')
    plt.savefig('boxplots.png')
    
def transactions_evolution(filename):
    rolling_avg=df.groupby('date').count()['Address'].rolling(window=7).mean().reset_index()
    
    plt.figure(figsize=(20,8))
    plt.title('Total transactions - 7 days rolling average \n',fontsize=25,fontname='Cambria',fontstyle='italic')
    sns.lineplot(x='date',y='Address',data=rolling_avg,)
    plt.xticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.yticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.xlabel('')
    plt.ylabel('Total Transactions \n',fontsize=20,fontname='Cambria')
    plt.savefig('Transactions Evolution.png')
    
def final_price_evolution(filename):  
    final_price_rolling=df.groupby('date').mean()['Final Price'].rolling(window=7).mean().reset_index()
    plt.figure(figsize=(20,8))
    plt.title('Average Final Price July 2020 - January 2021 \n',fontsize=30,fontname='Cambria',fontstyle='italic')
    sns.lineplot(x='date',y='Final Price',data=final_price_rolling)
    plt.xticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.yticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.xlabel('')
    plt.ylabel('')
    plt.savefig('Average Final Price.png')
    
    
def final_price_per_county(filename):
    top_3=df.loc[(df['County']=='Stockholm County') | (df['County']=='Skåne County') | (df['County']=='Västra Götaland County')]
    plt.figure(figsize=(22,10))
    plt.title('Average Final Price July 2020 - January 2021 \n',fontsize=30,fontname='Cambria',fontstyle='italic')
    sns.barplot(x='Month',y='Final Price',data=top_3,hue='County',palette='mako',estimator=np.mean,ci=None)
    plt.legend(fontsize=14)
    plt.xticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.xlabel('Month',fontsize=25,fontname='Cambria')
    
    plt.ylabel('Average Final Price \n',fontsize=25,fontname='Cambria')
    plt.yticks(rotation=0,fontsize=18,fontname='Cambria')
    plt.savefig('Bar Plots - Top 3 Counties.png')
    
def top_10_brokers(filename):
    #brokers_df=df.groupby('Broker').sum()['Final Price'].sort_values(ascending=False).head(10).reset_index()
    plt.figure(figsize=(20,15))
    plt.title('Top Performing Brokers (cummulated revenues) \n',fontname='Cambria',fontsize=35,fontstyle='italic')
    #sns.barplot(x='Final Price',y='Broker',data=brokers_df,color='darkcyan')
    df.groupby('Broker').sum()['Final Price'].sort_values(ascending=True).tail(10).plot.barh(color='darkcyan')
    plt.ylabel('')
    plt.xlabel('Revenues',fontname='Cambria',fontsize=30)
    plt.yticks(fontname='Cambria',fontsize=30)
    plt.xticks(fontname='Cambria',fontsize=30)
    plt.tight_layout()
    plt.savefig('Top 10 Brokers.png')


