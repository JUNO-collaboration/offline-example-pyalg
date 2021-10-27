#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-*- author: Tao Lin -*-

##############################################################################
# Import
##############################################################################
from Tutorial import JUNOApplication
from Tutorial import JUNOModule
from Tutorial import JUNODataBufferModule
from Tutorial import JUNORootInputModule

##############################################################################
# Module definition
##############################################################################

class Edm2NumpyModule(JUNOModule):
    def __init__(self):
        pass

    def register_options(self, parser):
        pass

    def init(self, toptask, args):
        # Create a python store
        import SniperPython
        toptask.createSvc("PyDataStoreSvc/DataStore")

        # Create one algorithm in C++ to convert the EDM data to numpy
        # Create another algorithm in Python to process data
        import ExamplePyAlg
        import ExamplePyAlg.DummyPyAlg

        edm2numpy = toptask.createAlg("Edm2NumpyAlg")
        self.dummypyalg = ExamplePyAlg.DummyPyAlg.DummyPyAlg("DummyPyAlg")
        toptask.addAlg(self.dummypyalg)

##############################################################################
# Application
##############################################################################
juno_application = JUNOApplication(description="Convert SimEvent to numpy")
juno_application.set_default_input("sample_detsim.root")

databuffer_module = JUNODataBufferModule()
rootinput_module = JUNORootInputModule()
edm2numpy_module = Edm2NumpyModule()

juno_application.register(databuffer_module)
juno_application.register(rootinput_module)

juno_application.register(edm2numpy_module)

juno_application.run()
