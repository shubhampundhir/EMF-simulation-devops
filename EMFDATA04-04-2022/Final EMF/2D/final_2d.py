# Add units of measurements particularly for span, electric field
# show a figure showing x y z co-ordinate system
# check output of measurement function next week and compare with matlab
# install numpy module
import cmath
import math
import numpy
import cmath
import matplotlib.pyplot as plt
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
V=[(-151.6+262.5j),(303.1+0j),(-151.6-262.5j)]; # in kV
# code for fetching voltage and phase angle data automatically
#a=1;
Vm=[];
Pm=[];
V=[];
#for a in range(0,nphase,1):
 #   print('Phase %d ' %(a+1))
  #  voltage = float(input('RMS Line-Line voltage magnitude in kV='));
  #  Vm.append(voltage);
  #  print('Phase %d ' %(a+1))
  #  phase=float(input('phase angle in degree='));
   # Pm.append(phase)
   # x=math.cos(float (Pm[a])*((22/7)/180))
   # y=math.sin(float(Pm[a])*((22/7)/180))
   # V.append(Vm[a]/math.sqrt(3)*complex(x,y))
# print(Vm);
# print(Pm);
# print (V)
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
#step=round(float(input('No. of step(integer value)=')));
#step=19;
div = round(float(input('Enter No. of Sub divisions=')));

# TO ACCOUNT FOR ADDITIONAL VALUE INCORPORATED AT MIN CLEARANCE
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
x_inc = (x_end - x_start) / div;
y_inc = (y_end - y_start) / div;
z_inc = (z_end - z_start) / div;

if x_inc == 0:
    for ar in numpy.arange(0,(div + 1),1):
        # X.append(x_start)
        X.insert(ar, x_start)
else:
    X.insert(0, x_start)
    for ar in numpy.arange(1, (div + 1),1):
        # X.append(x_start)
        X.insert(ar,(X[ar-1]+x_inc))
if y_inc == 0:
    for ar in numpy.arange(0,(div + 1), 1):
        Y.insert(ar, y_start)
else:
    Y.insert(0, y_start)
    for ar in numpy.arange(1, (div + 1), 1):
        # X.append(x_start)
        Y.insert(ar, (Y[ar - 1] + y_inc))
if z_inc == 0:
    for ar in numpy.arange(0,(div + 1), 1):
        Z.insert(ar, z_start)
else:
    Z.insert(0, z_start)
    for ar in numpy.arange(1, (div + 1), 1):
        # X.append(x_start)
        Z.insert(ar, (Z[ar - 1] + z_inc))

#print(X)
#print(Y)
#print(Z)
m= numpy.array([X, Y, Z]);
m=numpy.transpose(m)
print(m);


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
    #print (Y1);
    return Y1


for ii in range(0, div + 1, 1):
    measurement_height = [];
    for r in range(0, nphase, 1):
        conductor_yaxix = ele_height(r,m[ii][2]);
        measurement_height.insert(r,conductor_yaxix)
    final_height.insert(ii,measurement_height);


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
# heights of conductor
P=[];
Cap=[];
def Magnetic(y, m, V, H):
    Ex =0;
    Ey =0;
    #print(m);
    #calculatuion of distance of point from all conductor
    xx=m[y][0]; # extracting x-cordinate from m
    yy=m[y][1]; # extracting y-cordinate from m
    for zz in range(0, nphase, 1):
        X= xx - condx_axis[zz];
        V= H[zz][zz] - yy;
        HI = (H[zz][zz] + yy);
        #X=xx -condx_axis[zz] horizontal distance
        #V=H[zz][zz] - y vertical distance
        D = ((X*X)+(V*V));
        DI = (X*X+HI*HI);
        Ex = Ex+(Q[0][zz]*X/D-Q[0][zz]*X/DI)*18;
        Ey = Ey+(-Q[0][zz]*V/D-Q[0][zz]*HI/DI)*18;
        # Ex = Ex + ((Q[0][zz]*(xx -condx_axis[zz])/D) - (Q[0][zz] * (xx -condx_axis[zz]/DI)))*18;
        #Ey = Ey + ((Q[0][zz]*(H[zz][zz]-yy)/D) - (Q[0][zz]*(H[zz][zz]+yy) / DI)) * 18;
    #print(Ex)
    #print(Ey)
    E1=cmath.sqrt(Ex.real*Ex.real+Ey.real*Ey.real+Ex.imag*Ex.imag+Ey.imag*Ey.imag)*1000;#v/meter
    #print(E1)
    return E1
E=[];
for y in range(0, (div+1), 1):

    Z, H = Capacitor(y); #P matrix whose inverse is having capacitance
    P.insert(y,Z) #nano range
    #print(P[y])
    Cap.insert(y,numpy.linalg.inv(P[y]));#nano range
    #print(Cap[y]);
    Q = numpy.dot(Cap,V); #micro range
    #print(Q)
    E.insert(y,Magnetic(y,m,Q,H));
#cc=[];
#for y in range(0, (div+1), 1):
  #  cc.insert(y,m[y][2]);
#print(E)
#print(final)
#plt.plot(cc,E)
   # plt.ylabel('some numbers')
#plt.show()
   #print(E[y])

