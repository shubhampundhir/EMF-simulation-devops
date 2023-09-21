import cmath
import math
import numpy
# Inputs of the long transmission line
#d = float(input('diameter of the one strand in Cm='));
d = 3.5;
#n = int(input('total number of strand in bundle='));
n = 6;
#s = float(input('space between any 2 strand='));
s = 45.7;
#nphase = int(input('total no of phases='));
nphase = 8;
pi = cmath.pi;
db = s / math.sin(pi/n);
eradi = n*d/db;
eradi = math.pow(eradi, 1/n);
eradi = eradi*db/2;
#eradi = 35.8;
eradi = eradi/100; #from cm to meter
print (eradi*2);
Vm=[442.2,442.2,442.2,442.2,442.2,442.2,0,0]; # phase to ground voltage array
Pm=[0,240,120,240,0,120,0,0]; # Phase angle array
h111=[29,43.7,60.5,29,43.7,60.5,72.9,72.9];
h222=[29,43.7,60.5,29,43.7,60.5,72.9,72.9];
min_cle11=[18.2,32.8,49.6,18.2,32.8,49.6,61.5,61.5];
x_cor=[-12.51,-11.081,-9.96,12.51,11.081,9.96,-10.356,10.356];
#V=[(-151.6+262.5j),(303.1+0j),(-151.6-262.5j)]; # in kV
# code for fetching voltage and phase angle data automatically
#Vm=[];
#Pm=[];
V=[];
span=386;
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
b=0;
######### X-CORDINATE AND MAX-SAG  CALCULATION FOR ALL PHASES
def cordinates(a):
    #print (a)
    #print('cordinate of conductor %d ' % (a + 1))
    #cond_x_axis1 = float(input('x cordinate='));
    cond_x_axis1 = x_cor[a];
    #profile2 = float(input('for Flat conductor profile press 1 and Catenary conductor profile press 2='));
    #profile1=round(profile2);
    profile1=1;
    if profile1 == 2 or  profile1 == 1:
        #h11 = float(input('starting tower height='));
        #h11=21.813;
        #h22=21.813;
        #h22 = float((input('ending tower
        # height=')));
        h11=h111[a];
        h22=h222[a];
        if profile1 == 2:
            #min_cle1 = float(input('min clearance='));
            #min_cle1=8.813;
            min_cle1=min_cle11[a];
        elif profile1 == 1:
            if h11 > h22:
                min_cle1=h22
            else:
                min_cle1=h11
        h1.insert(a,h11);
        h2.insert(a,h22);
        #print (min_cle1);
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
cond_div=1;
div=20;
#def measurement(div):
X=[];
Y=[];
Z=[];
#x_start = float(input('starting x cordinate of measured point='));
x_start = -32;
#x_end = float(input('ending x cordinate of measured point='));
x_end = 32;
#y_start = float(input('starting y cordinate of measured point='));
y_start = 1.8;
#y_end = float(input('ending y cordinate of measured point='));
y_end = 1.8;
#z_start = float(input('starting z cordinate of measured point='));
z_start = 193;
#z_end = float (input('ending z cordinate of measured point='));
z_end = 193;
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
m= numpy.array([X, Y, Z]);# MEASUREMENT POINTS MATRIX
m=numpy.transpose(m)
print(m);
####### HEIGHT calculation for all conductors at particular location
final=[]
conductor_span=[];
conductor_yaxix=[];
conductor_xaxix=[];
final_height=[];
sec=[];
#print(sec)
#print(final)
#print(conductor_span)
#final_height=[];
#return final_height
def ele_height(a, mmm1):
    sec = span/div;
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
            for yyyy in range(0, (cond_div+1), 1):
                cordi_span.insert(yyyy, xxx)
                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                sec_len1.insert(yyyy,span/(cond_div) )
                xxx = xxx + sec;
                #print (xxx)
        else:
            for yyyy in range(0, (cond_div+1), 1):
                cordi_span.insert(yyyy, xxx)
                sec_cordi_height.insert(yyyy, ele_height(a, xxx))
                sec_cordi_xaxix.insert(yyyy, condx_axis[a])
                diagonal_length=math.sqrt((h1[a] - h2[a])*(h1[a] - h2[a])+span*span)
                sec_len1.insert(yyyy,diagonal_length/(cond_div) )
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
print(sec_matrix1)
#print(len(section_len2[0]))

