#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Sniper import PyAlgBase

class DummyPyAlg(PyAlgBase):

    def __init__(self, name):
        PyAlgBase.__init__(self, name)

    def initialize(self):
        self.datastore = self.get("DataStore").data()

        return True

    def execute(self):
        pmtid = None
        npe = None
        hittime = None

        # Get pmtid/npe/hittime
        pmtid = self.access_array("pmtid")
        npe = self.access_array("npe")
        hittime = self.access_array("hittime")

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
