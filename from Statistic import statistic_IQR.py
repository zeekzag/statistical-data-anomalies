from Statistics import statistic_IQR

s = statistic_IQR()
range = [48,52,57,61,64,72,76,77,81,85,88]

upper_q = s.upper(range)
lower_q = s.lower(range)
inter_q = s.iqr(range)
anomalies = s.anomalies(range)

print(upper_q)
print(lower_q)
print(inter_q)
print(anomalies)
