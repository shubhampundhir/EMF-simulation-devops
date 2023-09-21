import cmath
import math
import numpy
# Inputs of the long transmission line
#d = float(input('diameter of the one strand in Cm='));
d = 3.5;
#n = int(input('total number of strand in bundle='));
n = 1;
#s = float(input('space between any 2 strand='));
s = 45.7;
#nphase = int(input('total no of phases='));
nphase = 8;
pi = cmath.pi;
db = s / math.sin(pi/n);
eradi = n*d/db;
eradi = math.pow(eradi, 1/n);
eradi = eradi*db/2;
eradi = eradi/100;
Im=[442.2,442.2,442.2,442.2,442.2,442.2,0,0]; # Current array
#Im=[100*math.sqrt(3)]; # Current array
Pm=[0,120,240,0,120,240,0,0]; # phase angle array
h111=[29,43.6,60.5,29,43.6,60.5,72.9,72.9];
h222=[29,43.6,60.5,29,43.6,60.5,72.9,72.9];
x_cor=[12.5,11.1,10,-12.5,-11.1,-10,10.4,-10.4];
min_cle11=[18.2,32.8,49.6,18.2,32.8,49.6,61.5,61.5];
#V=[(-151.6+262.5j),(303.1+0j),(-151.6-262.5j)]; # in kV
# code for fetching voltage and phase angle data automatically
a=0;
#Vm=[];
#Pm=[];
I=[];
span=386;
#span = float(input('span length='));
weight=0.35;
for a in range(0,nphase,1):
    #print('Phase %d ' %(a+1))
    #voltage = float(input('RMS Line-Line voltage magnitude in kV='));
    #Vm.append(voltage);
    #print('Phase %d ' %(a+1))
    #phase=float(input('phase angle in degree='));
    #Pm.append(phase)
    x=math.cos(float (Pm[a])*((22/7)/180));
    y=math.sin(float(Pm[a])*((22/7)/180));
    I.append((Im[a])*complex(x,y));
print (I)
####### VOLTAGE FOR EACH SECTION TO CALCULATE Q, DQ
def sec_voltage(qq):
    each_sec_voltage = [];
    each_sec_voltage_real=[];
    each_sec_voltage_imag=[];
    for vv in range(0, (sec[qq]-1), 1):
        each_sec_voltage.insert(vv,I[qq])
        each_sec_voltage_real.insert(vv, I[qq].real)
        each_sec_voltage_imag.insert(vv, I[qq].imag)
    #each_sec_volatge1=numpy.reshape(each_sec_volatge,((sec[qq]-1),1))
    #print(each_sec_volatge_imag)
    #print(each_sec_volatge_real)
    return each_sec_voltage

condx_axis=[];
profile=[];
h1=[];
h2=[];
min_cle=[];
s1=[];
s2=[];
D=[];
b=0;
######### X-CORDINATE AND MAX-SAG  CALCULATION FOR ALL PHASES
def cordinates(a):
    #print('cordinate of conductor %d ' % (a + 1))
    #cond_x_axis1 = float(input('x cordinate='));
    cond_x_axis1 =x_cor[a];
    #profile2 = float(input('for Flat conductor profile press 1 and Catenary conductor profile press 2='));
    #profile1=round(profile2);
    profile1=2;
    if profile1 == 2 or  profile1 == 1:
        #h11 = float(input('starting tower height='));
        #h11=5;
        #h22=5;
        h11=h111[a];
        h22=h222[a];
        #h22 = float((input('ending tower height=')));
        if profile1 == 2:
            #min_cle1 = float(input('min clearance='));
            min_cle1 = min_cle11[a];
        elif profile1 == 1:
            if h11 > h22:
                min_cle1=h22
            else:
                min_cle1=h11
        h1.insert(a,h11);
        h2.insert(a,h22);
        condx_axis.insert(a,cond_x_axis1);
        #print(condx_axis);
        profile.insert(a,profile1);
        min_cle.insert(a,min_cle1);
        s1.append((h1[a] - min_cle[a]));
        s2.append((h2[a] - min_cle[a]));
        #print (s1)
        #print (s2)
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
######### MEASUREMENT POINT CALCULATION
#div = round(float(input('Enter No. of Sub divisions=')));
cond_div=19;
div=20;
#def measurement(div):
X=[];
Y=[];
Z=[];
#x_start = float(input('starting x cordinate of measured point='));
x_start= -32;
#x_end = float(input('ending x cordinate of measured point='));
x_end = 32;
#y_start = float(input('starting y cordinate of measured point='));
y_start = 1;
#y_end = float(input('ending y cordinate of measured point='));
y_end = 1;
#z_start = float(input('starting z cordinate of measured point='));
z_start =193;
#z_end = float (input('ending z cordinate of measured point='));
z_end =193;
x_inc = ((x_end - x_start)/div);
y_inc = ((y_end - y_start)/div);
z_inc = ((z_end - z_start)/div);
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

