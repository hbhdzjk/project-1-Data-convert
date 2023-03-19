
import scipy.io as scio
import numpy as np
import sys,os
import pytest
from nanonispy import read

def test_imcomplete_3ds(self):
    fn_sxm_incomplete='..\\data_test\\不完整非对称\\1001.sxm'
    fn=fn_sxm_incomplete
    data_sxm=read.Scan(fn)
    
    raw_header={}
    fname='temp.mat'
    raw_header['savepath']=fname
    raw_header['header']=data_sxm.header
    read.Write(data_sxm,raw_header,'sxm','3ds')
    print('sb')
    temp=read.Grid(fn)