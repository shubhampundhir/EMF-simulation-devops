import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import mysql.connector
import requests
import os
import math
import numpy as np
import cmath
import sys
import xlrd
import matplotlib.pyplot as plt
import csv
from numpy.fft import fft, ifft
import scipy
from scipy.fft import fft, fftfreq
from scipy import signal

in_dir = 'C:/Users/PC3/Desktop/DCRM/'
files_to_run = os.listdir(in_dir) #list of the file in the current directory for processing
ext = ('.csv', 'xlsx')
file ='170032_08-06-2009_16-39-51_DCRM.csv'
df = pd.read_csv(in_dir + file, header=None)
#print(df)
n_row=df.shape[0]; # no. of rows
n_col=df.shape[1]; # no. of columns
#print (n_row)
#print(n_col)
#n_row = df.shape[0];## will not work in case multiple sheets are read at one time.
#n_col = df.shape[1];
#print(n_row)
#print(n_col)
#print (res)
#df = pd.DataFrame(df, dtype ='object')
#print (df.iat[9, 8])
samp_freq=int(df.iat[9, 8])*1000; #in kHz
samp_time=1/samp_freq;
no_samp=(int(df.iat[10, 3])/(1/int(df.iat[9, 8]))) # plot length/(1/sampling frequency)
total_time=int(df.iat[10, 3]);
#print (samp_freq)
#print (df.columns)
I1=df.iloc[25:8025, 1:2]# dataframe
#print (I1.dtypes)
I2=df.iloc[25:8025, 2:3]# dataframe
I3=df.iloc[25:8025, 3:4]# dataframe
T1=df.iloc[25:8025, 5:6]# dataframe
T2=df.iloc[25:8025, 6:7]# dataframe
T3=df.iloc[25:8025, 7:8]# dataframe
DR1=df.iloc[25:8025, 9:10]# dataframe
DI1=df.iloc[25:8025, 10:11]# dataframe
DR2=df.iloc[25:8025, 11:12]# dataframe
DI2=df.iloc[25:8025, 12:13]# dataframe
DR3=df.iloc[25:8025, 13:14]# dataframe
DI3=df.iloc[25:8025, 14:15]# dataframe
DR4=df.iloc[25:8025, 15:16]# dataframe
DI4=df.iloc[25:8025, 16:17]# dataframe
DR5=df.iloc[25:8025, 17:18]# dataframe
DI5=df.iloc[25:8025, 18:19]# dataframe
DR6=df.iloc[25:8025, 19:20]# dataframe
DI6=df.iloc[25:8025, 20:22]# dataframe
##### for numpy array conversion # conversion of dataframe to numpy arrayx
I1=np.hstack(I1.to_numpy().astype(float))# conversion of array of array to single dimension array by hstack function # conversion of dataframe to numpy array # conversion of string to float type values
I2=np.hstack(I2.to_numpy().astype(float))# conversion of dataframe to numpy array # conversion of string to float type values
I3=np.hstack(I3.to_numpy().astype(float))
T1=np.hstack(T1.to_numpy().astype(float))
T2=np.hstack(T2.to_numpy().astype(float))
T3=np.hstack(T3.to_numpy().astype(float))
DR1=np.hstack(DR1.to_numpy().astype(float))
DI1=np.hstack(DI1.to_numpy().astype(float))
DR2=np.hstack(DR2.to_numpy().astype(float))
DI2=np.hstack(DI2.to_numpy().astype(float))
DR3=np.hstack(DR3.to_numpy().astype(float))
DI3=np.hstack(DI3.to_numpy().astype(float))
DR4=np.hstack(DR4.to_numpy().astype(float))
DI4=np.hstack(DI4.to_numpy().astype(float))
DR5=np.hstack(DR5.to_numpy().astype(float))
DI5=np.hstack(DI5.to_numpy().astype(float))
DR6=np.hstack(DR6.to_numpy().astype(float))
DI6=np.hstack(DI6.to_numpy().astype(float))
#print (I1.dtype)
x_axis= np.arange(1,8001)
plt.title("DCRM graph")
plt.xlabel("No. of sample or time in msec")
plt.ylabel("Magnitude")
#plt.plot(x_axis, I1,x_axis, I2,x_axis, I3,x_axis, DI1,x_axis, DI2,x_axis, DI3,x_axis, DI4,x_axis, DI5,x_axis, DI6,x_axis, DR1,x_axis, DR2,x_axis, DR3,x_axis, DR4,x_axis, DR5,x_axis, DR6)
plt.plot(x_axis,I2,x_axis,DI2,x_axis,DR2,x_axis,T2)
plt.style.use('seaborn-poster')
#plt.show()
sr = 2000# sampling rate
ts = 1.0/sr# sampling interval
t = np.arange(0,1,ts)
no_samp=8000
samp_time=400/(1000*no_samp);
#print (samp_time)
samp_freq=1/samp_time;
#print (samp_freq)
total_time=int(df.iat[10, 3])/1000;
t = np.arange(0,total_time,samp_time)


