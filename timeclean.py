import pandas as pd
import numpy as np


def data_cleaner(dataframe, Datetime_column, time_interval, outcome_column, time_steps_to_evaluate=1, time_steps_look_ahead=0, interprolation_direction='forward'):



  if interprolation_direction == 'forward':
    interprolation_direction = 'ffill'
  elif interprolation_direction == 'backward':
    interprolation_direction = 'bfill'

  #sort by DateTime
  df_sorted = dataframe.sort_values(Datetime_column)

  #Deletes duplicates, keeps last value, and sets DateTime as index
  indexed_df = df_sorted.drop_duplicates(Datetime_column, keep='last').set_index(Datetime_column)

  #Creates consistent intervals according to input
  regularized_intervals = indexed_df.asfreq(freq=time_interval, method='ffill')

  #separates data that will be the Y from X
  Y_data = regularized_intervals[outcome_column].to_frame(name=outcome_column)
  X_data = regularized_intervals.drop([outcome_column], axis =1)

  X_reg_intervals, Y_reg_intervals = [], []

  #time_steps_to_evaluate will be the number of time steps in each instance of the X data, time_steps_look_ahead will be the number of time steps the model will look ahead
  for i in range(len(X_data) - time_steps_to_evaluate - time_steps_look_ahead):
    x = X_data.iloc[i:(i+time_steps_to_evaluate)].values
    X_reg_intervals.append(X_data.iloc[i:(i+time_steps_to_evaluate)].values)
    Y_reg_intervals.append(Y_data.iloc[i + time_steps_to_evaluate + time_steps_look_ahead -1].values)

  #reshapes and converts to np arrays

  X_output_data = np.array(X_reg_intervals).reshape(len(X_reg_intervals), X_data.shape[1], time_steps_to_evaluate)
  Y_output_data = np.array(Y_reg_intervals).reshape(len(Y_reg_intervals), 1)

  return X_output_data, Y_output_data

