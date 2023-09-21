import cmath
import math
import numpy
print(abs(3+4j))

AF.insert(tt, AF1);
BF.insert(tt, BF1);
AS.insert(tt, AS1);
BS.insert(tt, BS1);
# print(AF);
# AF=numpy.transpose(AF)
# print(AF);
# BF=numpy.transpose(BF)
# AS=numpy.transpose(AS)
# BS=numpy.transpose(BS)
# Vreal=
# Vimag=
# print (Voltage_imag)
# print(one);
# print(AF);
# print(numpy.subtract(one,sss));
# print(Voltage);
INVERSE_AF = numpy.linalg.inv(AF);
# print(INVERSE_AF);
voltage = sec_voltage(pp);
sss = numpy.matmul(AS, INVERSE_AF);
one = numpy.identity((sec[pp] - 1));
DQ1_real = numpy.matmul(numpy.subtract(one, sss), voltage);
DQ2_real = numpy.matmul(sss, BF);
DQ3_real = numpy.subtract(BS, DQ2_real);
DQ4_real = numpy.linalg.inv(DQ3_real);
DQ = numpy.matmul(DQ1_real, DQ4_real);  # DQ is equal to DQ/4*pi*E
DQ_real = DQ.real;
DQ_imag = DQ.imag;
jjj = numpy.matmul(INVERSE_AF, (voltage));
kkk = numpy.matmul(numpy.matmul(INVERSE_AF, BF), DQ);
Q = numpy.subtract(jjj, kkk);  ##in nano columb #DQ is equal to DQ/4*pi*E
Q_real = Q.real;
Q_imag = Q.imag;
return DQ_real, Q_real, DQ_imag, Q_imag