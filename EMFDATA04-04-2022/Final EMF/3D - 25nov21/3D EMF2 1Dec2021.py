# Add units of measurements particularly for span, electric field
# show a figure showing x y z co-ordinate system
# check output of measurement function next week and compare with matlab
# install numpy module
import cmath
import math
import numpy
#import matplotlib.pyplot as plt
# import cmath
 #import array
# Inputs of the long transmission line
#d = float(input('diameter of the one strand in Cm='));
d = 3.5;
#n = int(input('total number of strand in bundle='));
n = 1;
#s = float(input('space between any 2 strand='));
s = 45.7;
#nphase = int(input('total no of phases='));
nphase = 1;
pi=22/7;
db = s / math.sin(pi/n);
eradi = n*d/db;
eradi = math.pow(eradi, 1/n);
eradi = eradi*db/2;
#print(eradi)

Vm=[400]; # Voltage array
Pm=[0]; # phase angle array
#V=[(-151.6+262.5j),(303.1+0j),(-151.6-262.5j)]; # in kV
# code for fetching voltage and phase angle data automatically
a=0;
#Vm=[];
#Pm=[];
V=[];
for a in range(0,nphase,1):
    #print('Phase %d ' %(a+1))
    #voltage = float(input('RMS Line-Line voltage magnitude in kV='));
    #Vm.append(voltage);
    #print('Phase %d ' %(a+1))
    #phase=float(input('phase angle in degree='));
    #Pm.append(phase)
    x=math.cos(float (Pm[a])*((22/7)/180));
    y=math.sin(float(Pm[a])*((22/7)/180));
    V.append((Vm[a]/math.sqrt(3))*complex(x,y));
#print(Vm);
#print(Pm);
#print (V[0])
# transposition required or not to be ascertained
""" V=V';
"""
# round()
span=400;
#span = float(input('span length='));
weight=0.35;
condx_axis=[];
profile=[];
h1=[];
h2=[];
min_cle=[];
s1=[];
s2=[];
D=[];
#a=0;
b=0;
def cordinates(a):
    #print('cordinate of conductor %d ' % (a + 1))
    #cond_x_axis1 = float(input('x cordinate='));
    cond_x_axis1 = -7.5
    #profile2 = float(input('for Flat conductor profile press 1 and Catenary conductor profile press 2='));
    #profile1=round(profile2);
    profile1=2;
    if profile1 == 2 or  profile1 == 1:
        #h11 = float(input('starting tower height='));
        h11=21.813;
        h22=21.813;
        #h22 = float((input('ending tower height=')));
        if profile1 == 2:
            #min_cle1 = float(input('min clearance='));
            min_cle1=8.813;
        elif profile1 == 1:
            if h11 > h22:
                min_cle1=h22
            else:
                min_cle1=h11
        h1.insert(a,h11);
        h2.insert(a,h22);
        condx_axis.insert(a,cond_x_axis1);
        profile.insert(a,profile1);
        min_cle.insert(a,min_cle1);
        s1.append(int(h1[a] - min_cle[a]));
        s2.append(int(h2[a] - min_cle[a]));
        if s1[a] < 0 or s2[a] < 0:
            print("data entered is incorrect please enter data again")
            s1.pop(a)
            s2.pop(a)
            h1.pop(a)
            h2.pop(a)
            condx_axis.pop(a)
            profile.pop(a)
            min_cle.pop(a)
            cordinates(a)
    else:
        cordinates(a)

for a in range(0, nphase, 1):
    cordinates(a);
#print(condx_axis);
#step=round(float(input('No. of step(integer value)=')));
step=19;
#div = round(float(input('Enter No. of Sub divisions=')));
div=19;
#def measurement(div):
X=[];
Y=[];
Z=[];
#x_start = float(input('starting x cordinate of measured point='));
x_start = -7.5;
#x_end = float(input('ending x cordinate of measured point='));
x_end = 7.5
#y_start = float(input('starting y cordinate of measured point='));
y_start = 1;
#y_end = float(input('ending y cordinate of measured point='));
y_end = 1;
#z_start = float(input('starting z cordinate of measured point='));
z_start = 200;
#z_end = float (input('ending z cordinate of measured point='));
z_end = 200;
x_inc = ((x_end - x_start) / div);
y_inc = ((y_end - y_start) / div);
z_inc = ((z_end - z_start) / div);

