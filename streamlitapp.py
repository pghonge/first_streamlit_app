import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new healthy dinner')
streamlit.title('Hello')
streamlit.title('good morning!!!')
streamlit.text('🥑🍞 avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select fruit to get information')
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
    #streamlit.text(fruityvice_response.json())
except URLError as e:
  streamlit.error()

