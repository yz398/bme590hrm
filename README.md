# bme590hrm
assignment07
Yi Zhao

the basic functions are in list_module

the way to get the results:
	ECG('test_data1.csv')

In the class ECG, it contains mean_bpm, duration, voltage_extremes,
time_beats, num_beats	
	
I write the detect function by myself, so it cannot cover whole cases
but it can deal with most datasets. To find the peaks, first, I use a 
threshold = 0.2* maximum. Then I use the the maximum and the points around 
it to form a sample test. Using the sample to do correlate with whole data.
After that, using detect function to find peaks.


