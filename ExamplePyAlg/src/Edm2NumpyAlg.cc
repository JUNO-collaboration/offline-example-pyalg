#include "Edm2NumpyAlg.hh"

#include "SniperKernel/AlgBase.h"
#include "SniperKernel/AlgFactory.h"
#include "SniperKernel/SniperLog.h"
#include "SniperKernel/SniperPtr.h"

#include "EvtNavigator/NavBuffer.h"

Edm2NumpyAlg::Edm2NumpyAlg(const std::string& name)
    : AlgBase(name) {

}

bool Edm2NumpyAlg::initialize() {
    return true;
}

bool Edm2NumpyAlg::execute() {
    return true;
}

bool Edm2NumpyAlg::finalize() {
    return true;
}