if x_inc == 0:
    for ar in numpy.arange(start=0,stop=(div + 1),step=1):
        # X.append(x_start)
        X.insert(ar, x_start)
else:
    X.insert(0, x_start)
    for ar in numpy.arange(start=1, stop=(div + 1), step=1):
        # X.append(x_start)
        X.insert(ar, (X[ar-1]+x_inc))
if y_inc == 0:
    for ar in numpy.arange(0,(div + 1), 1):
        Y.insert(ar, y_start)
else:
    Y.insert(0, y_start)
    for ar in numpy.arange(start=1, stop=(div + 1), step=1):
        # X.append(x_start)
        Y.insert(ar, (Y[ar - 1] + y_inc))
if z_inc == 0:
    for ar in numpy.arange(0,(div + 1), 1):
        Z.insert(ar, z_start)
else:
    Z.insert(0, z_start)
    for ar in numpy.arange(start=1, stop=(div + 1), step=1):
        # X.append(x_start)
        Z.insert(ar, (Z[ar - 1] + z_inc))

#print(X)
#print(Y)
#print(Z)
m= numpy.array([X, Y, Z]);
m=numpy.transpose(m)
#print(m);

#print(m);
# final sag profiles for all conductors
final=[]
conductor_span=[];
conductor_yaxix=[];
conductor_xaxix=[];
final_height=[];
sec=[];
#print(sec)
#print(final)
#print(m)
#print(conductor_span)
#final_height=[];
#return final_height
def ele_height(a, mmm1):
    sec = span / div;

    if profile[a] == 2:
        # sec = span / mmm;
        # distance of lowest point of conductor from the taller support
        # if statement is required for ? choosing taller support
        s1 = h1[a] - min_cle[a];
        s2 = h2[a] - min_cle[a];
        D = s1 / s2;
        min = span * math.sqrt(D) / (1 + math.sqrt(D));
        if (s1 > s2):
            #print(min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = (To / weight * (math.cosh(weight * (min - mmm1) / To) - 1)) + min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1 - min) / To) - 1)) + min_cle[a];
        elif (s2 > s1):
            #print (min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * (span-min) * (span-min) / (2 * s2);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = (To / weight * (math.cosh(weight * (min - mmm1) / To) - 1)) + min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1 - min) / To) - 1)) + min_cle[a];
        elif (s1 == s2):
            #print (min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1< min:
                Y1 = (To / weight * (math.cosh(weight * (min-mmm1) / To) - 1))+ min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1-min) / To) - 1))+ min_cle[a];
    else:
        Y1 = h2[a] + (h2[a] - h1[a]) / span * (mmm1 - span);
    return Y1
