# SI 507 housing assistance portal

### Project Motivation
Shortlisting universities based on location can be challenging for international students due to various factors that need to be considered. Rent, weather conditions, and crime rate are some crucial factors that require attention. Unfortunately, there is no centralized website that provides all these data in one place. Therefore, I suggest creating a one-stop solution to address this issue.

### Python Packages to be installed separately 
- Flask
- Requests
- Plotly

## Instructions on how to interact with the system 
Enter the university name for which you want the information. All the weather data is displayed in the form of plots, which can be zoomed in or saved. All the housing information, such as rent prices, restaurant prices, etc., is displayed using an interactive table (datatable library). The user can sort data in ascending or descending order and download the table as PDF, CSV, or JSON.  

![website demo](https://github.com/SauravTelge/SI507-housing-assistance-portal/blob/main/extra_files/demo_website.gif)


## Data Structure

- Crimes-related data for different cities are stored in a **tree** data structure.
- A Binary search tree to insert, delete, and search a node.
- A node consists of a key-value pair, where the key contains the city's rank in terms of crimes, and the value contains a list consisting of the city name, state, and number of crimes per day.
- Scrapped this data from a website and cached it in a JSON before storing it in a tree.
- Based on the binary search results obtained after comparing nodes in terms of rank, we can quickly access the desired node's results.
