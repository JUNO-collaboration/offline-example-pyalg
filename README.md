# JUNO Offline Example (Python Algorithm)

## Quickstart

```bash
$ git clone git@github.com:JUNO-collaboration/offline-example-pyalg.git
$ cd offline-example-pyalg
$ source /cvmfs/juno.ihep.ac.cn/centos7_amd64_gcc830/Pre-Release/J21v2r0-branch/setup.sh
$ ./build.sh
$ source InstallArea/setup.sh

$ # Run detector simulation, the EDM data sample_detsim.root will be generated.
$ python $TUTORIALROOT/share/tut_detsim.py gun
$ python ExamplePyAlg/share/run.py
```

In the Python algorithm, it will try to use numpy, torch and tensorflow to process the data. 
The numpy is installed in the JUNO offline software by default.
If you need to install torch or tensorflow, please run following commands.

```bash
$ mkdir pyinstalled
$ pip install -t pyinstalled tensorflow torch # In this example, will tensorflow 2.6 (protobuf 3.9.2)
$ pip install -t pyinstalled -U protobuf==3.9.2 six==1.15.0 # To work with tensorflow 2.6
$ rm -rf pyinstalled/numpy* # remove local numpy
$ export PYTHONPATH=$(pwd)/pyinstalled:$PYTHONPATH
$ python ExamplePyAlg/share/run.py
```

