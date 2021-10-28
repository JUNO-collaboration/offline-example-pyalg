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

