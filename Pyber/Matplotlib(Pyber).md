

```python
# import dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
```


```python
# read csv files

RD = "raw_data/ride_data.csv"
RD = pd.read_csv(RD)

CD = "raw_data/city_data.csv"
CD = pd.read_csv(CD)
CD.city.drop_duplicates(inplace=True)

# # merge csv files
city_ride_data = pd.merge(RD, CD, how='outer',on="city")

city_ride_data.head()


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Lake Jonathanshire</td>
      <td>2018-01-14 10:14:22</td>
      <td>13.83</td>
      <td>5739410935873</td>
      <td>5</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Lake Jonathanshire</td>
      <td>2018-04-07 20:51:11</td>
      <td>31.25</td>
      <td>4441251834598</td>
      <td>5</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lake Jonathanshire</td>
      <td>2018-03-09 23:45:55</td>
      <td>19.89</td>
      <td>2389495660448</td>
      <td>5</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lake Jonathanshire</td>
      <td>2018-04-07 18:09:21</td>
      <td>24.28</td>
      <td>7796805191168</td>
      <td>5</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lake Jonathanshire</td>
      <td>2018-01-02 14:14:50</td>
      <td>13.89</td>
      <td>424254840012</td>
      <td>5</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# defining values to variable
Urban = city_ride_data[(city_ride_data.type == "Urban")]
Suburban = city_ride_data[(city_ride_data.type == "Suburban")]
Rural = city_ride_data[(city_ride_data.type == "Rural")]

# counting riders per urban cities by grouping data by urban
urban_ride_bycity = Urban.groupby([city_ride_data.city]).count()["ride_id"]

# finding average fare for urban cities by grouping data by urban
urban_avgfare = Urban.groupby([city_ride_data.city]).mean()["fare"]


# --------------------------------------------------------------------
# repeating the same for Suburban & Rural
Suburban_ride_bycity = Suburban.groupby([city_ride_data.city]).count()["ride_id"]
Suburban_avgfare = Suburban.groupby([city_ride_data.city]).mean()["fare"]


# for Rural 
rural_rides_bycity = Rural.groupby([city_ride_data.city]).count()["ride_id"]
Rural_average_fare = Rural.groupby([city_ride_data.city]).mean()["fare"]

```


```python
# creating bubble plot

plt.scatter(urban_ride_bycity, urban_avgfare, label = "Urban", s=urban_ride_bycity*20, marker="o", color=["lightcoral"], edgecolors="white")
plt.scatter(Suburban_ride_bycity, Suburban_avgfare, label = "Suburban",s=Suburban_ride_bycity*20, marker="o", color=["lightskyblue"], edgecolors="white")
plt.scatter(rural_rides_bycity, Rural_average_fare, label = "Rural", s=rural_rides_bycity*20, marker="o", color=["gold"], edgecolors="white")

# Plot field size
plt.xlim(0, 45)
plt.ylim(18,50)

# Create a title, x label, and y label for plot
plt.title("Pyber Ride Sharing Data")
plt.xlabel("Total Number of Rides (per city)")
plt.ylabel("Average Fare ($)")

plt.legend(title="City Types")

plt.annotate("Note:\nCircle size represent the driver count per City", xy=(30, 30), xycoords='data',xytext=(47, 35),)
            
            
plt.grid(c="grey")

plt.show()
plt.savefig("Ride_sharing_data.png")
```


![png](output_3_0.png)



    <matplotlib.figure.Figure at 0x29a7b7d5a58>



```python
# Total Fares by City Type by using pie chart

#Define Axis

#X axis (by grouping the data by type and fare and getting the sum)
tot_rides_bycityfare = city_ride_data.groupby(["type"])[["fare"]].sum()

# Format plot
plt.pie(tot_rides_bycityfare, 
        explode=[0,0,.1], 
        labels=["Rural","Suburban","Urban"], 
        colors=["gold","lightskyblue", "lightcoral"],
        autopct= '%.2f%%',
        pctdistance=.6, 
        shadow=True, 
        startangle=100)

# for parameter reference: https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html

# Create a title, x label, and y label for plot
plt.title("Percentage of Total Fares by City Type")
plt.axis("equal")
plt.show()
plt.savefig("Fare_byCity.png")
```


![png](output_4_0.png)



    <matplotlib.figure.Figure at 0x29a7b7a0a90>



```python
#Define Axis

#X axis (To calculate total rides by cities we have grouped data by type and counted the riders IDs to get the number of rides)
tot_rides_bycitytype = city_ride_data.groupby(["type"])[["ride_id"]].count()

# Format plot
plt.pie(tot_rides_bycitytype, 
        explode=[0,0,.1], 
        labels=["Rural","Suburban","Urban"], 
        colors=["gold","lightskyblue", "lightcoral"], 
        
        autopct= '%.2f%%',
        pctdistance=.6, 
        shadow=True, 
        startangle=100)

# for parameter reference: https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.pie.html

# Create a title, x label, and y label for plot
plt.title("Percentage of Total Rides by City Type")
plt.axis("equal")
plt.show()
plt.savefig("Rides_byCity.png")
```


![png](output_5_0.png)



    <matplotlib.figure.Figure at 0x29a7b5d3358>



```python
#Define Axis

#X axis
tot_drivers_bycitytype = CD.groupby(["type"])[["driver_count"]].sum()

# Format plot
plt.pie(tot_drivers_bycitytype, 
        explode=[0,0,.1], 
        labels=["Rural","Suburban","Urban"], 
        colors=["gold","lightskyblue", "lightcoral"], 
        autopct= '%.2f%%',
        pctdistance=.6, 
        shadow=True, 
        startangle=120)

# Create a title, x label, and y label for plot
plt.title("Percentage of Total Drivers by City Type")
plt.axis("equal")
plt.show()
plt.savefig("Drivers_byCity.png")
```


![png](output_6_0.png)



    <matplotlib.figure.Figure at 0x29a7b503b00>

