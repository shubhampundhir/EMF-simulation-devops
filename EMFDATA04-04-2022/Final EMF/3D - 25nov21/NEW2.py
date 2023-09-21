# Add units of measurements particularly for span, electric field
# show a figure showing x y z co-ordinate system
# check output of measurement function next week and compare with matlab
# install numpy module
import cmath
import math
import numpy
import cmath
#import matplotlib.pyplot as plt
# import cmath
#import array
# Inputs of the long transmission line
d = float(input('diameter of the one strand in Cm='));
#d = 3.5;
n = int(input('total number of strand in bundle='));
#n = 5;
s = float(input('space between any 2 strand='));
#s = 45.7;
nphase = int(input('total no of phases='));
#nphase = 3
pi=22/7;
db = s / math.sin(pi/n)
eradi = n*d/db
eradi = math.pow(eradi, 1/n)
eradi = eradi*db/2;
print(eradi)

#Vm=[525, 525, 525]; # Voltage array
#Pm=[120, 0, 240]; # phase angle array
#V=[(-151.6+262.5j),(303.1+0j),(-151.6-262.5j)]; # in kV
# code for fetching voltage and phase angle data automatically
#a=1;
Vm=[];
Pm=[];
V=[];
for a in range(0,nphase,1):
    print('Phase %d ' %(a+1))
    voltage = float(input('RMS Line-Line voltage magnitude in kV='));
    Vm.append(voltage);
    print('Phase %d ' %(a+1))
    phase=float(input('phase angle in degree='));
    Pm.append(phase)
    x=math.cos(float (Pm[a])*((22/7)/180))
    y=math.sin(float(Pm[a])*((22/7)/180))
    V.append(Vm[a]/math.sqrt(3)*complex(x,y))
# print(Vm);
# print(Pm);
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
    print('cordinate of conductor %d ' % (a + 1))
    cond_x_axis1 = float(input('x cordinate='));
    profile2 = float(input('for Flat conductor profile press 1 and Catenary conductor profile press 2='));
    profile1=round(profile2);
    if profile1 == 2 or  profile1 == 1:
        h11 = float(input('starting tower height='));
        h22 = float((input('ending tower height=')));
        if profile1 == 2:
            min_cle1 = float(input('min clearance='));
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
step=round(float(input('No. of step(integer value)=')));
#step=19;
div = round(float(input('Enter No. of Sub divisions=')));
#div=19;

#def measurement(div):
X=[];
Y=[];
Z=[];
x_start = float(input('starting x cordinate of measured point='));
x_end = float(input('ending x cordinate of measured point='));
y_start = float(input('starting y cordinate of measured point='));
y_end = float(input('ending y cordinate of measured point='));
z_start = float(input('starting z cordinate of measured point='));
z_end = float (input('ending z cordinate of measured point='));
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

