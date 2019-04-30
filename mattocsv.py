import numpy.linalg
import numpy.random
import scipy.stats
import scipy.io
import argparse
import numpy
import math
import sys
import os

import os.path

if __name__ == "__main__" :

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-m","--rmat-filename", help="Observed transition matrix filename", \
            type=str, required=True, dest="rmatfilename")
    parser.add_argument("-b", "--imat-filename", help="Rewards matrix filename", \
            type=str, required=True, dest="imatfilename")
    parser.add_argument("-M", "--name-of-matrix", help="Name of the observed transition matrix ", \
            type=str, required=False, default="ms", dest="nameofmatrix")
    parser.add_argument("-B", "--name-of-bpmatrix", help="Name of the rewards matrix ", \
            type=str, required=False, default="i_r", dest="nameofbpmatrix")
    
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()


    namebp = args.nameofbpmatrix
    filename1 = args.rmatfilename
    filename2 = args.imatfilename
    namems = args.nameofmatrix
    
    errmsg = []
    
    if not (os.path.isfile(filename1)):
        print "File " + filename1 + " does not exist"
        exit(1)
    
    if not (os.path.isfile(filename2)):
        print "File ", filename2, " does not exist"
        exit(1)
    
    msd = scipy.io.loadmat(filename1)
    bpd = scipy.io.loadmat(filename2)
    
    if not(namems in msd.keys()):
        print "Cannot find " + namems + " in " + filename1
        print msd.keys()
        exit(1)
    
    if not(namebp in bpd.keys()):
        print "Cannot find " + namebp + " in " + filename2
        print bpd.keys()
        exit(1)
    
    if msd[namems].shape[0] != bpd[namebp].shape[0]:
        print "wrong dim of the input matrix"
        exit(1)
    
    ms = msd[namems]
    ir = bpd[namebp]

    print "2"
    print namems
    print ms.shape[0], " , ", ms.shape[1] 
    for i in range(ms.shape[0]):
        for j in range(ms.shape[1]-1):
            sys.stdout.write( str(ms[i, j]) + " , ")
        sys.stdout.write( str(ms[i, -1]) + "\n")

    print namebp 
    print ir.shape[0], " , ", ir.shape[1]
    for i in range(ir.shape[0]):
        for j in range(ir.shape[1]-1):
            sys.stdout.write( str(ir[i, j]) + " , ")
        sys.stdout.write( str(ir[i, -1]) + "\n")
    
