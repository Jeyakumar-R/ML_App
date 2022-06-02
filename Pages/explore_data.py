import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# @st.cache
def app():
    if 'data' not in st.session_state:
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        df = st.session_state.data
        st.markdown('# Explore Data')
        st.write(df)
        st.subheader("Columns in dataset")
        st.write(df.columns)
        st.subheader("Shape of the dataset")
        st.write(df.shape)
        st.subheader("Null values")
        st.write(pd.DataFrame([{col: int(df[col].isna().sum()) for col in df.columns}]).T)
        st.subheader("Summary")
        st.write(df.describe().T)
        st.subheader("Data Visualization")
        fig, ax = plt.subplots()
        corr = df.corr()
        ax = sns.heatmap(
            corr,
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True
        )
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        ax.set_title("Correlation Matrix")
        st.pyplot(fig)
        
        # Plot and Visualization

        st.subheader("Customizable Plot")
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns to plot", all_columns_names)   
        st.set_option('deprecation.showPyplotGlobalUse', False)
        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
            
            # Plot By streamlit
            if type_of_plot == 'area':
                cust_data = df[selected_columns_names]
                st.area_chart(cust_data)
            elif type_of_plot == 'line':
                cust_data = df[selected_columns_names]
                st.line_chart(cust_data)
        
            # Custom Plot
            elif type_of_plot:
                cust_data = df[selected_columns_names].plot(kind=type_of_plot)
                st.write(cust_data)
                st.pyplot()