def sec_length(a):
    sec_len = [];
    sec_len1 = [];
    sec = span /div;
    cordi_span = [];  # starting and ending point each section
    sec_cordi_height = [];  # height at each sec point
    sec_cordi_xaxix = [];

    if profile[a] == 2:
        # sec = span / mmm;
        # distance of lowest point of conductor from the taller support
        # if statement is required for ? choosing taller support
        s1 = h1[a] - min_cle[a];
        s2 = h2[a] - min_cle[a];
        if (s1 > s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            aa = 0;
            for yyy in numpy.arange(min, 0,-sec):
                cordi_span.insert(aa,(min-yyy))
                sec_cordi_height.insert(aa,ele_height(a, (min-yyy)))
                sec_cordi_xaxix.insert(aa,condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * yyy / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * 0 / To)))
            sec_cordi_height.insert(aa, ele_height(a, (min - yyy)))
            cordi_span.insert(aa, (min - 0))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            #print(0)
            aa = aa + 1;
            To = weight * min * min / (2 * s2);
            for zzz in numpy.arange((sec - yyy), (span - min), sec):
                cordi_span.insert(aa,(zzz+min))
                sec_cordi_height.insert(aa, ele_height(a, (zzz+min)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * zzz / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * (span - min) / To)))
            cordi_span.insert(aa, (span))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            sec_cordi_height.insert(aa, ele_height(a, (span)))
            #print(span - min)
            aa = aa + 1;

        elif (s2 > s1):
            D = s2 / s1
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s2);  # To = weight * x * x / (2 * max_sag)
            aa = 0;
            for zzz in numpy.arange(min, 0, -sec):
                cordi_span.insert(aa, (min - zzz))
                sec_cordi_height.insert(aa, ele_height(a, (min - zzz)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * zzz / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * 0 / To)))
            sec_cordi_height.insert(aa, ele_height(a, (min - yyy)))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            cordi_span.insert(aa, (min - 0))
            #print(0)
            aa = aa + 1;
            To = weight * min * min / (2 * s1);
            for yyy in numpy.arange((sec - zzz), (span - min), sec):
                cordi_span.insert(aa, (yyy + min))
                sec_cordi_height.insert(aa, ele_height(a, (yyy + min)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * yyy / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * (span-min) / To)))
            cordi_span.insert(aa, (span))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            sec_cordi_height.insert(aa, ele_height(a, (span)))
            #print(span-min)
            aa = aa + 1;
        elif (s1 == s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            aa = 0;
            for yyy in numpy.arange(min, 0, -sec):
                cordi_span.insert(aa, (min-yyy))
                sec_cordi_height.insert(aa, ele_height(a, (yyy + min)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * yyy / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * 0 / To)))
            sec_cordi_height.insert(aa, ele_height(a, (min - yyy)))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            cordi_span.insert(aa, (min - 0))
            #print(0)
            aa = aa + 1;
            To = weight * min * min / (2 * s2);
            for zzz in numpy.arange((sec-yyy), (span - min), sec):
                cordi_span.insert(aa, (zzz + min))
                sec_cordi_height.insert(aa, ele_height(a, (zzz + min)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * zzz / To)))
                aa = aa + 1;
            sec_len1.insert(aa, To / weight * (math.sinh(weight * (span-min) / To)))
            cordi_span.insert(aa, (span))
            sec_cordi_xaxix.insert(aa, condx_axis[a])
            sec_cordi_height.insert(aa, ele_height(a, (span)))
            #print(span-min)
            aa = aa + 1;
    else:
        xxx = 0;
        if (h1[a] == h2[a]):
            #To = weight * min * min / (2 * s1);
            for yyyy in range(0, div+1, 1):
                cordi_span.insert(yyyy, xxx)
                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                sec_len1.insert(yyyy,span/(div+1) )
                xxx = xxx + sec;
        else:
            for yyyy in range(0, div+1, 1):
                cordi_span.insert(yyyy, xxx)
                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                diagonal_length=math.sqrt((h1[a] - h2[a])*(h1[a] - h2[a])+span*span)
                sec_len1.insert(yyyy,diagonal_length/(div+1) )
                xxx = xxx + sec;

    #print(To / weight * (math.sinh(weight *400/To)))
    #print(sec_len1)
    mm = numpy.array([sec_cordi_xaxix, sec_cordi_height, cordi_span]);
    mm = numpy.transpose(mm)
    #print (mm)
    return sec_len1,len(sec_len1),mm