def mittal(a,mmm):
  if mmm==0:
      sec=span/div;
  else:
      sec=span/mmm;
  W = [];
  extra = [];
  extra1 = [];
  height = [];
  height1 = [];
  axix = [];
  if profile[a] == 2:
        #sec = span / mmm;
        # distance of lowest point of conductor from the taller support
        # if statement is required for ? choosing taller support
        s1 = h1[a] - min_cle[a];
        s2 = h2[a] - min_cle[a];
        if (s1>s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (1 + math.sqrt(D)); # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min/ (2 * s1); # To = weight * x * x / (2 * max_sag)
            s = 0;
            for p in numpy.arange(0, min, sec):

                 Y1 = s1-To / weight * (math.cosh(weight * p / To) - 1) + min_cle[a];
                 W.insert(s, Y1)
                 s = s + 1;
                # print(p)
            # print(p)
            # p=min;

            # Y1 = To / weight * (math.cosh(weight * (p - span) / To) - 1) + min_cle[a];
            # W.insert(s3, Y1)
            # s3 = s3 + 1;
            # d = d + 1;
            # print(p)
            for q in numpy.arange((p + sec), span, sec):
                # print(q)
                Y1 = s2-To / weight * (math.cosh(weight * (q - span) / To) - 1) + min_cle[a];
                W.insert(s, Y1)
                s = s + 1;
            # print(q)
            #print(W);
            #print(height);
            for dd in numpy.arange(0, span, sec):
                axix.append(dd);
            axix = numpy.append(axix, span).copy()
        elif(s2>s1):
            D = s2 / s1
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s2);  # To = weight * x * x / (2 * max_sag)
            s=0;
            for p in numpy.arange(0, min, sec):
                Y1 = s2-To / weight * (math.cosh(weight*p/To)-1)+min_cle[a];
                W.insert(s,Y1)
                s=s+1;
            #print(p)
            #print(p)
            #p=min;

            #Y1 = To / weight * (math.cosh(weight * (p - span) / To) - 1) + min_cle[a];
            #W.insert(s3, Y1)
            #s3 = s3 + 1;
            #d = d + 1;
            #print(p)
            for q in numpy.arange((p+sec), span, sec):
                #print(q)
                Y1 = s1-To / weight * (math.cosh(weight * (q-span) / To) - 1) + min_cle[a];
                W.insert(s,Y1)

                s=s+1;
            #print(q)
            #print(W)
            for dd in numpy.arange(0, span, sec):
                axix.append(dd);
            axix = numpy.append(axix, span).copy()
        elif(s1==s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (
                        1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            s = 0;
            for p in numpy.arange(0, min, sec):
                Y1 = s1-To / weight * (math.cosh(weight * p / To) - 1) + min_cle[a];
                W.insert(s, Y1)
                s = s + 1;
                # print(p)
            # print(p)
            # p=min;

            # Y1 = To / weight * (math.cosh(weight * (p - span) / To) - 1) + min_cle[a];
            # W.insert(s3, Y1)
            # s3 = s3 + 1;
            # d = d + 1;
            # print(p)
            for q in numpy.arange((p + sec), span, sec):
                # print(q)
                Y1 = s2-To / weight * (math.cosh(weight * (q - span) / To) - 1) + min_cle[a];
                W.insert(s, Y1)

                s = s+ 1;
            # print(q)
            #print(W);

            for dd in numpy.arange(0, span, sec):
                axix.append(round(dd));
            axix = numpy.append(axix, span).copy()
  else:
      #sec = span / mmm;
      mm = 0;
      for d in numpy.arange(0, span, sec):
          #print(d)
          e = h2[a] + (h2[a] - h1[a]) / span * (d - span);
          W.insert(mm,e)
          mm = mm + 1;
          d=d+sec
          e = h2[a] + (h2[a] - h1[a]) / span * (d - span);
          W.insert(mm,e)
      for dd in numpy.arange(0,span,sec):
          axix.append(round(dd));
      axix = numpy.append(axix,span).copy()
  #print(W);
  #print(axix);
  return W,axix
# final sag profiles for all conductors
final=[]
conductor_span=[];
conductor_yaxix=[];
conductor_xaxix=[];
final_height=[];
sec=[];
for ii in range(0, div + 1, 1):
  for r in range(0, nphase, 1):
    conductor_yaxix,conductor_xaxix=mittal(r,m[ii][2]);
    #print(conductor_yaxix)
    conductor_span.insert(r,conductor_xaxix);
    #print(conductor_span);

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
        if (s1 > s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = s1 - To / weight * (math.cosh(weight * mmm1/ To) - 1) + min_cle[a];
            else:
                Y1 = s2 - To / weight * (math.cosh(weight * (mmm1 - span) / To) - 1) + min_cle[a];

        elif (s2 > s1):
            D = s2 / s1
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s2);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = s1 - To / weight * (math.cosh(weight * mmm1 / To) - 1) + min_cle[a];
            else:
                Y1 = s2 - To / weight * (math.cosh(weight * (mmm1 - span) / To) - 1) + min_cle[a];


        elif (s1 == s2):
            D = s1 / s2
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1< min:
                Y1 = s1 - To / weight * (math.cosh(weight * mmm1 / To) - 1) + min_cle[a];
            else:
                Y1 = s2 - To / weight * (math.cosh(weight * (mmm1 - span) / To) - 1) + min_cle[a];
    else:
       Y1 = h2[a] + (h2[a] - h1[a]) / span * (mmm1 - span);


    return Y1


for ii in range(0, div + 1, 1):
    measurement_height = [];
    for r in range(0, nphase, 1):
        conductor_yaxix= ele_height(r,m[ii][2]);
        measurement_height.insert(r,conductor_yaxix)
    final_height.insert(ii,measurement_height);

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
    return sec_len1,len(sec_len1),mm
def length(a):
    A = []
    for s in range(0, nphase, 1):
        A.insert(s,(condx_axis[a]-condx_axis[s]))
    return A
# L is distance between the conductors based on co-ordinates
L=[]
for t in range(0, nphase, 1):
    L.insert(t,length(t))
#print(L)
def Capacitor(y):
    Z = [0] * nphase
    H = [0] * nphase
    for x in range(nphase):
       H[x] = [0] * nphase
       Z[x] = [0] * nphase

    for R in range (0, nphase, 1):
        for C in range(0, nphase, 1):
            if R == C:
                H[R][C] = final_height[y][R]
    #print(H)
    for w in range(0, nphase, 1):
         for x in range(0, nphase, 1):
            if w==x:
              Z[w][x] = 18*math.log((2*100*H[w][x])/eradi,math.e);
              #print (Z)
            else:
                AA=math.sqrt(L[w][x] * L[w][x] + (H[x][x] - H[w][w]) * (H[x][x] - H[w][w]));
                BB=math.sqrt(L[w][x] * L[w][x] + (H[x][x] + H[w][w]) * (H[x][x] + H[w][w]));
                Z[w][x]=18 * math.log(BB/AA,math.e);
                #print(Z)
    return Z,H
# heights of conducto

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
   sec.insert(ww,nsec)
   sec_matrix1.insert(ww,sec_matrix);
   for www in range(1, nsec, 1):
     section_len1.insert(www-1,abs(section_len[www]-section_len[www-1]))
   section_len2.insert(ww,section_len1)

   section_len1=[];
#print(sec_matrix1)
"""

print(sec_matrix1[0])
print(sec_matrix1[0][0])
print(sec_matrix1[0][0][0])"""
#sec_matrix1[0][0][0]  x_cordinatre of 1st sec
#sec_matrix1[0][0][1]  y_cordinatre of 1st sec
#sec_matrix1[0][0][2]  z_cordinatre of 1st sec
def sec_mes(ss):
    measurement_sec = [];
    for www in range(0, div+1, 1):
        measurement_sec.insert(www,m[ss])
    return measurement_sec

#shubh=sec_mes(1);
#shubh[0][0])x_cordinatre of 1st sec of mesa
#shubh[0][1])y_cordinatre of 1st sec of mesa
#shubh[0][2])z_cordinatre of 1st sec of mesa

def sec_voltage(qq):
    each_sec_volatge = [];
    for vv in range(0, (sec[qq]-1), 1):
        each_sec_volatge.insert(vv,V[qq])

    #each_sec_volatge1=numpy.reshape(each_sec_volatge,((sec[qq]-1),1))
    print(each_sec_volatge)
    return each_sec_volatge
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
        XF = (2*XB1) / 3 + (XE1 * 1) / 3;
        XS = (2*XE1) / 3 + (XB1 * 1) / 3;
        YB1 = sec_matrix1[pp][tt][1];
        YE1 = sec_matrix1[pp][tt + 1][1];
        YF = (2*YB1) / 3 + (YE1 * 1) / 3;
        YS = (2*YE1) / 3 + (YB1 * 1) / 3;
        ZB1 = sec_matrix1[pp][tt][2];
        ZE1 = sec_matrix1[pp][tt + 1][2];
        ZF = (2*ZB1) / 3 + (ZE1 * 1) / 3;
        ZS = (2*ZE1) / 3 + (ZB1 * 1) / 3;
        for ttt in range(0, (sec[pp]-1), 1):#will run for all sec
            first=section_len2[pp][ttt]/3;# Sec_lenght/3;
            second=(section_len2[pp][ttt]*2)/3;# 2*Sec_lenght/3;
            third = section_len2[pp][ttt] *2/ 3;  # Sec_lenght/3;
            forth = (section_len2[pp][ttt] ) / 3;  # 2*Sec_lenght/3;
            XB = sec_matrix1[pp][ttt][0];
            XE = sec_matrix1[pp][ttt + 1][0];
            YB = sec_matrix1[pp][ttt][1]
            YE = sec_matrix1[pp][ttt + 1][1];
            ZB = sec_matrix1[pp][ttt][2]
            ZE = sec_matrix1[pp][ttt + 1][2]

            LL = math.sqrt((XB - XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
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
                delta1 = math.sqrt((XF-XE)*(XF-XE)+(YF-YE)*(YF-YE)+(ZF-ZE)*(ZF-ZE));
                delta2 = math.sqrt((XF-XB)*(XF-XB)+(YF-YB)*(YF-YB)+(ZF-ZB)*(ZF-ZB));
                Idelta1 = math.sqrt((XF - XE) * (XF - XE) + (YF + YE) * (YF + YE) + (ZF - ZE) * (ZF - ZE));
                Idelta2 = math.sqrt((XF - XB) * (XF - XB) + (YF + YB) * (YF + YB) + (ZF - ZB) * (ZF - ZB));
                delta3 = math.sqrt((XS - XE) * (XS - XE) + (YS - YE) * (YS - YE) + (ZS - ZE) * (ZS - ZE));
                delta4 = math.sqrt((XS - XB) * (XS - XB) + (YS - YB) * (YS - YB) + (ZS - ZB) * (ZS - ZB));
                Idelta3 = math.sqrt((XS - XE) * (XS - XE) + (YS + YE) * (YS + YE) + (ZS - ZE) * (ZS - ZE));
                Idelta4 = math.sqrt((XS - XB) * (XS - XB) + (YS + YB) * (YS + YB) + (ZS - ZB) * (ZS - ZB));
            seg_height = ele_height(pp, section_len2[pp][ttt]);
            V1= math.log(((delta1+delta2+LL)/(delta1+delta2-LL))*((Idelta1+Idelta2-LL)/(Idelta1+Idelta2+LL)),math.e)
            V2=((delta1-delta2)/LL)-((Idelta1-Idelta2)/LL)+((Idelta1*Idelta1-Idelta2*Idelta2)/(2*LL*LL))*(math.log(((Idelta1+Idelta2+LL)/(Idelta1+Idelta2-LL)), math.e))-((delta1*delta1-delta2*delta2)/(2*LL*LL)*(math.log(((delta1+delta2+LL)/(delta1+delta2-LL)), math.e)));
            AF1.insert(ttt,V1)
            BF1.insert(ttt,V2);
            V3 = math.log((delta3 + delta4 + LL) / (delta3 + delta4 - LL) * ((Idelta3 + Idelta4 - LL) / (Idelta3 + Idelta4 + LL)), math.e)
            V4 = (delta3 - delta4) / LL - (Idelta3 - Idelta4) / LL + ((Idelta3 * Idelta3 - Idelta4 * Idelta4) / (2 * LL * LL) * math.log(((Idelta3 + Idelta4 - LL) / (Idelta3 + Idelta4 + LL)),math.e)) - ((delta3 * delta3 - delta4 * delta4) / (  2 * LL * LL) * math.log(((delta3 + delta4 + LL) / (delta3 + delta4 - LL)), math.e));
            AS1.insert(ttt, V3);
            BS1.insert(ttt, V4);
        #print(AF1)
        AF.insert(tt,AF1);
        BF.insert(tt, BF1);
        AS.insert(tt, AS1);
        BS.insert(tt, BS1);

    INVERSE_AF=numpy.linalg.inv(AF);
    Voltage=sec_voltage(pp);
    sss=numpy.matmul(AS,INVERSE_AF);
    one=numpy.identity((sec[pp]-1));
    #print(one);
    #print(sss);
    #print(numpy.subtract(one,sss));
    #print(Voltage);
    DQ1=numpy.matmul(numpy.subtract(one,sss),Voltage);
    print(DQ1);
    DQ1=DQ1/9;#in nano columb
    jjj=numpy.matmul(INVERSE_AF ,(Voltage));
    jjj=jjj/9;
    kkk=numpy.matmul(numpy.matmul(INVERSE_AF, BF), DQ1);
    Q1=numpy.subtract(jjj,kkk);##in nano columb
    #print(DQ1)
    #print(Q1)
    return DQ1,Q1
E=[];
for gg in range(0, (div+1), 1): #FOR EACH MEASUREMENT point
    EX_MAIN = 0;
    EX_IMAG = 0;
    EY_MAIN = 0;
    EY_IMAG = 0;
    EZ_MAIN = 0;
    EZ_IMAG = 0;
    for www in range(0, nphase, 1):
        DQ,Q = seg_matrix(www);
        for tttt in range(0, sec[www]-1, 1):
            XB = sec_matrix1[www][tttt][0];
            XE = sec_matrix1[www][tttt+1][0];
            YB = sec_matrix1[www][tttt][1]
            YE = sec_matrix1[www][tttt + 1][1]
            ZB = sec_matrix1[www][tttt][2]
            ZE = sec_matrix1[www][tttt + 1][2]
            XT=  m[gg][0];
            YT = m[gg][1];
            ZT = m[gg][2];
            L = math.sqrt((XB - XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
            D1 = math.sqrt((XT - XE) * (XT - XE) + (YT - YE) * (YT - YE) + (ZT - ZE) * (ZT - ZE))
            D2 = math.sqrt((XT - XB) * (XT - XB) + (YT - YB) * (YT - YB) + (ZT - ZB) * (ZT - ZB))
            D3 = math.sqrt((XT - XE) * (XT - XE) + (YT + YE) * (YT + YE) + (ZT - ZE) * (ZT - ZE))
            D4 = math.sqrt((XT - XB) * (XT - XB) + (YT + YB) * (YT + YB) + (ZT - ZB) * (ZT - ZB))
            A=(((D1*D1-D2*D2)-L*L)/(2*L));
            B=math.sqrt(D2*D2-A*A);
            C=(2*L*(D1+D2))/(D1*D2*(D1+D2-L)*(D1+D2+L));
            D=((DQ[tttt]*B)/L)*(1/D1-1/D2)
            E1_MAIN=((Q[tttt]-(DQ[tttt]*(D1*D1-D2*D2))/2*(L*L))*(B*C)-D)/9;
            E=(DQ[tttt]/L)*math.log((D1+D2+L)/(D1+D2-L),math.e)
            F=(DQ[tttt]*(D1+D2))/(2*D1*D2);
            E1_DESS_MAIN=((Q[tttt]*(1/D2-1/D1))+ E-F)/9;
            A1 = ((D3 * D3 - D4 * D4) - L * L) / (2 * L);
            B1 = math.sqrt(D4 * D4 - A1 * A1);
            C1 = (2 * L * (D3 + D4)) / (D3 * D4 * (D3 + D4 - L)*(D3 + D4 + L));
            D11= ((DQ[tttt] * B1) / L) * (1 / D3 - 1 / D4)
            E1_IMAG = ((Q[tttt] - (DQ[tttt] * (D3 * D3 - D4 * D4)) / 2 * (L * L)) * (B1 * C1) - D11)/9;
            E1 = (DQ[tttt] / L) * math.log((D3 + D4 + L) / (D3 + D4 - L), math.e)
            F1 = (DQ[tttt] * (D3+D4))/(2*D3*D4);
            E1_DESS_IMAG = ((Q[tttt] - (1/D3-1/D4))+ E1-F1)/9;
            E_XMAIN=E1_MAIN*(XB - A/L*(XE-XB)-XT)
            E_DESS_XMAIN=E1_DESS_MAIN*((XE-XB)/L);
            E_XIMAG = E1_IMAG * (XB - A / L * (XE - XB) - XT)
            E_DESS_XIMAG = E1_DESS_MAIN * ((XE - XB) / L);
            EX_MAIN = EX_MAIN+(E_XMAIN + E_DESS_XMAIN);
            EX_IMAG = EX_IMAG+(E_XIMAG + E_DESS_XIMAG);
            E_YMAIN = E1_MAIN * (YB - A / L * (YE - YB) - YT)
            E_DESS_YMAIN = E1_DESS_MAIN * ((YE - YB) / L);
            E_YIMAG = E1_IMAG * (YB - A / L * (YE - YB) - YT)
            E_DESS_YIMAG = E1_DESS_MAIN * ((YE - YB) / L);
            EY_MAIN = EY_MAIN + (E_YMAIN + E_DESS_YMAIN);
            EY_IMAG = EY_IMAG + (E_YIMAG + E_DESS_YIMAG);
            E_ZMAIN = E1_MAIN * (ZB - A / L * (ZE - ZB) - ZT)
            E_DESS_ZMAIN = E1_DESS_MAIN * ((ZE - ZB) / L);
            E_ZIMAG = E1_IMAG * (ZB - A / L * (ZE - ZB) - ZT)
            E_DESS_ZIMAG = E1_DESS_MAIN * ((ZE - ZB) / L);
            EZ_MAIN = EZ_MAIN + (E_ZMAIN + E_DESS_ZMAIN);
            EZ_IMAG = EZ_IMAG + (E_ZIMAG + E_DESS_ZIMAG);
    FINAL_E=cmath.sqrt(EX_MAIN*EX_MAIN+EX_IMAG*EX_IMAG+EY_MAIN*EY_MAIN+EY_IMAG*EY_IMAG+EZ_MAIN*EZ_MAIN+EZ_IMAG*EZ_IMAG)
    print(FINAL_E)

    #E.insert(gg,FINAL_E);

