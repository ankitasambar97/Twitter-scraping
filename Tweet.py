import streamlit as st
import pandas as pd
import pymongo
from PIL import Image
st.set_page_config(page_title='Twitter scrapping',layout='centered')
st.header('&emsp;&emsp;&emsp;&emsp;&emsp;**:blue[TWITTER SCRAPPING]**')

t_image=Image.open(r"C:\Users\HP\Desktop\Guvi\Project\Twitter_image.JPG")
st.image(t_image)

#DISPLAYING DATASET
#Reading csv file via pandas and add a button to display the loaded dataset and its length
st.header('**:blue[Twitter Scrapping introduction:]**')
st.write('''&emsp;&emsp;Twitter scraping is the process of collecting data from Twitter using software tools and libraries. This can include various types of data, such as tweets, profiles, hashtags, locations, and followers, depending on the specific requirements of the project. Twitter scraping can be done using open-source or proprietary tools, and often requires advanced knowledge of programming languages like Python, JavaScript, or R, as well as web scraping techniques and data processing.''')
st.write('''**&emsp;&emsp;:red_circle: we scrape Netflix India tweets in this project**''')

df=pd.read_csv("C:/Users/HP/Downloads/twitter_scrapping_Netflixn.csv")
st.dataframe(df)

st.header('**:blue[Viewing dataset and download as CSV and JSON files:]**')
st.write('''&emsp;&emsp;Welcome to Dataset Explorer, the easy way to view and download your data! With our interactive tool, you can upload your dataset in seconds and view it as an interactive table. Plus, you can download your data as a CSV or JSON file for further analysis.''')
st.text('')  

result=st.button('**_Click here to view a dataset_**')
if result:
    st.write(len(df.index))
    st.dataframe(df)
    
def convert_df_csv(df):
    return df.to_csv()

def convert_df_json(df):
    return df.to_json()

def convert_df_dict(df):
    return df.to_dict('records')



#****************************************************************************************************************************************#
# Adding downlaod buttons to down DF as CSV and JSON
csv=convert_df_csv(df)
Json_data=convert_df_json(df)
st.write('Click the below buttons to downlod the datset as **CSV** and **JSON** files')
col1,col2,col3,col4=st.columns(4)
with col1:
    st.download_button(label='**_Download CSV_**',
                       data=csv,
                       file_name='twitter_netflix.csv',
                       mime='text/csv')
with col2:
    st.download_button(label='**_Download JSON_**',
                       data=Json_data,
                       file_name='twitter_netflix.json',
                       mime='application/json')


#****************************************************************************************************************************************#   
#HASHTAG FILTER 
st.header('**:blue[Filter with #Hashtags and downdload as CSV and JSON:]**')
st.write('''&emsp;&emsp;Effortlessly filter your data using hashtags with our powerful tool! Simply add hashtags to your data, and you can easily search and filter through it to find exactly what you're looking for. Plus, you can even download your filtered data as a CSV or JSON file for further analysis.''')

# df=pd.read_csv("C:/Users/shakt/OneDrive/Desktop/scrapping/twitter_scrapping_Netflix.csv")
df=pd.read_csv("C:/Users/HP/Downloads/twitter_scrapping_Netflixn.csv")
# st.dataframe(df)

# Defining a function to filter the data based on given hashtag
def filter_hashtag(hashtag):
    if hashtag:
        filtered_hashtag = df[df['CONTENT'].str.contains(hashtag)]
        if not filtered_hashtag.empty:
            st.write('Number of tweets:',len(filtered_hashtag.index))
            st.write(filtered_hashtag)
            return filtered_hashtag
        else:
            st.write('No data found for the given hashtag')

hashtag = st.text_input(label='Please type your hashtag in the search bar')
filtered_data = filter_hashtag(hashtag)

# Adding downlaod buttons to down DF as CSV and JSON
#st.write('Click the below buttons to downlod the #hashtag filtered datset as **CSV** and **JSON** files')
col1,col2,col3,col4=st.columns(4)
with col1:    
    if filtered_data is not None:       
        csv = convert_df_csv(filtered_data)
        st.download_button(label='**_Download CSV_**', data=csv, file_name='twitter_hashtag.csv', mime='text/csv')

