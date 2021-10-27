#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Sniper import PyAlgBase


##############################################################################
# Numpy is installed by default in JUNO offline software
##############################################################################
try:
    import numpy as np
except:
    np = None

##############################################################################
# Torch could be installed by following command:
#
#   pip install --user torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html 
#
# Reference: https://pytorch.org/get-started/locally/
#
##############################################################################
try:
    import torch
except:
    torch = None # if no torch found

##############################################################################
# Tensorflow could also be installed with dedicated install prefix by following command:
#
#   pip install --target /tmp/lint/juno-J21v2r0-branch-testing/tensorflow tensorflow
#
# Then you need to add this path to sys.path
#  export PYTHONPATH=/tmp/lint/juno-J21v2r0-branch-testing/tensorflow:$PYTHONPATH
#
# Note: the tensorflow may install its own numpy, which could cause problem. 
#
##############################################################################
try:
    import tensorflow as tf
except:
    tf = None



class DummyPyAlg(PyAlgBase):

    def __init__(self, name):
        PyAlgBase.__init__(self, name)
        self.pmtid = None
        self.npe = None
        self.hittime = None

    def initialize(self):
        self.datastore = self.get("DataStore").data()

        return True

    def execute(self):
        pmtid = None
        npe = None
        hittime = None

        # Get pmtid/npe/hittime
        self.pmtid = self.access_array("pmtid")
        self.npe = self.access_array("npe")
        self.hittime = self.access_array("hittime")

        if self.pmtid is None:
            print("array pmtid not found. ")
            return False
        if self.npe is None:
            print("array npe not found. ")
            return False
        if self.hittime is None:
            print("array hittime not found. ")
            return False

        if np:
            self.process_data_in_numpy()
        # Test if pytorch is installed
        if torch:
            self.process_data_in_torch()
        # Test if tensorflow is installed
        if tf:
            self.process_data_in_tensorflow()

        return True

    def finalize(self):
        return True

    ##########################################################################
    # HELPERS
    ##########################################################################
    def access_array(self, name):
        import ExamplePyAlg
        if hasattr(ExamplePyAlg, name):
            print("Get %s from module ExamplePyAlg"%name)
            return getattr(ExamplePyAlg, name)
        elif "pmtid" in self.datastore:
            print("Get %s from PyDataStore"%name)
            return self.datastore[name]
        else:
            print("Can't get %s in the store."%name)
            print(self.datastore)

    def process_data_in_numpy(self):
        # calculate the sum of nPE
        totalpe = np.sum(self.npe)
        print("Total PE (numpy): ", totalpe)

        # calculate the mean of hittime
        meanhittime = np.mean(self.hittime)
        print("Mean hit time (numpy): ", meanhittime)

    def process_data_in_torch(self):
        # calculate the sum of nPE
        npe = torch.from_numpy(self.npe)
        totalpe = torch.sum(npe)
        print("Total PE (torch): ", totalpe)

        # calculate the mean of hittime
        hittime = torch.from_numpy(self.hittime)
        meanhittime = torch.mean(hittime)
        print("Mean hit time (torch): ", meanhittime)

    def process_data_in_tensorflow(self):
        # calculate the sum of nPE
        npe = self.npe
        totalpe = tf.math.reduce_sum(npe)
        print("Total PE (tensorflow): ", totalpe)

        # calculate the mean of hittime
        hittime = self.hittime
        meanhittime = tf.math.reduce_mean(hittime)
        print("Mean hit time (tensorflow): ", meanhittime)

