'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
runner_runs = 10
runner_runs_km = runner_runs*1.6
time_in_seconds = (30*60)+30
time_in_hr = (time_in_seconds)/3600
average_speed = runner_runs_km / time_in_hr
print(average_speed)
