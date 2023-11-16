import streamlit
import pandas
streamlit.title('My Parents new healthy dinner')
streamlit.title('Hello')
streamlit.title('good morning!!!')
streamlit.text('🥑🍞 avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


# Display the table on the page.
