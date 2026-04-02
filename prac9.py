p_cloudy = 0.40
p_rain = 0.20
p_cloud_and_rain = 0.85
result = (p_rain * p_cloud_and_rain) / p_cloudy
print("Probability of rain if it is cloudy :",result)
print("Percentage:",result * 100,"%")