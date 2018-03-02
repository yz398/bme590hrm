# bme590hrm
assignment07
Yi Zhao

the basic functions are in list_module

the way to get the results:
	core = ECG(filename = 'test_data1.csv')

In the class ECG, it contains mean_bpm, duration, voltage_extremes,
time_beats, num_beats	
	
I write the detect function by myself, so it cannot cover whole cases
but it can deal with most datasets. To find the peaks, first, I use a 
threshold = 0.2* maximum. Then I use the the maximum and the points around 
it to form a sample test. Using the sample to do correlate with whole data.
After that, using detect function to find peaks.

the fuctions in list_module can also be used in other classes
beats(): the number for the sample
collectdata(): read .csv and return 2 lists with time and voltage
detect_peak(): find the peaks of the list of voltages and return peaks value and indexes
duration(): find the duration for the sample
mean_bpm(): estimate of bpm per minute
min_max_voltage(): find the minimum and the maximum of a list of voltage and return a tuple
time_beats(): find the time series for a beat the first value of each row is the valid number of the time series
