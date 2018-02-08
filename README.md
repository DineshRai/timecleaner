# timecleaner
Python package to help set up time series data for machine learning


To install:
```
pip3 install timeclean
```

To call into your python scripts
```
from timecleaner import data_cleaner
```

There are several parameters that have to be filled


```
X, Y = data_cleaner(dataframe, Datetime_column, time_interval, outcome_column, time_steps_to_evaluate, time_steps_look_ahead, interprolation_direction)
```

-dataframe - the csv data you wish to use in the format of a pandas dataframe 

-Datetime_column - the name of the Datetime column in your dataset, format as string

-time_interval - the intervals you wish to use when you evaluate your dataset, fromat as string, eg '30min', '10min', '30S, '1S', etc

-outcome_column - the name of the column in your dataset your wish to use as your outcome (ie 'y-axis), format as string

-time_sets_to_evaluate - the number of time steps you wish to use when evaluating your X data

-time_steps_look_ahead - the number of time steps you want to predict ahead (eg if you want predict stock prices 3 hours ahead in hourly data, select 3)

-interprolation_direction - either 'forwards' or 'backwards'

