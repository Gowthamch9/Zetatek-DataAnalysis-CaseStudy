import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Pandas
##Load the data
sales_data= pd.read_csv("D:\\sales_data.csv")

#Marplotlib
#Stacked bar chart
stacked=sales_data.groupby(["Product_Category","Customer_Type"])["Sales_Amount"].sum().unstack()
stacked.plot(kind='bar',
             stacked=True,
             colormap="coolwarm",
             figsize=(8,6))
plt.title("Stacked sales by category and Customer type")
plt.xlabel("Product category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Linechart of Region sales
sales_data["Sale_Date"]= pd.to_datetime(sales_data["Sale_Date"])
region_sales=sales_data.groupby(["Sale_Date","Region"])["Sales_Amount"].sum().unstack()
region_sales.plot(kind='line',
                 title="Regional Sales", 
                 ylabel="Sales Amount",
                 xlabel="Date",
                 color="Green",
                 figsize=(12,6)) #figsize=(width, height)
plt.tight_layout() #It automatically adjusts the spacing of subplots and prevents overlapping
plt.show()


#Linechart 
sales_data["Sale_Date"]= pd.to_datetime(sales_data["Sale_Date"])
daily_sales=sales_data.groupby("Sale_Date")["Sales_Amount"].sum()
daily_sales.plot(kind='line',
                 title="Daily Sales", 
                 ylabel="Sales",
                 xlabel="Date",
                 color="Red",
                 figsize=(10,6)) #figsize=(width, height)
plt.tight_layout() #It automatically adjusts the spacing of subplots and prevents overlapping
plt.show()


payment_share= sales_data.groupby("Payment_Method")["Sales_Amount"].sum()
payment_share.plot.pie(autopct="%1.1f%%", figsize=(6,6))
plt.title("Total sales by each Payment Method")
plt.ylabel("")  # Hides the default ylabel
plt.show()

#Seaborn
#Creating Barplot
sns.barplot(x="Product_Category", y="Quantity_Sold", data=sales_data, estimator=np.sum,palette="coolwarm" )
plt.title("Total quantity sold per category")
plt.xlabel("Product Category")
plt.ylabel("Total quantity")
plt.xticks(rotation=45)
plt.show()

#Creating boxplot
sns.boxenplot(x="Region",y="Sales_Amount", data=sales_data, palette="Set2")
plt.title("Sales per Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.show()

#Creating Histogram
sns.histplot(sales_data["Sales_Amount"],kde=True, color='blue')
plt.title("Sales amount distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()


# Numpy 
print("Mean Sales:",np.mean(sales_data["Sales_Amount"]))
print("Sandard Deviation:", np.std(sales_data["Sales_Amount"]))
sales_data["Sales_Normalized"]=(sales_data["Sales_Amount"]- np.min(sales_data["Sales_Amount"]))/(np.max(sales_data["Sales_Amount"])- np.min(sales_data["Sales_Amount"]))

## ckeck the basics
print(sales_data.head()) ##first few rows
print(sales_data.shape) ## the shape of the data set
print(sales_data.info()) ## data type and any null entries
print(sales_data.columns) ## column names of the data set

column_names= list(sales_data.columns)
print(column_names) ## column names using list function

##the number of unique regions
total_rows= len(sales_data)
print(total_rows) 
unique_regions= sales_data['Region'].nunique
print(f"Total rows:{total_rows},Unique Regions:{unique_regions}")

##total sales amount
total_sales_amount= sales_data["Sales_Amount"].sum()
print(f"Total Sales amount:{total_sales_amount}")

##total sales in each region
region_total_sales= sales_data.groupby("Region")["Sales_Amount"].sum()
print(f"Total Sale per region :\n{region_total_sales}")

##total sales in each category
Category_sales= sales_data.groupby("Product_Category")["Sales_Amount"].sum()
print(Category_sales)

##total discount
total_discount= sales_data["Discount"].sum()
print(f"Total Discount:{total_discount}")

##total sales by each Sales person
Rep_name=sales_data.groupby("Sales_Rep")["Sales_Amount"].sum().sort_values(ascending=False)
print(f"Top Sales Persons: \n{Rep_name}")

## Region wise Average discount
Regional_discount=sales_data.groupby("Region")["Discount"].mean()
print(Regional_discount)

## Category wise Average discount
Category_discount=sales_data.groupby("Product_Category")["Discount"].mean()
print(Category_discount)

##the type of customers
Customer_type= sales_data["Customer_Type"].value_counts()
print(Customer_type)

##Total number of payments by each payment method
payment_method=sales_data["Payment_Method"].value_counts()
print(f"Number of payments by each payment method: {payment_method}")

## Total amount of payment by each payment method
payment_type= sales_data.groupby("Payment_Method")["Sales_Amount"].sum()
print(f"Total payment by each payment method:{payment_type}")

##total sales using for loop
total_sales=0
for amount in sales_data["Sales_Amount"]:
    total_sales+= amount
print(total_sales)

##total quantity sold using numpy
quantity_arrey=np.array(sales_data["Quantity_Sold"])
total_quantity = np.sum(quantity_arrey)
print(total_quantity)

##the profit margin per row
sales_data["Profit_margin"]= sales_data["Unit_Price"]- sales_data["Unit_Cost"]
print(sales_data[["Product_ID","Profit_margin"]].head())

##clasifying high vs low margin
sales_data["Margin_Level"]= np.where(sales_data["Profit_margin"]>=100, "High Margin", "Low Margin")
print(sales_data[["Product_ID","Profit_margin","Margin_Level"]].head())

