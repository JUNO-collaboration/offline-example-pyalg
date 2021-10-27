find_package(Boost COMPONENTS numpy)

PKG(ExamplePyAlg
    DEPENDS
        offline::SimEventV2
        Boost::numpy
)
