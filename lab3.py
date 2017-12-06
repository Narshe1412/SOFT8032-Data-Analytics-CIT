# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:54:14 2017

1. instant: record index
2. season : season (1:springer, 2:summer, 3:fall, 4:winter)
3. yr : year (0: 2011, 1:2012)
4. mnth : month ( 1 to 12)
5. hr : hour (0 to 23)
6. holiday : weather day is holiday or not (extracted from [Web Link])
7. weekday : day of the week
8. workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
9. + weathersit :
i. 1: Clear, Few clouds, Partly cloudy, Partly cloudy
ii. 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
iii. 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light
Rain + Scattered clouds
iv. 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
10. temp : Normalized temperature in Celsius. The values are divided to 41 (max)
11. atemp: Normalized feeling temperature in Celsius. The values are divided to 50
(max)
12. hum: Normalized humidity. The values are divided to 100 (max)
13. windspeed: Normalized wind speed. The values are divided to 67 (max)
14. casual: count of casual users
15. registered: count of registered users
16. cnt: count of total rental bikes including both casual and registered
"""

import numpy as np

data = np.genfromtxt("bikeSharing.csv", delimiter = ',')

## Part 1
HOLIDAYCOLUMN = 5
USERCOLUMN = 15

#generate a true table where HolidayColumn is 1
isHoliday = data[:, HOLIDAYCOLUMN ] == 1
#use this table to slice data
holidayUsers = data[isHoliday]
#calculate, on the new table, just the mean in the desired column
meanHoliday = np.mean(holidayUsers[:, USERCOLUMN], axis = 0)

isWeekday = data[:, HOLIDAYCOLUMN ] == 0
weekdayUsers = data[isWeekday]
meanWeekday = np.mean(weekdayUsers[:, USERCOLUMN], axis = 0)

# shortcut
hUsers = data[data[:, HOLIDAYCOLUMN] == 1]
hMean = np.mean(hUsers[:, USERCOLUMN], axis = 0)


""" 
## Part 2
You will notice that the values in the temp column are normalized. It stores
 normalized temperature in Celsius. The values are divided to 41 (max)
 Your objective is to produce a new NumPy array. The new array should be a copy
of the original array (see np.copy) with the real Celsius values replacing the
normalized values for the temperature column. 
"""
#celsius = 10
trueCelsius = np.copy(data)
trueCelsius[:,9] = trueCelsius[:,9] * 41


"""
## Part 3
Generally on a given day the number of registered users outnumber the
number of casual users. Determine the percentage of the days in the dataset
where the casual users outnumber the registered users (You should be able
to do this in 2 or 3 lines of code using a relational operator).
"""
#casual 14
#registered 15

comparison = (data[:,13]) > (data [:,14])
daysMoreCasual = data[(data[:,13]) > (data [:,14])]
print(len(daysMoreCasual) / len(data) * 100)


"""
## Part 4
In this question you should provide a new implementation of one of last
week’s questions using array indexing. The objective of this task is to
investigate the impact of weather conditions on the popularity of the bike
scheme. For each of the 4 possible weather conditions calculate the average
number of rental bikes.

Mean users for weather = Clear : 204.869271883
Mean users for weather = Misty : 175.165492958
Mean users for weather = Light Rain : 111.579281184
Mean users for weather = Heavy Rain : 74.3333333333

"""

#weather 9
#count 16
def avgWeather(weather):
    filteredTable = data[data[:, 8] == weather]
    return np.mean(filteredTable[:,15], axis = 0)

print("Mean users for weather Clear: ", avgWeather(1))
print("Mean users for weather Misty: ", avgWeather(2))
print("Mean users for weather Light Rain: ", avgWeather(3))
print("Mean users for weather Heavy Rain: ", avgWeather(4))