with col2:
    if filtered_data is not None:
        json = convert_df_json(filtered_data)
        st.download_button(label='**_Download JSON_**', data=json, file_name='twitter_hashtag.json', mime='application/json')
    
st.text('')  
st.text('') 
st.text('')   

#DATE RANGE FILTER
# Setting a header title with blue color for date range filter section 
st.header('**:blue[Filter with date ranges and downdload as CSV and JSON:]**')
st.write('''&emsp;&emsp;Filtering a pandas DataFrame with date ranges is a common task when working with time-series data. Streamlit is a popular Python library for building interactive web apps, which makes it easy to create a user interface for filtering and visualizing data. In this context, filtering a DataFrame with date ranges involves allowing users to input a start and end date, converting those inputs to datetime objects, and using boolean indexing to filter the DataFrame based on the selected date range. After the data is filtered, it's often useful to provide a download button for the filtered data in CSV or JSON format. This allows users to download the data for further analysis or visualization.''')

# df=pd.read_csv("C:/Users/shakt/OneDrive/Desktop/scrapping/twitter_scrapping_Netflix.csv")
df=pd.read_csv("C:/Users/HP/Downloads/twitter_scrapping_Netflixn.csv")
# st.dataframe(df)
# Convert the date column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

begin_date = st.date_input('Enter the begin state', value=df['DATE'].min().date())
start_date = pd.to_datetime(begin_date).tz_localize('UTC')

end_date = st.date_input('Enter the end date', value=df['DATE'].max().date())
end_date = pd.to_datetime(end_date).tz_localize('UTC') + pd.DateOffset(days=1)

result = df[(df['DATE'] >= start_date) & (df['DATE'] < end_date)]

#display as DataFrame
st.write('Number of tweets',len(result.index))
display=st.button('**Click here to view the filtered dataset**')
if display:
    st.write(result)
    
# Adding downlaod buttons to down DF as CSV and JSON
st.write('Click the below buttons to downlod the filtered datset as **CSV** and **JSON** files')   
col1,col2,col3,col4=st.columns(4)
with col1:
    if result is not None:
        csv = convert_df_csv(result)    
        st.download_button(label='**_Download CSV_**', data=csv, file_name='twitter_datefilter.csv', mime='text/csv')
with col2:
    if result is not None:
        json = convert_df_json(result)
        st.download_button(label='**_Download JSON_**', data=json, file_name='twitter_hashtag.json', mime='application/json')
        
#***********************************************************************************************************#
#UPLOADING DATA TO MONGODB
# Setting a header title with blue color for MongoDB upload section 
st.header('**:blue[Uploading Twitter Data to MongoDB:]**')
st.write('''&emsp;&emsp;Uploading Twitter data to MongoDB is a great way to store and manage large amounts of tweets. One easy way to do this is by using Python and a streaming GUI called Streamlit. With this approach, you can fetch tweets in real-time and store them in MongoDB with just a few lines of Python code.''')

#getting input from user such as Database,collection, number tweets
file="C:/Users/HP/Downloads/twitter_scrapping_Netflixn.csv"
num_tweets = st.number_input(label='Enter the number of tweets to upload', min_value=1, step=1,max_value=10000)
df=pd.read_csv(file,nrows=num_tweets)
link=pymongo.MongoClient("mongodb://localhost:27017")
DB_name=st.text_input(label='Enter the existing DB name to connect or new DB name to create')
DB_collection=st.text_input(label='Enter the collection name being part of the above given existing DB or new collection name to create')

#adding a button to upload the data to MongoDB
DB_upload=st.button(label='**_Upload to MongoDB_**')
if DB_upload:
    DB=link[DB_name]
    Collection=DB[DB_collection]
    docs=convert_df_dict(df)
    Collection.insert_many(docs)
    st.write(f"{len(docs)} tweets uploaded to {DB_name} : {DB_collection}")
    