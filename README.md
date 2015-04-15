# factor
Various implementations of integer factoring

## simple-factor.py
The simple implementation of integer factoring in Python 2.
Simply change the value of N to select what value to factor.
Ultimately prints a list of tuples containing each factor pair.

$ #for N=pow(2,50)
$ time ./simple-factor.py > /dev/null

real    0m10.614s
user    0m10.597s
sys     0m0.009s

## threading-factor.py
The more complex yet worse performing version of integer factoring.
This is also in Python 2 although very few changes would be needed
for it to work in Python 3. Uses the threading module. Since this is
very CPU-bound, the performace is worse that the simple factoring version.
This is due to the GIL. 
Details on GIL: http://www.dabeaz.com/python/UnderstandingGIL.pdf

$ #for N=pow(2,50)
$ time ./threading-factor.py > /dev/null

real    0m21.520s
user    0m21.809s
sys     0m7.298s
