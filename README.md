# Climate Analytics

The following project is focused: 
* **First**, on analysing and exploring climate weather conditions from Honolulu, Hawaii.
* And **second**, on designing a Climate API with Flask.

The development of the project includes two parts:

* **Step 1 - Climate Analysis and Exploration**

Use of Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. The analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
  * Precipitation Analysis
    * Design a query to retrieve the last 12 months of precipitation data.
    * Select only the `date` and `prcp` values.
  * Station Analysis
    * Design a query to calculate the total number of stations.
    * Design a query to find the most active stations.
    * List the stations and observation counts in descending order.
    * Which station has the highest number of observations?
    * Design a query to retrieve the last 12 months of temperature observation data (TOBS).
    * Filter by the station with the highest number of observations.
    
* **Step 2 - Climate App**

  * Design a Flask API based on the queries made previously
  * Use Flask to create your routes.

## Features

* **Advanced data storage and retrieval**
* Exploratory analysis of climate database using **SQLAlchemy ORM queries, Pandas, and Matplotlib.**

## Built with 

* Flask 

## Outcomes

Here you can check some of the outcomes of the project. However, if you have any doubts feel free to check files

### Area plot of Daily Rainfall average made with pandas
This was done by calculating daily normals (the averages for the min, avg, and max temperatures) from a specific date 

![Area_plot_data.png](Images/Area_plot_data.png)

### Initial page of Climate API made with Flask
With the queries made from the initial analysis, a flask API was made with four routes of the most important climate data.

![Initial_page.png](Images/Initial_page.png)