m=numpy.array([X, Y, Z]);# MEASUREMENT POINTS MATRIX
m=numpy.transpose(m)
#print(m);
####### HEIGHT calculation for all conductors at particular location
final = []
conductor_span = [];
conductor_yaxix = [];
conductor_xaxix = [];
final_height = [];
sec = [];
# print(sec)
# print(final)
# print(conductor_span)
# final_height=[];
# return final_height
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
            # print(min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = (To / weight * (math.cosh(weight * (min - mmm1) / To) - 1)) + min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1 - min) / To) - 1)) + min_cle[a];
        elif (s2 > s1):
            # print (min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * (span - min) * (span - min) / (2 * s2);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = (To / weight * (math.cosh(weight * (min - mmm1) / To) - 1)) + min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1 - min) / To) - 1)) + min_cle[a];
        elif (s1 == s2):
            # print (min);# min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            if mmm1 < min:
                Y1 = (To / weight * (math.cosh(weight * (min - mmm1) / To) - 1)) + min_cle[a];
            else:
                Y1 = (To / weight * (math.cosh(weight * (mmm1 - min) / To) - 1)) + min_cle[a];
    else:
        Y1 = h2[a] + (h2[a] - h1[a]) / span * (mmm1 - span);
    return Y1
####### Section matrix for all section of particular phase
def sec_length(a):
    sec_len = [];
    sec_len1 = [];
    sec = span/cond_div;
    cordi_span = [];  # starting and ending point each section
    sec_cordi_height = [];  # height at each sec point
    sec_cordi_xaxix = [];
    if profile[a] == 2:
        # distance of lowest point of conductor from the taller support
        # if statement is required for choosing taller support
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
            D = s1/s2;
            min = span * math.sqrt(D) / (1 + math.sqrt(D));  # min is basically x-axis point along the span at which min clearnace exists
            To = weight * min * min / (2 * s1);  # To = weight * x * x / (2 * max_sag)
            aa = 0;
            for yyy in numpy.arange(min, 0, -sec):
                cordi_span.insert(aa, (min-yyy))
                sec_cordi_height.insert(aa, ele_height(a, (min-yyy)))
                sec_cordi_xaxix.insert(aa, condx_axis[a])
                sec_len1.insert(aa, To / weight * (math.sinh(weight * yyy / To)))
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
            for yyyy in range(0, (div+1), 1):
                cordi_span.insert(yyyy, xxx)

                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                sec_len1.insert(yyyy,span/(div) )
                xxx = xxx + sec;
        else:
            for yyyy in range(0, (div+1), 1):
                cordi_span.insert(yyyy, xxx)
                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                diagonal_length=math.sqrt((h1[a] - h2[a])*(h1[a] - h2[a])+span*span)
                sec_len1.insert(yyyy,diagonal_length/(div) )
                xxx = xxx + sec;

    #print(To / weight * (math.sinh(weight *400/To)))
    #print(sec_len1)
    mm = numpy.array([sec_cordi_xaxix, sec_cordi_height, cordi_span]);
    mm = numpy.transpose(mm)
    #print (sec_cordi_height)
    #print (len(sec_cordi_height))
    #print (sec_len1)
    #print (len(sec_len1))
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
   #print(sec_matrix);
   sec.insert(ww,nsec)
   sec_matrix1.insert(ww,sec_matrix);
   for www in range(1, nsec, 1):
     section_len1.insert(www-1,abs(section_len[www]-section_len[www-1]))
   section_len2.insert(ww,section_len1)
   section_len1=[];

#print(sec_matrix1);

for j in range(0,div+1,1):
    Bx=0;
    By=0;
    Bz=0;
    Xp=m[j][0];
    Yp=m[j][1];
    Zp=m[j][2];
    #print(Xp);
    #print(Yp);
    #print(Zp);
    for jj in range(0,nphase,1):
        for jjj in range(0,cond_div,1):
            Xb = sec_matrix1[jj][jjj][0];
            Xe = sec_matrix1[jj][jjj + 1][0];
            Yb = sec_matrix1[jj][jjj][1];
            Ye = sec_matrix1[jj][jjj + 1][1];
            Zb = sec_matrix1[jj][jjj][2];
            Ze = sec_matrix1[jj][jjj + 1][2];
            #print(sec_matrix1[jj]);
            #print(Xb);
            #print(Yb);
            #print(Zb);
            #print(Xe);
            #print(Ye);
            #print(Ze);
            a = Xe - Xb;
            b = Ye - Yb;
            c = Ze - Zb;
            #print(a);
            #print(b);
            #print (c);
            #print (a * a + b * b + c * c);
            La =((Xp-Xb)*a+(Yp-Yb)*b+(Zp-Zb)*c)/(a*a+b*b+c*c);
            #print (La)
            Xs=(a) * La + Xb;
            Ys=(b) * La + Yb;
            Zs=(c) * La + Zb;
            Re = math.sqrt((Xp - Xe) * (Xp - Xe) + (Yp - Ye) * (Yp - Ye) + (Zp - Ze) * (Zp - Ze));
            Rb = math.sqrt((Xp - Xb) * (Xp - Xb) + (Yp - Yb) * (Yp - Yb) + (Zp - Zb) * (Zp - Zb));
            D = math.sqrt((Xp - Xs) * (Xp - Xs) + (Yp - Ys) * (Yp - Ys) + (Zp - Zs) * (Zp - Zs));
            #print (Re);
            #print(Rb);
            Bx=Bx+((I[jj])/(D*D)*((La)/(Rb)+(1-La)/(Re))*((Zp-Zs)*b-(Yp-Ys)*c)*10e-8);
            By=By+((I[jj])/(D*D)*((La)/(Rb)+(1-La)/(Re))*((Xp-Xs)*c-(Zp-Zs)*a)*10e-8);
            Bz=Bz +((I[jj])/(D*D)*((La)/(Rb)+(1-La)/(Re))*((Yp-Ys)*a-(Xp-Xs)*b)*10e-8);
            #print(Bx);
            #print(By);
            #print(Bz);
    B=cmath.sqrt(Bx*Bx+By*By+Bz*Bz);
    print (abs(B));

print (eradi)







