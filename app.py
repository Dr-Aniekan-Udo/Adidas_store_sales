import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# read the data from excel file
df = pd.read_excel(r"C:\Users\anibr\GITHUB HOME\streamlit_learning\Adidas.xlsx")
#set up the page appearnace for streamlit
st.set_page_config(layout = "wide")
#let's write the markdown setup
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html= True)
#let's import our image \
image = Image.open(r'C:\Users\anibr\GITHUB HOME\streamlit_learning\adidas-logo.jpg')

#let's create columns  where our charts will be displayed
col1, col2 = st.columns([0.1,0.9])

#edit each columnsto appropriate appearance
with col1:
    st.image(image,width = 100)
#let's write an html title
html_title = """
    <style>
    .title-test{
    font-weight:bold;
    padding:5px;
    border-radius:6px}
    </style>
    <center><h1 class = "title-test">Adidas Interactive Sales Dashboard</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html = True)
#create next batch of columns which we'll use for the charts
col3,col4,col5 =st.columns([0.1,0.45,0.45])
#build the columns components
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last Updated \n {box_date}")
with col4:
    fig1 = px.bar(df, x= "Retailer", y = "TotalSales", labels={"Totalsales" : "Total Sales {$}"},
                 title = "Total Sales by Retailer", hover_data = ["TotalSales"],
                 template="gridon", height = 500)
    st.plotly_chart(fig1,use_container_width = True)

#let's create drop down
_, view1, dwn1, view2, dwn2 = st.columns([0.15,0.30,0.10,0.30,0.10])
# under the col4 we want to create an expandable column 
# which displays the value of sales for each retailer siung the view1
with view1:
    expander = st.expander("Retail wise Sales")
    data = df[["Retailer","TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)

# To make the data downloadable we can write that using the dwn1 variable
with dwn1:
    st.download_button("Get data", data = data.to_csv().encode("utf-8"),
                       file_name= "sales_by_retailers.csv", mime="text/csv")
#let's create another chatrt for the right side using column 5 which we created earlier
#before then let's extract month and year from tghe invoice-date column of our data
# we will use this extract to plot a line gragh in our next chart

df["Month_Year"] = df["InvoiceDate"].dt.strftime("%B %Y")
df["Year_Index"] = df["InvoiceDate"].dt.strftime("%Y %m")

result = df.groupby(by = ["Month_Year","Year_Index"])["TotalSales"].sum().reset_index()
result = result.sort_values("Year_Index")
# reset index allow you to reset index, 
#this is because our extract will be save as new dataframe in result
# we can now use the dataframe to do a chart
with col5:
    fig2 = px.line(result, x = "Month_Year", y = "TotalSales", title = "Total sales over time",
                   template = "gridon")
    st.plotly_chart(fig2, use_container_width = True)

#let's create expander and get data for thi chart as well
with view2:
    expander = st.expander("Monthly sales")
    data = result
    expander.write(data)
#let,s create the download button and format, always remember to mention the encoding
# this will remove the bad characters from the dateset
with dwn2:
    st.download_button("Get data", data = result.to_csv().encode("utf-8"),
                       file_name= "Monthly_sales.csv", mime="text/csv")
# let's create a divider before create the next set of charts
st.divider()

result1 = df.groupby(by = "State")[["TotalSales", "UnitsSold"]].sum().reset_index()
# we will create two chart from two souces the total sale(barchart) and the unit sold(linechart)
# we will create a chart with unit sold as the y-axis in a secondarty chart
# we will create a dual exit chart
# let's add the unit sold as line chart on a secondary y-axis

# we will first create graphic object inatnace and feed it with our data
fig3 = go.Figure()
fig3.add_trace(go.Bar(x = result1["State"], y = result1["TotalSales"], name = "Total Sales"))
fig3.add_trace(go.Scatter(x = result1["State"], y = result1["UnitsSold"], mode = "lines",
                          name = "Unit sold", yaxis ="y2"))
# updating the layout
fig3.update_layout(
    title = "Total Sales and units sold by state",
    xaxis = dict(title = "State"),
    yaxis = dict(title = "Total Sales", showgrid = False),
    yaxis2 = dict(title = "UnitsSold", overlaying ="y", side = "right"),
    template = "gridon",
    legend = dict(x=1, y=1)
)
# let's create a column and insert our graph
_,col6 = st.columns([0.1,0.9])

with col6:
    st.plotly_chart(fig3, use_container_width= True)

# let's create an expander and download for this new graph too
_, view3, dwn3 = st.columns([0.3, 0.35, 0.35])

with view3:
    expander = st.expander("view sales by unit sold")
    expander.write(result1)
with dwn3:
    st.download_button("Get Data", data = result1.to_csv().encode("utf_8"),
                       file_name= "sales_by_Unitsold.csv", mime = "text/csv")
    
#let's divide to another section again
st.divider()

# let's create a tree map chart, which can help us view sles based on region and city
# so we first create a column for it
_, col7 = st.columns([0.1,0.9])

#let's group the total sales based on city and region
treemap = df[["Region", "City", "TotalSales"]].groupby( by = ["Region", "City"])["TotalSales"].sum().reset_index()

# To format our totalsales so that it's shrink to millions, 
# let create a function to divide it by 1000000
def format_sales(value):
    if value >= 0:
        return "{:.2f} Million".format(value/1000000)
treemap["TotalSales(millions)"] = treemap["TotalSales"].apply(format_sales)

#create a tree map
fig4 = px.treemap(treemap, path=["Region", "City"], values = "TotalSales",
                  hover_data= ["TotalSales(millions)"],
                  hover_name = "TotalSales(millions)",
                  color = "City", height = 700, width = 600)
fig4.update_traces(textinfo = "label+value")

with col7:
    st.subheader(" Total sales by Region and City in Treemap :point_down:")
    st.plotly_chart(fig4,use_container_width=True)

# let's create a function to download all the dataset, and place it under the treemap
_,view4, dwn4 = st.columns([0.3, 0.35, 0.35])

with view4:
    result2 = df[["Region","City","TotalSales"]].groupby(by = ["Region","City"])["TotalSales"].sum()
    expander = st.expander("view sales data for Totalsales by Region and City")
    expander.write(result2)

with dwn4:
    st.download_button("Get Data", data = result2.to_csv().encode("utf-8"),
                       file_name = "Sales_region_City", mime = "text/csv")
# to allow viewers to get the whole raw data
# we create a drop down for that and a download button
    
st.divider()

_,view5,dwn5 = st.columns([0.1,0.9,0.1])

with view5:
    expander = st.expander("view raw adidas sales data")
    expander.write(df)
with dwn5:
    st.download_button("Get Raw Data", data = df.to_csv().encode("utf-8"),
                       file_name = "Adidas_rawdata.csv", mime = "text/csv")
st.divider()