#print(L)
section_len=[];
section_len1=[];
sec=[];
cordi_section=[];
section_len2=[];
sec_cordi_height1=[];
sec_cordi_xaxix1=[];
sec_matrix1=[];
for ww in range(0, nphase, 1):
   section_len = [];
   cordi_sec=[];
   section_len,nsec,sec_matrix=sec_length(ww);
   #print(nsec)
   sec.insert(ww,nsec)
   sec_matrix1.insert(ww,sec_matrix);
   for www in range(1, nsec, 1):
     section_len1.insert(www-1,abs(section_len[www]-section_len[www-1]))
   section_len2.insert(ww,section_len1)
   section_len1=[];
#print(section_len2)

"""
print(sec_matrix1[0])
print(sec_matrix1[0][0])
print(sec_matrix1[0][0][0])"""
#sec_matrix1[0][0][0]  x_cordinatre of 1st sec
#sec_matrix1[0][0][1]  y_cordinatre of 1st sec
#sec_matrix1[0][0][2]  z_cordinatre of 1st sec
def sec_voltage(qq):
    each_sec_voltage = [];
    each_sec_voltage_real=[];
    each_sec_voltage_imag=[];
    for vv in range(0, (sec[qq]-1), 1):
        each_sec_voltage.insert(vv,V[qq])
        each_sec_voltage_real.insert(vv, V[qq].real)
        each_sec_voltage_imag.insert(vv, V[qq].imag)

    #each_sec_volatge1=numpy.reshape(each_sec_volatge,((sec[qq]-1),1))
    #print(each_sec_volatge_imag)
    #print(each_sec_volatge_real)
    return each_sec_voltage
