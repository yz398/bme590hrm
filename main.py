def main():
	from list_module import beats
	from list_module import collectdata
	from list_module import detect
	from list_module import duration
	from list_module import mean_bpm
	from list_module import min_max_voltage
	from list_module import time_beats
	import json
	form class_ecg import ECG

	core = ECG(filename = "test_data21.csv")
	core.writejson()
	print(core.voltage_extremes)
	print(core.durationtime)
	print(core.num_beat)
	print(core.mean_hr_bpm)
	print(core.time_beat)


if __name__ == "__main__":
	main()
