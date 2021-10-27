#include "Edm2NumpyAlg.hh"

#include "SniperKernel/AlgBase.h"
#include "SniperKernel/AlgFactory.h"
#include "SniperKernel/SniperLog.h"
#include "SniperKernel/SniperPtr.h"

#include "SniperPython/PyDataStore.h"

#include "EvtNavigator/NavBuffer.h"

namespace p = boost::python;
namespace np = boost::python::numpy;


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

    np::initialize();

    return true;
}

bool Edm2NumpyAlg::execute() {
    // = prepare =
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

    // = convert hit to numpy array =
    auto hit_collection = simevt->getCDHitsVec();
    auto hit_col_size = hit_collection.size();
    if (not hit_col_size) {
        LogInfo << "Skip the event due to empty collection. " << std::endl;
        return true;
    }

    p::tuple shape = p::make_tuple(hit_col_size);
    np::dtype dtype_int = np::dtype::get_builtin<int>();
    np::dtype dtype_double = np::dtype::get_builtin<double>();

    np::ndarray arr_pmtid = np::zeros(shape, dtype_int);
    np::ndarray arr_npe = np::zeros(shape, dtype_int);
    np::ndarray arr_hittime = np::zeros(shape, dtype_double);

    int hit_counter = 0;
    for (auto hit: hit_collection) {
        int pmtid = hit->getPMTID();
        int npe = hit->getNPE();
        double hittime = hit->getHitTime();

        arr_pmtid[hit_counter] = pmtid;
        arr_npe[hit_counter] = npe;
        arr_hittime[hit_counter] = hittime;

        ++hit_counter;
    }

    // register them 

    SniperDataPtr<PyDataStore> pystore(*getRoot(), "DataStore");
    if (pystore.invalid()) {
        LogError << "Failed to find the PyDataStore. Register the value to module " << std::endl;

        p::object this_module = p::import("ExamplePyAlg");
        this_module.attr("pmtid") = arr_pmtid;
        this_module.attr("npe") = arr_npe;
        this_module.attr("hittime") = arr_hittime;
    } else {
        LogInfo << "Register the value to PyDataStore. " << std::endl;
        pystore->set("pmtid", arr_pmtid);
        pystore->set("npe", arr_npe);
        pystore->set("hittime", arr_hittime);
    }



    return true;
}

bool Edm2NumpyAlg::finalize() {
    return true;
}