X = fft(DR1*8/4095) # FFT of a signal since 8ohm is the range of resistance
N = len(X) # Length of X
n= np.arange(N)
#freq = n/samp_time
freq=np.fft.fftfreq(n=DR1.size, d=samp_time)
#print (len(freq))
#print (samp_time)
plt.subplot(2,1,1)
plt.scatter(freq, np.abs(X),s=5)
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.subplot(2,1,2)
plt.plot(x_axis, DR1)
#plt.show()

####FFT of a DR1signal
DR1=df.iloc[2288:6475, 9:10]# dataframe
DR1=np.hstack(DR1.to_numpy().astype(float))
X = fft(DR1*8/4095) # FFT of a signal since 8ohm is the range of resistance
N = len(X) # Length of X
n= np.arange(N)
#freq = n/samp_time
freq=np.fft.fftfreq(n=DR1.size, d=samp_time)
#print (len(freq))
#print (samp_time)
plt.subplot(2,1,1)
plt.scatter(freq, np.abs(X),s=5)
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
#x_axis= np.arange(0,400,samp_time*1000)
x_axis= np.arange(0,209.35,samp_time*1000)
plt.subplot(2,1,2)
plt.plot(x_axis, ifft(X), 'r', x_axis, DR1*8/4095, 'y')
plt.xlabel('Time (msec)')
plt.ylabel('Amplitude')
plt.tight_layout()
#plt.show()
#print (samp_time*1000)
i=(2289-739)*samp_time;
j=(8025-6475)*samp_time;
#print (i*1000)
#print (j*1000)
def unit_step(a,n,Ymax):
    unit=[];
    #print (n)
    for sample in n:
        #print(sample)
        if sample<=a:
            unit.append(Ymax)
        elif sample>a and sample<UL:
            unit.append(0)
            #print(unit)
        elif sample>=UL:
            #print (unit)
            unit.append(Ymax)
    return (unit)
a=0 ##delay of pulse wave
LL=0# start of pulse
UL=(len(x_axis)-1)*samp_time*1000#end of pulse
Ymax=np.abs(max(ifft(X)))###maximum amplitude of ifft or original signal
unit=unit_step(a,x_axis,Ymax)
unit = np.array(unit)  ### convert type list to numpy.ndarray
plt.subplot(2,1,1)
z=DR1*8/4095-unit### conversion of data frame to numpy nd array (multi-dimension)to single dimension array and subtracting unit wave
plt.plot(x_axis, DR1*8/4095,x_axis, z)
#print (unit-np.hstack(DR1))
#print (z)
f_z = fft(z)
#print (samp_time)
freq2=np.fft.fftfreq(n=f_z.size, d=samp_time)
#print (len(freq))
plt.subplot(2,1,2)
plt.plot(freq2,np.abs(f_z), freq,np.abs(X))
#plt.show()

### ### function to identify and select data range for individual array from csv
def fetch_data(file_name,Req_para):
    para_values=[]
    in_dir = 'C:/Users/PC3/Desktop/DCRM/'
    files_to_run = os.listdir(in_dir) #list of the file in the current directory for processing
    ext = ('.csv', 'xlsx')
    df = pd.read_csv(in_dir + file_name, header=None)
    samp_freq = 20000;
    samp_time = 1/samp_freq;
    no_samp=400 / (1000 * samp_time);
    #n_row=df.shape[0]; # no. of rows
    #n_col=df.shape[1]; # no. of columns
    for para in Req_para:
        # Select columns containing defined value
        col_filter = (df == para).any()# will iterate all rows to find the value
        col_pos = np.flatnonzero(col_filter)  # getting non zero indices
        # Select rows containing defined value
        row_filter = df[col_pos].values == para
        row_pos = np.flatnonzero(row_filter)# getting non zero indices
        sub_df = df.loc[row_pos[0] + 1:row_pos[0] + no_samp, col_filter]
        para_values.append(sub_df)
    # print("\ncolumns selected :", col_pos)
    # print (df.head())
    #print("\nRows selected :", pos)
    #result=df.iloc[pos]# selecting rows
    #print (result)
    return para_values
