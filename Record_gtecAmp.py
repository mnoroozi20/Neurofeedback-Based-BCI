import pygds as g
import numpy as np
import pandas as pd

d = g.GDS()

minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0]
d.SamplingRate, d.NumberOfScans = minf_s

for ch in d.Channels:
    ch.Acquire = True
d.SetConfiguration()
scope = g.Scope(1/d.SamplingRate, title="Channels: %s", ylabel = u"U[μV]")

Matrixdata=[]
event_time=int(input('Enter the time of event:'))
i=0
while i<event_time:
    aa = d.GetData(d.SamplingRate)
    Matrixdata.extend(aa)   
    i+=1
my_array = np.array(Matrixdata)

# print(my_array)
# print(type(my_array))
# print(my_array.shape)
pd.DataFrame(my_array).to_excel('my_matrix.xlsx')
