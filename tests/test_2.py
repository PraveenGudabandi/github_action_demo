#test_2.py
import os,sys
sys.path.insert(0,os.getcwd())

from script import addition
def test_data_tyep():
    subj=addition(2,3)
    assert isinstance(subj,int)