####### VOLTAGE FOR EACH SECTION TO CALCULATE Q, DQ
def sec_voltage():
    for a in range(0, nphase, 1):
        #print('Phase %d ' %(a+1))
        #voltage = float(input('RMS Line-Line voltage magnitude in kV='));
        #Vm.append(voltage);
        #print('Phase %d ' %(a+1))
        #phase=float(input('phase angle in degree='));
        #Pm.append(phase)
        x = math.cos(float(Pm[a]) * (cmath.pi/180));
        y = math.sin(float(Pm[a]) * (cmath.pi/180));
        V.append((Vm[a])*complex(x, y));
        #iq=cmath.rect(Vm[a],math.radians(Pm[a]));
        #print (iq)
        # V.append((Vm[a]/math.sqrt(3))*complex(x,y));
    each_sec_voltage = [];
    #print (type(each_sec_voltage))
    #print (numpy.shape (each_sec_voltage))
    for nn in range (0,nphase,1):
        for vv in range(0, cond_div, 1):
            each_sec_voltage.insert(nn*cond_div+vv,V[nn]*1000)
    #each_sec_volatge1=numpy.reshape(each_sec_volatge,((sec[qq]-1),1))
    #print(type(each_sec_voltage))
    #print(numpy.transpose(each_sec_voltage))
    #each_sec_voltage=numpy.transpose(each_sec_voltage)
    #print (numpy.shape (each_sec_voltage))
    #print(type(each_sec_voltage))
    #print((each_sec_voltage))
    #each_sec_voltage=[each_sec_voltage]
    #print (numpy.shape (each_sec_voltage))
    #print(type(each_sec_voltage))
    #print(sec_vol)
    #print(type (sec_vol))
    #print((numpy.transpose(sec_vol)))
    #print(type (numpy.transpose(sec_vol)))
    #print((numpy.transpose(numpy.transpose(sec_vol))))
    #print(type(numpy.transpose(numpy.transpose(sec_vol))))
    return each_sec_voltage