#print(sec_matrix1)
def seg_matrix(pp):
    AF1 = [];
    AF = [];
    BF1 = [];
    BF = [];
    AS1 = [];
    AS = [];
    BS1 = [];
    BS = [];
    DQ = [];
    Q = [];
    for tt in range(0, (sec[pp]-1), 1):#will run for all sec
        AF1 = [];
        BF1 = [];
        AS1 = [];
        BS1 = [];
        XB1 = sec_matrix1[pp][tt][00];
        XE1 = sec_matrix1[pp][tt + 1][0];
        XF = XB1*(2/3) + XE1/3;
        XS = XE1*(2/3) + XB1/3;
        YB1 = sec_matrix1[pp][tt][1];
        YE1 = sec_matrix1[pp][tt + 1][1];
        YF = YB1*(2/3) + YE1/3;
        YS = YE1*(2/3) + YB1/3;
        ZB1 = sec_matrix1[pp][tt][2];
        ZE1 = sec_matrix1[pp][tt + 1][2];
        ZF = ZB1*(2/3) + ZE1/3;
        ZS = ZE1*(2/3)+ ZB1/3;
        #print(XB1)
        #print(YB1)
        #print(ZB1)
        #print(XE1)
        #print(YE1)
        #print(ZE1)
        for ttt in range(0, (sec[pp]-1), 1):#will run for all sec
            #first=section_len2[pp][ttt]/3;# Sec_lenght/3;
            #second=(section_len2[pp][ttt]*2)/3;# 2*Sec_lenght/3;
            #third = section_len2[pp][ttt] *2/ 3;  # Sec_lenght/3;
            #forth = (section_len2[pp][ttt]) / 3;  # 2*Sec_lenght/3;
            XB = sec_matrix1[pp][ttt][0];
            XE = sec_matrix1[pp][ttt + 1][0];
            YB = sec_matrix1[pp][ttt][1]
            YE = sec_matrix1[pp][ttt + 1][1];
            ZB = sec_matrix1[pp][ttt][2];
            ZE = sec_matrix1[pp][ttt + 1][2];
            #print(XB)
            #print(YB)
            #print(ZB)
            #print(XE)
            #print(YE)
            #print(ZE)
            #print(first);
            #print(second);
            #print(third);
            #print(forth);
            LL = math.sqrt((XB - XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
            second=LL/3;# Sec_lenght/3;
            first=LL*2/3;# 2*Sec_lenght/3;
            forth=LL*2/3;  # Sec_lenght/3;
            third=LL/3;  # 2*Sec_lenght/3;
            #LL1=section_len2[pp][ttt]
            if tt==ttt:
              delta1 =  math.sqrt((first)*(first)+(eradi)*(eradi));
              delta2 = math.sqrt((second) * (second) + (eradi) * (eradi));
              Idelta1 = math.sqrt((first) * (first) + (eradi) * (eradi));
              Idelta2 = math.sqrt((second) * (second) + (eradi) * (eradi));
              delta3 = math.sqrt((third) * (third) + (eradi) * (eradi));
              delta4 = math.sqrt((forth) * (forth) + (eradi) * (eradi));
              Idelta3 = math.sqrt((third) * (third) + (eradi) * (eradi));
              Idelta4 = math.sqrt((forth) * (forth) + (eradi) * (eradi));
            else:
                #section_len, nsec, sec_matrix = sec_length(pp);
                #sec_cordi_xaxix, sec_cordi_height, cordi_span
              delta1 = math.sqrt((XF - XE) * (XF - XE) + (YF - YE) * (YF - YE) + (ZF - ZE) * (ZF - ZE));
              delta2 = math.sqrt((XF - XB) * (XF - XB) + (YF - YB) * (YF - YB) + (ZF - ZB) * (ZF - ZB));
              Idelta1 = math.sqrt((XF - XE) * (XF - XE) + (YF + YE) * (YF + YE) + (ZF - ZE) * (ZF - ZE));
              Idelta2 = math.sqrt((XF - XB) * (XF - XB) + (YF + YB) * (YF + YB) + (ZF - ZB) * (ZF - ZB));
              delta3 = math.sqrt((XS - XE) * (XS - XE) + (YS - YE) * (YS - YE) + (ZS - ZE) * (ZS - ZE));
              delta4 = math.sqrt((XS - XB) * (XS - XB) + (YS - YB) * (YS - YB) + (ZS - ZB) * (ZS - ZB));
              Idelta3 = math.sqrt((XS - XE) * (XS - XE) + (YS + YE) * (YS + YE) + (ZS - ZE) * (ZS - ZE));
              Idelta4 = math.sqrt((XS - XB) * (XS - XB) + (YS + YB) * (YS + YB) + (ZS - ZB) * (ZS - ZB));

            #seg_height = ele_height(pp, section_len2[pp][ttt]);
            V1= math.log(((delta1+delta2+LL)/(delta1+delta2-LL))*((Idelta1+Idelta2-LL)/(Idelta1+Idelta2+LL)),math.e)
            V2=((delta1-delta2)/LL)-((Idelta1-Idelta2)/LL)+((Idelta1*Idelta1-Idelta2*Idelta2)/(2*LL*LL))*(math.log(((Idelta1+Idelta2+LL)/(Idelta1+Idelta2-LL)), math.e))-(((delta1*delta1-delta2*delta2)/(2*LL*LL))*(math.log(((delta1+delta2+LL)/(delta1+delta2-LL)),math.e)));
            AF1.insert(ttt,V1)
            BF1.insert(ttt,V2);
            V3 = math.log(((delta3+delta4+LL)/(delta3+delta4-LL))*((Idelta3+Idelta4-LL)/(Idelta3+Idelta4+LL)),math.e)
            V4 = ((delta3-delta4)/LL)-((Idelta3-Idelta4)/LL)+((Idelta3*Idelta3-Idelta4*Idelta4)/(2*LL*LL)*(math.log(((Idelta3+Idelta4+LL)/(Idelta3+Idelta4-LL)),math.e))) - (((delta3*delta3-delta4*delta4)/(2*LL*LL)) * (math.log(((delta3+delta4+LL)/(delta3+delta4-LL)), math.e)));
            AS1.insert(ttt,V3);
            BS1.insert(ttt,V4);
        #print(AF1)
        AF.insert(tt,AF1);
        BF.insert(tt,BF1);
        AS.insert(tt,AS1);
        BS.insert(tt,BS1);
    #Vreal=
    #Vimag=
    #print (Voltage_imag)
     #print(one);
    #print(sss);
    #print(numpy.subtract(one,sss));
    #print(Voltage);
    INVERSE_AF = numpy.linalg.inv(AF);
    voltage = sec_voltage(pp);
    sss = numpy.matmul(AS, INVERSE_AF);
    one = numpy.identity((sec[pp] - 1));
    DQ1_real=numpy.matmul(numpy.subtract(one,sss),voltage);
    DQ2_real=numpy.matmul(sss,BF);
    DQ3_real=numpy.subtract(BS,DQ2_real);
    DQ4_real= numpy.linalg.inv(DQ3_real);
    DQ=numpy.matmul(DQ1_real,DQ4_real);#DQ is equal to DQ/4*pi*E
    DQ_real=DQ.real;
    DQ_imag=DQ.imag;
    jjj=numpy.matmul(INVERSE_AF ,(voltage));
    kkk=numpy.matmul(numpy.matmul(INVERSE_AF, BF),DQ);
    Q=numpy.subtract(jjj,kkk);##in nano columb #DQ is equal to DQ/4*pi*E
    Q_real=Q.real;
    Q_imag=Q.imag;
    return DQ_real,Q_real,DQ_imag,Q_imag
E=[];
#print(m)
#print (sec_matrix1)
for gg in range(0, (div+1), 1): #FOR EACH MEASUREMENT point
    E_xreal = 0;
    E_yreal = 0;
    E_zreal = 0;
    E_ximag = 0;
    E_yimag = 0;
    E_zimag = 0;
    for www in range(0, nphase, 1):
        DQ_real,Q_real,DQ_imag,Q_imag = seg_matrix(www);# loop executing 20 times for Q DQ
        Q_vreal= Q_real;
        DQ_vreal= DQ_real;
        Q_vimag= Q_imag;
        DQ_vimag= DQ_imag;
        #print(DQ_real);
        #print(DQ_imag);
        #print(Q_real);
        #print(Q_imag);
        #print(len(DQ_real));
        #print(len(DQ_imag));
        #print(len(Q_real));
        #print(len(Q_imag));
        #print (len(sec_matrix1[0]));
        for tttt in range(0, sec[www]-1, 1):
            XB = sec_matrix1[www][tttt][0];
            XE = sec_matrix1[www][tttt+1][0];
            YB = sec_matrix1[www][tttt][1];
            YE = sec_matrix1[www][tttt + 1][1];
            ZB = sec_matrix1[www][tttt][2];
            ZE = sec_matrix1[www][tttt + 1][2];
            #print (sec_matrix1[www])
            #print(XB)
            #print(YB)
            #print(ZB)
            #print(XE)
            #print(YE)
            #print(ZE)
            XT=  m[gg][0];
            YT = m[gg][1];
            ZT = m[gg][2];
            #print(XT)
            #print(YT)
            #print(ZT)
            L = math.sqrt((XB-XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
            D1 = math.sqrt((XT-XE) * (XT-XE) + (YT - YE) * (YT - YE) + (ZT - ZE) * (ZT - ZE))
            D2 = math.sqrt((XT-XB) * (XT - XB) + (YT - YB) * (YT - YB) + (ZT - ZB) * (ZT - ZB))
            D3 = math.sqrt((XT-XE) * (XT - XE) + (YT + YE) * (YT + YE) + (ZT - ZE) * (ZT - ZE))
            D4 = math.sqrt((XT-XB) * (XT - XB) + (YT + YB) * (YT + YB) + (ZT - ZB) * (ZT - ZB))
            A =(((D1*D1-D2*D2)-(L*L))/(2*L));
            A1 = (((D3*D3-D4*D4)-(L*L))/(2*L));

            E_orthomain_real=((Q_real[tttt]-(DQ_real[tttt]*(D1*D1-D2*D2)/(2*L*L)))*((2*L*(D1+D2))/(D1*D2*(D1+D2-L)*(D1+D2+L))))-(((DQ_real[tttt])/L)*(1/D1-1/D2));# Main conductor orthogonal component
            E_orthomain_xreal= E_orthomain_real*(XB-((A/L)*(XE-XB))-XT);  # ortho component main conductor along x direction
            E_orthomain_yreal = E_orthomain_real*(YB-((A/L)*(YE-YB))-YT); # ortho component main conductor along y direction
            E_orthomain_zreal = E_orthomain_real*(ZB-((A/L)*(ZE-ZB))-ZT); # ortho component main conductor along z direction

            E_paramain_real=(Q_real[tttt]*(1/D2-1/D1))+ ((DQ_real[tttt]/L)*math.log((D1+D2+L)/(D1+D2-L),math.e))-((DQ_real[tttt]*(D1+D2))/(2*D1*D2));# Main conductor parallel component
            E_paramain_xreal = E_paramain_real*((XE-XB)/L); # para component main conductor along x direction
            E_paramain_yreal = E_paramain_real*((YE-YB)/L);  # para component main conductor along y direction
            E_paramain_zreal = E_paramain_real*((ZE-ZB)/L);  # para component main conductor along z direction

            E_orthomain_imag=((Q_imag[tttt]-(DQ_imag[tttt]*(D1*D1-D2*D2)/(2*L*L)))*((2*L*(D1+D2))/(D1*D2*(D1+D2-L)*(D1+D2+L))))-(((DQ_imag[tttt])/L)*(1/D1-1/D2));# Main conductor orthogonal component
            E_orthomain_ximag= E_orthomain_imag*(XB-((A/L)*(XE-XB))-XT);  # ortho component main conductor along x direction
            E_orthomain_yimag = E_orthomain_imag*(YB-((A/L)*(YE-YB))-YT); # ortho component main conductor along y direction
            E_orthomain_zimag = E_orthomain_imag*(ZB-((A/L)*(ZE-ZB))-ZT); # ortho component main conductor along z direction

            E_paramain_imag=(Q_imag[tttt]*(1/D2-1/D1))+ ((DQ_imag[tttt]/L)*math.log((D1+D2+L)/(D1+D2-L),math.e))-((DQ_imag[tttt]*(D1+D2))/(2*D1*D2));# Main conductor parallel component
            E_paramain_ximag = E_paramain_imag*((XE-XB)/L); # para component main conductor along x direction
            E_paramain_yimag = E_paramain_imag*((YE-YB)/L);  # para component main conductor along y direction
            E_paramain_zimag = E_paramain_imag*((ZE-ZB)/L);  # para component main conductor along z direction

            ### virtual conductor calculation
            E_orthovirt_real=((Q_vreal[tttt]-(DQ_vreal[tttt]*(D3*D3-D4*D4)/(2*L*L)))*((2*L*(D3+D4))/(D3*D4*(D3+D4-L)*(D3+D4+L))))-(((DQ_vreal[tttt])/L)*(1/D3-1/D4));# Main conductor orthogonal component
            E_orthovirt_xreal= E_orthovirt_real*(XB-((A1/L)*(XE-XB))-XT);  # ortho component imaginary/virtual conductor along x direction
            E_orthovirt_yreal = E_orthovirt_real*(-YB-((A1/L)*(-YE+YB))-YT); # ortho component imaginary/virtual conductor along y direction
            E_orthovirt_zreal = E_orthovirt_real*(ZB-((A1/L)*(ZE-ZB))-ZT); # ortho component imaginary/virtual conductor along z direction

            E_paravirt_real= (Q_vreal[tttt]*(1/D4-1/D3))+ ((DQ_vreal[tttt]/L)*math.log((D3+D4+L)/(D3+D4-L),math.e))-((DQ_vreal[tttt]*(D3+D4))/(2*D3*D4));# Imaginery conductor parallel component# Main conductor parallel component
            E_paravirt_xreal = E_paravirt_real*((XE-XB)/L); # para component main conductor along x direction
            E_paravirt_yreal = E_paravirt_real*((-YE+YB)/L);  # para component main conductor along y direction
            E_paravirt_zreal = E_paravirt_real*((ZE-ZB)/L);  # para component main conductor along z direction

            E_orthovirt_imag=((Q_vimag[tttt]-(DQ_vimag[tttt]*(D3*D3-D4*D4)/(2*L*L)))*((2*L*(D3+D4))/(D3*D4*(D3+D4-L)*(D3+D4+L))))-(((DQ_vimag[tttt])/L)*(1/D3-1/D4));# Main conductor orthogonal component
            E_orthovirt_ximag= E_orthovirt_imag*(XB-((A1/L)*(XE-XB))-XT);  # ortho component imaginary/virtual conductor along x direction
            E_orthovirt_yimag = E_orthovirt_imag*(-YB-((A1/L)*(-YE+YB))-YT); # ortho component imaginary/virtual conductor along y direction
            E_orthovirt_zimag = E_orthovirt_imag*(ZB-((A1/L)*(ZE-ZB))-ZT); # ortho component imaginary/virtual conductor along z direction

            E_paravirt_imag= (Q_vimag[tttt]*(1/D4-1/D3))+ ((DQ_vimag[tttt]/L)*math.log((D3+D4+L)/(D3+D4-L),math.e))-((DQ_vimag[tttt]*(D3+D4))/(2*D3*D4));# Main conductor parallel component
            E_paravirt_ximag = E_paravirt_imag*((XE-XB)/L); # para component main conductor along x direction
            E_paravirt_yimag = E_paravirt_imag*((-YE+YB)/L);  # para component main conductor along y direction
            E_paravirt_zimag = E_paravirt_imag*((ZE-ZB)/L);  # para component main conductor along z direction

            ## main conductor total axis wise real component
            E_main_xreal = E_orthomain_xreal + E_paramain_xreal;
            E_main_yreal = E_orthomain_yreal + E_paramain_yreal;
            E_main_zreal = E_orthomain_zreal + E_paramain_zreal;

            ## main conductor total axis wise imag component
            E_main_ximag = E_orthomain_ximag + E_paramain_ximag;
            E_main_yimag = E_orthomain_yimag + E_paramain_yimag;
            E_main_zimag = E_orthomain_zimag + E_paramain_zimag;

            ## virtual conductor total axis wise real component
            E_virt_xreal = E_orthovirt_xreal + E_paravirt_xreal;
            E_virt_yreal = E_orthovirt_yreal + E_paravirt_yreal;
            E_virt_zreal = E_orthovirt_zreal + E_paravirt_zreal;

            ## virtual conductor total axis wise imag component
            E_virt_ximag = E_orthovirt_ximag + E_paravirt_ximag;
            E_virt_yimag = E_orthovirt_yimag + E_paravirt_yimag;
            E_virt_zimag = E_orthovirt_zimag + E_paravirt_zimag;

            # real component of Electric field
            E_realx = E_main_xreal - E_virt_xreal;
            E_realy = E_main_yreal - E_virt_yreal;
            E_realz = E_main_zreal - E_virt_zreal;
            # imanginery component of Electric field
            E_imagx = E_main_ximag - E_virt_ximag;
            E_imagy = E_main_yimag - E_virt_yimag;
            E_imagz = E_main_zimag - E_virt_zimag;

            E_xreal = E_xreal + E_realx;
            E_yreal = E_yreal + E_realy;
            E_zreal = E_zreal + E_realz;
            E_ximag = E_ximag + E_imagx;
            E_yimag = E_yimag + E_imagy;
            E_zimag = E_zimag + E_imagz;

        FINAL_E=math.sqrt(E_xreal*E_xreal +E_yreal*E_yreal+E_zreal*E_zreal+E_ximag*E_ximag+E_yimag*E_yimag+E_zimag*E_zimag);
        print(FINAL_E)
    E.insert(gg,FINAL_E);


