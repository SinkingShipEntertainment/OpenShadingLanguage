
# FindOpenEXR
set(OPENEXR_HOME $ENV{REZ_OPENEXR_ROOT})

# FindLLVM
set(LLVM_FIND_QUIETLY OFF)
set(LLVM_DIRECTORY $ENV{REZ_LLVM_ROOT})

# Set which python version to look for
set(REZ_BUILD_WITH_PYTHON_VERSION "2.7")
if($ENV{REZ_PYTHON_VERSION} EQUAL "3.7.7")
    set(REZ_BUILD_WITH_PYTHON_VERSION "3.7")
endif()

# FindBoost and FindPython
set(BOOST_CUSTOM 1)
set(Boost_VERSION 1.70)
set(BOOST_ROOT $ENV{REZ_BOOST_ROOT})
set(Boost_INCLUDE_DIRS $ENV{BOOST_INCLUDEDIR})
set(Boost_LIBRARY_DIRS $ENV{BOOST_LIBRARYDIR})
set(Boost_PYTHON_LIBRARIES $ENV{REZ_BOOST_ROOT}/lib)
set(Boost_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_filesystem.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_system.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_thread.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_regex.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_wave.so
)
set(Boost_PYTHON27_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_python27.so
)
set(Boost_PYTHON37_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_python37.so
)
