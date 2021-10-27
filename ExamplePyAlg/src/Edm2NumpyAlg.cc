#include "Edm2NumpyAlg.hh"

#include "SniperKernel/AlgBase.h"
#include "SniperKernel/AlgFactory.h"
#include "SniperKernel/SniperLog.h"
#include "SniperKernel/SniperPtr.h"

#include "EvtNavigator/NavBuffer.h"

DECLARE_ALGORITHM(Edm2NumpyAlg);

Edm2NumpyAlg::Edm2NumpyAlg(const std::string& name)
    : AlgBase(name) {

}

bool Edm2NumpyAlg::initialize() {

    SniperDataPtr<JM::NavBuffer>  navBuf(*getRoot(), "/Event");

    if ( navBuf.invalid() ) {
        LogError << "cannot get the NavBuffer @ /Event" << std::endl;
        return false;
    }
    m_buf = navBuf.data();

    return true;
}

bool Edm2NumpyAlg::execute() {
    auto nav = m_buf->curEvt();
    if (not nav) {
        LogError << "Failed to find the event navigator. " << std::endl;
        return false;
    }

    auto simhdr = static_cast<JM::SimHeader*>(nav->getHeader("/Event/Sim"));
    if (not simhdr) {
        LogError << "Failed to find the SimHeader. " << std::endl;
        return false;
    }

    auto simevt = static_cast<JM::SimEvent*>(simhdr->event());
    if (not simevt) {
        LogError << "Failed to find the SimEvent. " << std::endl;
        return false;
    }

    LogInfo << "The SimEvent ID: " << simevt->getEventID() << std::endl;

    return true;
}

bool Edm2NumpyAlg::finalize() {
    return true;
}
