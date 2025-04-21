#STREAMLIT APP SALES
# ----

# To run app (put this in Terminal):
#   streamlit run 00_jumpstart/03_streamlit_jumpstart.py


# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# 1.0 Title and Introduction

st.title("Business Dashboard")
st.write(
    """
    This dashboard provides insights into sales, customers demographics, and product performance. Upload your data to get started.
    """
         )



# 2.0 Data Input

if st.button("Start Analysis"):
        st.header("Upload Business Data")
        
        # uploaded_file = "data/sales.csv"
        data = pd.read_csv("00_jumpstart/data/sales.csv")




# 3.0 App Body 
#  What Happens Once Data Is Loaded?



if uploaded_file:
    # data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data.head())

# * Sales insights

if uploaded_file is not None:

    
    # Sales Insights
    st.header('Sales Insights')
    
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        
        st.write("Sales Over Time:")
        
        fig = px.line(data, x = "sales_date", y = "sales_amount", title = "Sales Ovver Time")
        
        st.plotly_chart(fig)
        
    else:
        
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns.")

# * Customer Segmentation by Region

    st.header("Customer Segmentation")

    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("Customer Segmentation")
        fig = px.pie(data, names = "region", title = "Customer Segmentation", values = "sales_amount")
        st.plotly_chart(fig)
        
    else:
        
        st.warning("Please ensure your data has a 'region' column.")

# * Product Analysis

    st.header("Product Analysis")
    
    if 'product' in data.columns and 'sales_amount' in data.columns:
         
        st.write("Top Products by Sales")
        
        top_products_df = data \
            .groupby('product') \
            .sum('sales_amount') \
            .nlargest(10, 'sales_amount')
        
        fig = px.bar(
            data_frame = top_products_df, 
            x = top_products_df.index, 
            y = 'sales_amount',
            title = "Top Products by Sales Amount"
        )
        
        st.plotly_chart(fig)
        
    else:
        
        st.warning("Please ensure your data has 'product' and 'sales_amount' columns for Product Analysis.")
        
    
    selected_product = st.selectbox(
        label = "Select a product for detailed analysis:",
        options = data['product'].unique(),
        help = "Choose a product to view detailed sales data."
    )
    
    st.write(f"Sales Data for {selected_product}:")
    
        


# * Feedback Form

    st.header("Feedback (Your opinion counts)")
    feedback = st.text_area(
        label = "Your Feedback",
        placeholder = "Please share your thoughts on the dashboard.",
        help = "We value your feedback to improve our dashboard."
    )
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")


# 4.0 Footer

st.write("---")
st.write("This business dashboard template is flexible. Expand upon it based on your specific business needs.")



if __name__ == "__main__":
    pass