#each_sec_voltage=sec_voltage (0);
#print ((each_sec_voltage))len
#print (sec_matrix1)
def seg_matrix():
    AF = [];
    BF = [];
    AS = [];
    BS = [];
    for qq in range (0,nphase,1):#will run for all phases
        for tt in range(0, cond_div, 1):  # will run for all sec of above phases
            AF1 = [];
            BF1 = [];
            AS1 = [];
            BS1 = [];
            XB1 = sec_matrix1[qq][tt][00];
            XE1 = sec_matrix1[qq][tt + 1][0];
            XF = XB1*(2/3)+XE1/3;
            XS = XE1*(2/3)+XB1/3;
            YB1 = sec_matrix1[qq][tt][1];
            YE1 = sec_matrix1[qq][tt + 1][1];
            YF = YB1*(2/3)+YE1/3;
            YS = YE1*(2/3)+YB1/3;
            ZB1 = sec_matrix1[qq][tt][2];
            ZE1 = sec_matrix1[qq][tt + 1][2];
            ZF = ZB1*(2/3)+ZE1/3;
            ZS = ZE1*(2/3)+ZB1/3;
            #print(ZS);
            #print(XB1)
            #print(YB1)
            #print(ZB1)
            #print(XE1)
            #print(YE1)
            #print(ZE1)
            for pp in range(0, nphase, 1):  # will run for all phases of above section
                for ttt in range(0, cond_div, 1):#will run for all sec
                    XB = sec_matrix1[pp][ttt][0];
                    XE = sec_matrix1[pp][ttt + 1][0];
                    YB = sec_matrix1[pp][ttt][1]
                    YE = sec_matrix1[pp][ttt + 1][1];
                    ZB = sec_matrix1[pp][ttt][2];
                    ZE = sec_matrix1[pp][ttt + 1][2];
                    #print(XB)
                    #print(YB)
                    #print(ZB)
                    #print (pp)
                    #print(XE)
                    #print(YE)
                    #print(ZE)
                    LL = math.sqrt((XB - XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
                    first=LL*2/3;# 2*Sec_lenght/3;
                    second=LL/3;# Sec_lenght/3;
                    third=LL/3;  # 2*Sec_lenght/3;
                    forth=LL*2/3;  # Sec_lenght/3;
                    #print(first);
                    #print(second);
                    #print(third);
                    #print(forth);
                    #LL1=section_len2[pp][ttt]
                    if (tt==ttt) & (pp==qq):
                      delta1 = math.sqrt((first)*(first)+(eradi)*(eradi));
                      delta2 = math.sqrt((second)*(second) + (eradi) * (eradi));
                      delta3 = math.sqrt((third)*(third) + (eradi) * (eradi));
                      delta4 = math.sqrt((forth)*(forth) + (eradi) * (eradi));
                    else:
                      delta1 = math.sqrt((XF - XE) * (XF - XE) + (YF - YE) * (YF - YE) + (ZF - ZE) * (ZF - ZE));
                      delta2 = math.sqrt((XF - XB) * (XF - XB) + (YF - YB) * (YF - YB) + (ZF - ZB) * (ZF - ZB));
                      delta3 = math.sqrt((XS - XE) * (XS - XE) + (YS - YE) * (YS - YE) + (ZS - ZE) * (ZS - ZE));
                      delta4 = math.sqrt((XS - XB) * (XS - XB) + (YS - YB) * (YS - YB) + (ZS - ZB) * (ZS - ZB));
                    Idelta1 = math.sqrt((XF - XE) * (XF - XE) + (YF + YE) * (YF + YE) + (ZF - ZE) * (ZF - ZE));
                    Idelta2 = math.sqrt((XF - XB) * (XF - XB) + (YF + YB) * (YF + YB) + (ZF - ZB) * (ZF - ZB));
                    Idelta3 = math.sqrt((XS - XE) * (XS - XE) + (YS + YE) * (YS + YE) + (ZS - ZE) * (ZS - ZE));
                    Idelta4 = math.sqrt((XS - XB) * (XS - XB) + (YS + YB) * (YS + YB) + (ZS - ZB) * (ZS - ZB));
                    V1= math.log(((delta1+delta2+LL)/(delta1+delta2-LL))*((Idelta1+Idelta2-LL)/(Idelta1+Idelta2+LL)),math.e)
                    V2=((delta1-delta2)/LL)-((Idelta1-Idelta2)/LL)+((Idelta1*Idelta1-Idelta2*Idelta2)/(2*LL*LL))*(math.log(((Idelta1+Idelta2+LL)/(Idelta1+Idelta2-LL)), math.e))-(((delta1*delta1-delta2*delta2)/(2*LL*LL))*(math.log(((delta1+delta2+LL)/(delta1+delta2-LL)),math.e)));
                    AF1.insert(pp*cond_div+ttt,V1)
                    BF1.insert(pp*cond_div+ttt,V2);
                    V3 = math.log(((delta3+delta4+LL)/(delta3+delta4-LL))*((Idelta3+Idelta4-LL)/(Idelta3+Idelta4+LL)),math.e)
                    V4 = ((delta3-delta4)/LL)-((Idelta3-Idelta4)/LL)+((Idelta3*Idelta3-Idelta4*Idelta4)/(2*LL*LL)*(math.log(((Idelta3+Idelta4+LL)/(Idelta3+Idelta4-LL)),math.e))) - (((delta3*delta3-delta4*delta4)/(2*LL*LL)) * (math.log(((delta3+delta4+LL)/(delta3+delta4-LL)), math.e)));
                    AS1.insert(pp*cond_div+ttt,V3);
                    BS1.insert(pp*cond_div+ttt,V4);
                #print(numpy.shape(AF1));
                #print(AF1)
            #print(numpy.shape(AF1));
            #print(AF1)
            #print(BS1)
            #print(numpy.shape(AF1))
            #print(BF1)
            AF.insert(qq*cond_div+tt,AF1);
            #print(numpy.shape(AF));
            #print (AF)
            BF.insert(qq*cond_div+tt,BF1);
            AS.insert(qq*cond_div+tt,AS1);
            BS.insert(qq*cond_div+tt,BS1);
    #print(len (AF));
    #AF=numpy.transpose(AF)
    #print(AF);
    #print(numpy.shape(AF));
    #print(numpy.shape(BF));
    #print(numpy.shape(AS));
    #print(numpy.shape(BS));
    #BF=numpy.transpose(BF)
    #AS=numpy.transpose(AS)
    #BS=numpy.transpose(BS)
    #print(one);
    #print(AF);
    #print(numpy.subtract(one,sss));
    #print(Voltage);
    INVERSE_AF = numpy.linalg.inv(AF);
    #print (INVERSE_AF)
    #print(numpy.shape(INVERSE_AF));
    #INVERSE_AF = numpy.linalg.inv(INVERSE_AF);# AF again
    #print (INVERSE_AF)
    sss = numpy.matmul(AS, INVERSE_AF);
    #print(numpy.shape(sss));
    DQ2 = numpy.matmul(sss, BF);
    #print(numpy.shape(DQ2));
    DQ3 = numpy.subtract(BS, DQ2);
    #print(numpy.shape(DQ3));
    DQ4 = numpy.linalg.inv(DQ3);
    #print(numpy.shape(DQ4));
    voltage = [sec_voltage()];
    #print (voltage)
    one = numpy.identity((nphase*cond_div));
    #print (one)
    #print(numpy.shape(one));
    #print(numpy.shape (numpy.subtract(one,sss)))
    #print(numpy.shape(voltage));
    voltage=numpy.transpose(voltage)
    #print (voltage)
    #print(numpy.shape(voltage));
    DQ1=numpy.matmul(numpy.subtract(one,sss),(voltage));
    #print(numpy.shape(DQ1));
    DQ=numpy.matmul(DQ4,DQ1);#DQ is equal to DQ/4*pi*E
    #print (numpy.shape(DQ))
    #print (DQ)
    #print (sss)
    #print(DQ1_real)
    #print(DQ2_real)
    #print(DQ3_real);
    #print (numpy.shape(INVERSE_AF))
    #print (numpy.shape(voltage))
    jjj=numpy.matmul(INVERSE_AF,(voltage));
    #print (numpy.shape(jjj))
    kkk=numpy.matmul(numpy.matmul(INVERSE_AF, BF),DQ);
    #print (numpy.shape(jjj))
    #print (numpy.shape(kkk))
    Q=numpy.subtract(jjj,kkk);##in nano columb #DQ is equal to DQ/4*pi*E
    #print (numpy.shape(Q))
    #print (Q)
    #print(DQ)
    return DQ,Q
E=[];
Exxx=[];
Eyyy=[];
Ezzz=[];
#print(m)
#print (sec_matrix1)
DQ, Q = seg_matrix();  # loop executing 20 times for Q DQ
#print (DQ)
#print (Q)
for gg in range(0, div+1, 1):  # FOR EACH MEASUREMENT point
    #print (gg);
    XT = m[gg][0];
    YT = m[gg][1];
    ZT = m[gg][2];
    #print(XT)
    #print(YT)
    #print(ZT)
    Exx = 0;
    Eyy = 0;
    Ezz = 0;
    for www in range(0, nphase, 1):
        Ex = 0;
        Ey = 0;
        Ez = 0;
        for tttt in range(0, cond_div, 1): # FOR EACH conductor section
            XB = sec_matrix1[www][tttt][0];
            XE = sec_matrix1[www][tttt + 1][0];
            YB = sec_matrix1[www][tttt][1];
            YE = sec_matrix1[www][tttt + 1][1];
            ZB = sec_matrix1[www][tttt][2];
            ZE = sec_matrix1[www][tttt + 1][2];
            #print (sec_matrix1[www])
            #print(XB)
            #print(YB)
            # print(ZB)
            # print(XE)
            #print(YE)
            #print(ZE)
            # print (m)
            L = math.sqrt((XB - XE) * (XB - XE) + (YB - YE) * (YB - YE) + (ZB - ZE) * (ZB - ZE))
            D1 = math.sqrt((XT - XE) * (XT - XE) + (YT - YE) * (YT - YE) + (ZT - ZE) * (ZT - ZE))
            D2 = math.sqrt((XT - XB) * (XT - XB) + (YT - YB) * (YT - YB) + (ZT - ZB) * (ZT - ZB))
            D3 = math.sqrt((XT - XE) * (XT - XE) + (YT + YE) * (YT + YE) + (ZT - ZE) * (ZT - ZE))
            D4 = math.sqrt((XT - XB) * (XT - XB) + (YT + YB) * (YT + YB) + (ZT - ZB) * (ZT - ZB))
            A = (((D1*D1-D2*D2) - (L*L)) / (2*L));
            A1 = (((D3*D3-D4*D4) - (L*L)) / (2*L));

            E_orthomain = ((Q[www*cond_div+tttt] - (DQ[www*cond_div+tttt] * (D1 * D1 - D2 * D2) / (2 * L * L))) * ((2 * L * (D1 + D2)) / (D1 * D2 * (D1 + D2 - L) * (D1 + D2 + L)))) - (((DQ[www*cond_div+tttt]) / L) * (1 / D1 - 1 / D2));  # Main conductor orthogonal component
            E_orthomain_x = E_orthomain * (XB - ((A / L) * (XE - XB)) - XT);  # ortho component main conductor along x direction
            E_orthomain_y = E_orthomain * (YB - ((A / L) * (YE - YB)) - YT);  # ortho component main conductor along y direction
            E_orthomain_z = E_orthomain * (ZB - ((A / L) * (ZE - ZB)) - ZT);  # ortho component main conductor along z direction

            E_paramain = (Q[www*cond_div+tttt] * (1 / D2 - 1 / D1)) + ((DQ[www*cond_div+tttt] / L) * math.log((D1 + D2 + L) / (D1 + D2 - L), math.e)) - ((DQ[www*cond_div+tttt] * (D1 + D2)) / (2 * D1 * D2));  # Main conductor parallel component
            E_paramain_x = E_paramain * ((XE - XB) / L);  # para component main conductor along x direction
            E_paramain_y = E_paramain * ((YE - YB) / L);  # para component main conductor along y direction
            E_paramain_z = E_paramain * ((ZE - ZB) / L);  # para component main conductor along z direction

            ### virtual conductor calculation
            E_orthovirt = ((Q[www*cond_div+tttt] - (DQ[www*cond_div+tttt] * (D3 * D3 - D4 * D4) / (2 * L * L))) * ((2 * L * (D3 + D4)) / (D3 * D4 * (D3 + D4 - L) * (D3 + D4 + L)))) - (((DQ[www*cond_div+tttt]) / L) * (1 / D3 - 1 / D4));  # Main conductor orthogonal component
            E_orthovirt_x = E_orthovirt * (XB - ((A1 / L) * (XE - XB)) - XT);  # ortho component imaginary/virtual conductor along x direction
            E_orthovirt_y = E_orthovirt * (-YB - ((A1 / L) * (-YE + YB)) - YT);  # ortho component imaginary/virtual conductor along y direction
            E_orthovirt_z = E_orthovirt * (ZB - ((A1 / L) * (ZE - ZB)) - ZT);  # ortho component imaginary/virtual conductor along z direction

            E_paravirt = (Q[www*cond_div+tttt] * (1 / D4 - 1 / D3)) + ((DQ[www*cond_div+tttt] / L) * math.log((D3 + D4 + L) / (D3 + D4 - L), math.e)) - ((DQ[www*cond_div+tttt] * (D3 + D4)) / (2 * D3 * D4));  # Imaginery conductor parallel component# Main conductor parallel component
            E_paravirt_x = E_paravirt * ((XE - XB) / L);  # para component main conductor along x direction
            E_paravirt_y = E_paravirt * ((-YE + YB) / L);  # para component main conductor along y direction
            E_paravirt_z = E_paravirt * ((ZE - ZB) / L);  # para component main conductor along z direction

            ## main conductor total axis wise real component
            E_main_x = E_orthomain_x + E_paramain_x;
            E_main_y = E_orthomain_y + E_paramain_y;
            E_main_z = E_orthomain_z + E_paramain_z;

            ## virtual conductor total axis wise real component
            E_virt_x = E_orthovirt_x + E_paravirt_x;
            E_virt_y = E_orthovirt_y + E_paravirt_y;
            E_virt_z = E_orthovirt_z + E_paravirt_z;

            # real component of Electric field
            E_x = E_main_x - E_virt_x;
            E_y = E_main_y - E_virt_y;
            E_z = E_main_z - E_virt_z;

            Ex = Ex + E_x;
            Ey = Ey + E_y;
            Ez = Ez + E_z;
        Exx = Exx + Ex;
        Eyy = Eyy + Ey;
        Ezz = Ezz + Ez;
    FINAL_E = math.sqrt(Exx.real * Exx.real + Eyy.real * Eyy.real + Ezz.real * Ezz.real + Ezz.imag * Ezz.imag + Exx.imag * Exx.imag + Eyy.imag * Eyy.imag);
    ### OR
    #FINAL_E = math.sqrt(abs(Exx)*abs(Exx)+abs(Eyy)*abs(Eyy)+abs(Ezz)*abs(Ezz))
    ### OR
    #FINAL_E = cmath.sqrt(Exx.real * Exx.real + Eyy.real * Eyy.real + Ezz.real * Ezz.real + Ezz.imag * Ezz.imag + Exx.imag * Exx.imag + Eyy.imag * Eyy.imag);
    #print(abs(FINAL_E))
    print((FINAL_E))

    E.insert(gg,abs(FINAL_E));
print (E)
#print (div)
#print (len(E))
#print (sec[0])

