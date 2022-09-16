find_package(Boost COMPONENTS numpy)

PKG(ExamplePyAlg
    DEPENDS
        junosw::SimEvent
        Boost::numpy
)
