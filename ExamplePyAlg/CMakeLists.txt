find_package(Boost COMPONENTS numpy)

PKG(ExamplePyAlg
    DEPENDS
        offline::SimEvent
        Boost::numpy
)
