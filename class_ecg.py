from list_module import beats
from list_module import collectdata
from list_module import detect
from list_module import duration
from list_module import mean_bpm
from list_module import min_max_voltage
from list_module import time_beats
import json


class ECG():
    """
        returns various attributes

        :param self: the name of test sample
        :type self: str
        :param self.time: the list of test time
        :param self.voltage: the list of test voltage
        :param self.voltage_extremes: tuple containing minimum and
                                        maximum lead voltages
        :param self.durationtime: time duration of the ECG strip
        :param self.num_beat:number of detected beats in the strip
        :param self.time_beat:numpy array of times when a beat occurred
        :param peaks: 2 lists contain original time and voltage
        
        :return: different attributes
    """
    def __init__(self, filename='test'):
        self.filename = filename
        (self.time, self.voltage) = (None, None)
        self.mean_hr_bpm = None
        self.voltage_extremes = None
        self.durationtime = None
        self.num_beat = None
        self.time_beat = None
        self.peaks = [None, None]
        
        self.collectdata()
        self.peak()
        self.beats()
        self.mean_bpm()
        self.time_beats()
        self.min_max_voltage()
        self.duration()
        
        self.writejson()

    def collectdata(self):
        (self.time, self.voltage) = collectdata(self.filename)
        return self.time, self.voltage

    def peak(self):
        """
            return the peaks' information of the ECG data
            
            :param fv: the original list of voltage
            :param cd: the list to store the results of correlate
            :param cb;a list store correlation results after thereshold
            :param a : the maximam of the original voltage
            :param aa: the sample to do the correlate
            
            :returns: return a list include index and value of peaks
            :rtype: [float,float]
        """
        fv = self.voltage
        a = fv.index(max(fv))
        import matplotlib.pyplot as plt
        aa = fv[a-12:a+12]
        cd = np.correlate(aa, fv, 'full')
        cb = []
        for i in range(len(cd)-1):
                if cd[i] > 0.2*max(cd):
                    cb.append(cd[i]) 
                else:
                    cb.append(0)
        plt.figure(1)
        plt.plot(cb)
        plt.plot(fv)
        plt.show()
        self.peaks = detect_peak(cb)
        return self.peaks
    def mean_bpm(self):
        self.mean_hr_bpm = mean_bpm(self.peaks[1], self.time)
        return self.mean_hr_bpm
    def min_max_voltage(self):
        self.voltage_extremes = min_max_voltage(self.voltage)
        return self.voltage_extremes
    def duration(self):
        self.durationtime = duration(self.time)
        return self.durationtime
    def time_beats(self):
        self.time_beat = time_beats(self.peaks[1], self.voltage)
        return self.time_beat
    def beats(self):
        self.num_beat = beats(self.peaks[1])
        return self.num_beat
    def writejson(self):
        figures = {"mean_hr_bpm": "self.mean_hr_bpm",
                   "voltage_extremes": "self.voltage_extremes",
                   "duration": "self.durationtime",
                   "num_beat": "self.numbeat",
                   "beats": "self.time_beat"}
        a = self.filename
        b = a.replace('.csv', '.json')
        with open (b, "w") as f:
            json.dump(figures, f)
        return