tc_coil_crnt=['Curret','current2','current3'];
dcrm=['Res1','Res2','Res3','Res4','Res5','Res6'];
dcrm_current=['Curr1', 'Curr2','Curr3','Curr4','Curr5','Curr6'];
contact_travel=['Travel 1','Travel 2','Travel 3'];

tc_coil_crnt_values=fetch_data('170032_08-06-2009_16-39-51_DCRM.csv',tc_coil_crnt);
dcrm_values=fetch_data('170032_08-06-2009_16-39-51_DCRM.csv',dcrm);
dcrm_current_values=fetch_data('170032_08-06-2009_16-39-51_DCRM.csv',dcrm_current);
contact_travel_values=fetch_data('170032_08-06-2009_16-39-51_DCRM.csv',contact_travel);
#print (contact_travel_values)
#print (tc_coil_crnt_values[0].dtypes)
##### for numpy array conversion # conversion of dataframe to numpy arrayx
I1=np.hstack(tc_coil_crnt_values[0].to_numpy().astype(float))# conversion of array of array to single dimension array by hstack function # conversion of dataframe to numpy array # conversion of string to float type values
I2=np.hstack(tc_coil_crnt_values[1].to_numpy().astype(float))# conversion of dataframe to numpy array # conversion of string to float type values
I3=np.hstack(tc_coil_crnt_values[2].to_numpy().astype(float))
T1=np.hstack(contact_travel_values[0].to_numpy().astype(float))
T2=np.hstack(contact_travel_values[1].to_numpy().astype(float))
T3=np.hstack(contact_travel_values[2].to_numpy().astype(float))
DR1=np.hstack(dcrm_values[0].to_numpy().astype(float))
DI1=np.hstack(dcrm_current_values[0].to_numpy().astype(float))
DR2=np.hstack(dcrm_values[1].to_numpy().astype(float))
DI2=np.hstack(dcrm_current_values[1].to_numpy().astype(float))
DR3=np.hstack(dcrm_values[2].to_numpy().astype(float))
DI3=np.hstack(dcrm_current_values[2].to_numpy().astype(float))
DR4=np.hstack(dcrm_values[3].to_numpy().astype(float))
DI4=np.hstack(dcrm_current_values[3].to_numpy().astype(float))
DR5=np.hstack(dcrm_values[4].to_numpy().astype(float))
DI5=np.hstack(dcrm_current_values[4].to_numpy().astype(float))
DR6=np.hstack(dcrm_values[5].to_numpy().astype(float))
DI6=np.hstack(dcrm_current_values[5].to_numpy().astype(float))
### ### function to identify empty arrays and not considered same for analytics
### identify active channels for evaluation
### target open close time trend by trigger time and duration co-ordination
def idntf_act_chnl(in_arys):
    out_array = [];
    for arr in in_arys:
        out_array = np.append(out_array,(np.any(arr)));  # True if any values of array are non-zero else false for zero/empty array
    return out_array
in_chnl=[I1,I2,I3,T1,T2,T3,DR1,DR2,DR3,DR4,DR5,DR6,DI1,DI2,DI3,DI4,DI5,DI6]
act_chnl=[]
eval_arys=[];
act_chnl = idntf_act_chnl(in_chnl);# 1 for active channels and 0 for non-active channels
print (act_chnl)
arr = np.array([[0, 8, 0], [7, 0, 0], [-5, 0, 1]])
#print("Input  array : \n", arr)
out_tpl = np.nonzero(arr)
#print("Indices of non zero elements : ", out_tpl)
### identify last non-zero value in array
x_end=np.max(np.nonzero([-2, 20, -1, 0, 3, 0, 0]))
x_start=np.min(np.nonzero([-2, 20, -1, 0, 3, 0, 0]))
no_samp_perd=x_end-x_start
duration=no_samp_perd*samp_time ## duration of pulse in one file
#print (x_end)
#print (x_start)
#print (duration)​



