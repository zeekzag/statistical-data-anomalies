import math

class statistic_IQR:
    
        def upper(self, value):
            
            sortvalue = sorted(value)
            n = len(value)
            
            try:
                self.upperindex = 0.75 * n
                uppindex = self.upperindex
                if isinstance(uppindex, float):
                    uppindex = math.ceil(uppindex)
                    self.uppervalue = sortvalue[uppindex]
                    return self.uppervalue
                else:
                    uppindex = int(uppindex)
                    self.uppervalue = sortvalue[uppindex]
                    return self.uppervalue
            
            except TypeError:
                print('Value is not in an integer or float data type.')
                
                
                
        def lower(self, value):
            
            sortvalue = sorted(value)
            n = len(value)
            
            try:
                self.lowerindex = 0.25 * n
                lowindex = self.lowerindex
                if isinstance(lowindex, float):
                    lowindex = math.ceil(lowindex)
                    self.lowervalue = sortvalue[lowindex]
                    return self.lowervalue
                else:
                    lowindex = int(lowindex)
                    self.lowervalue = sortvalue[lowindex]
                    return self.lowervalue
            
            except TypeError:
                print('Value is not an integer or float data type.')
        
        def iqr(self, value):
            
            try:
                upper_val = self.upper(value)
                lower_val = self.lower(value)
                iqr_val = upper_val - lower_val
                return iqr_val
            
            except TypeError:
                print('Value is not an integer or float data type.')
    
        def anomalies(self, value):
            
            try:
                anomaly_range = []
                threshold = 0.2
                upp_limit = self.upper(value) + threshold * self.iqr(value)
                low_limit = self.lower(value) - threshold * self.iqr(value)
                for x in value:
                    if (x >= upp_limit) or (x <= low_limit):
                        anomaly_range.append(x)
                return sorted(anomaly_range)
                
            except TypeError:
                print('Value is not an integer or float data type')

