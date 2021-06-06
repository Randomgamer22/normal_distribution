import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

#reading the csv file and creating lsits based on columns
df = pd.read_csv("csvfiles/StudentsPerformance.csv")
marks_list = df['writing score'];

#calculating mean, median and mode
marks_mean = statistics.mean(marks_list);
marks_median = statistics.median(marks_list);
marks_mode = statistics.mode(marks_list);

#printing mean, median and mode 
print("{} is the mean.".format(marks_mean))
print("{} is the median.".format(marks_median))
print("{} is the mode.".format(marks_mode))

#calculating standard deviation and deviation start and end 1, 2, 3
stdev = statistics.stdev(marks_list)
stdev1start, stdev1end = marks_mean - stdev, marks_mean + stdev
stdev2start, stdev2end = marks_mean - (stdev * 2), marks_mean + (stdev * 2)
stdev3start, stdev3end = marks_mean - (stdev * 3), marks_mean + (stdev * 3)

#creating lists containing values in stdev 1, 2, 3
list_stdev1 = [mark for mark in marks_list if mark > stdev1start and mark < stdev1end]
list_stdev2 = [mark for mark in marks_list if mark > stdev2start and mark < stdev2end]
list_stdev3 = [mark for mark in marks_list if mark > stdev3start and mark < stdev3end]

#printing percentage of values inside stdev 1, 2, 3
print("{}% of values are inside standard deviation 1".format(len(list_stdev1)*100.0/len(marks_list)))
print("{}% of values are inside standard deviation 2".format(len(list_stdev2)*100.0/len(marks_list)))
print("{}% of values are inside standard deviation 3".format(len(list_stdev3)*100.0/len(marks_list)))

fig = ff.create_distplot([marks_list], ["Marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [marks_mean, marks_mean], y = [0, 0.1589], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [stdev1start, stdev1start], y = [0, 0.1589], mode = "lines", name = "stdev1start"))
fig.add_trace(go.Scatter(x = [stdev1end, stdev1end], y = [0, 0.1589], mode = "lines", name = "stdev1end"))
fig.add_trace(go.Scatter(x = [stdev2start, stdev2start], y = [0, 0.1589], mode = "lines", name = "stdev2start"))
fig.add_trace(go.Scatter(x = [stdev2end, stdev2end], y = [0, 0.1589], mode = "lines", name = "stdev2end"))
fig.add_trace(go.Scatter(x = [stdev3start, stdev3start], y = [0, 0.1589], mode = "lines", name = "stdev3start"))
fig.add_trace(go.Scatter(x = [stdev3end, stdev3end], y = [0, 0.1589], mode = "lines", name = "stdev3end"))
fig.show()