#print(para_values)
#plt.show()
#print(type(df.iat[10, 4]))
#print(df.iat[10, 4])
#print(df.iat[9, 9])
#print(df.iloc[0:11,0:5]) # prints 11 rows with 4 columns [row,column]
#print(df.iloc[0:11])# prints full 11 rows
#print(df.iloc[0:11,:])# prints full 11 rows with all columns
#print(df.iloc[:,0:5])# prints full 5 columns
#print (df.index)# returns index or number of rows
#print (df.columns)# returns index or number of rows gives the list of the column (header) names.
#print (df.shape)# shows dimension of data frame
#print(df[['User Name', 'Age', 'Gender']]) #get columns by its name
#pd.read_csv(file_path, header=None, usecols=[3,6]) # reads only specific column of csv file
#df['City'][1] # dataframe[column name][row index]

#print(x.dtypes)
#print(type(x))## type is dataframe
#print(x.dtypes)
#print(type(x))## type is dataframe
#print (type(x.values))## type is numpy array
#y=x.values; # conversion of dataframe to numpy array
#print (y)
#y=y.astype(float) # conversion of string to float type values
#print (type (y))
#print(y[8]+y[9])# its type is string






## detect file with xlsx extension and convert all sheets of the file in csv file
## for extracting data from excel sheet
#for file in files_to_run:
#    if file.endswith(ext[1]):
        #print('Running {}'.format(in_dir + file))
#        df = pd.read_excel(in_dir + file, sheet_name=None) ##  if sheet_name=None is specified it will read all sheets in excel else only one
        #print(df)
#        sheets = df.keys()
#        for sheet_name in sheets:
#            sheet = pd.read_excel(in_dir + file, sheet_name=sheet_name)
#            sheet.to_csv(in_dir + "%s.csv" % sheet_name, index=False, header=None)

#processing of all csv files
## CSV file can have only 1 sheet and its a limitation
#for file in files_to_run:
#    if file.endswith(ext[0]):
#        print('Running {}'.format(in_dir + file))
#        df = pd.read_csv(in_dir + file, header=None)
        #print(df)
#        n_row=df.shape[0]; # no. of rows
#        n_col=df.shape[1]; # no. of columns
        #print (n_row)
        #print(n_col)
        #n_row = df.shape[0];## will not work in case multiple sheets are read at one time.
        #n_col = df.shape[1];
        #print(n_row)
        #print(n_col)
        #print (res)
#        df = pd.DataFrame(df)
#        no_samples=(int(df.iat[10, 4])/(1/int(df.iat[9, 9])))
#        print (no_samples)
        #print(type(df.iat[10, 4]))
#        print(df.iat[10, 4])
#        print(df.iat[9, 9])
        #print(df.iat[0, 0])





#### extract sheet names from excel
#xl = pd.ExcelFile(in_dir + file)
#print(xl.sheet_names)
#res = len(xl.sheet_names)

###### read a xls or xlsx file and convert to csv
#file = ('C:/Users/PC3/Desktop/DCRM/HU Result Channel Data from SCOPE.xlsx')
#read_file = pd.read_excel (file,engine='openpyxl')
#read_file.to_csv (r'C:/Users/PC3/Desktop/DCRM/OUTPUT4.csv', index = None, header=True)
#print (read_file)




## no. of rows and columns
#n_row=df.shape[0];
#n_col=df.shape[1];
#print (n_row)
#print(n_col)






##### for numpy array conversion # conversion of dataframe to numpy arrayx
#I1=I1.values.astype(float) # conversion of string to float type values # same conversion of dataframe to numpy arrayx
#I2=I2.values.astype(float) # conversion of string to float type values# conversion of dataframe to numpy arrayx
#I3=I3.values.astype(float)
#T1=T1.values.astype(float)
#T2=T2.values.astype(float)
#T3=T3.values.astype(float)
#DR1=DR1.values.astype(float)
#DI1=DI1.values.astype(float)
#DR2=DR2.values.astype(float)
#DI2=DI2.values.astype(float)
#DR3=DR3.values.astype(float)
#DI3=DI3.values.astype(float)
#DR4=DR4.values.astype(float)
#DI4=DI4.values.astype(float)
#DR5=DR5.values.astype(float)
#DI5=DI5.values.astype(float)
#DR6=DR6.values.astype(float)
#DI6=DI6.values.astype(float)




