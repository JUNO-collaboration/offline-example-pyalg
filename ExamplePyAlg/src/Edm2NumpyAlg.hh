#ifndef Edm2NumpyAlg_hh
#define Edm2NumpyAlg_hh

#include <SniperKernel/AlgBase.h>

#include <EvtNavigator/NavBuffer.h>
#include <Event/SimHeader.h>

#include <boost/python/numpy.hpp>

class Edm2NumpyAlg: public AlgBase {
public:
    Edm2NumpyAlg(const std::string& name);
    
    bool initialize();
    bool execute();
    bool finalize();

private:
    JM::NavBuffer* m_buf;
};

#endif
