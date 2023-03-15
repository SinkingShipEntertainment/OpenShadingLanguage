name = "osl"

version = "1.12.10.0"

description = \
    """
    Open Shading Language (OSL) is a small but rich language for programmable
    shading in advanced renderers and other applications, ideal for describing
    materials, lights, displacement, and pattern generation.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "boost-1.76.0",
    "openexr-3.1.5",
    "oiio-2.3.15.0.sse.2",
    "pybind11",
    "numpy",
    "pugixml",
]

private_build_requires = [
    "llvm-15.0.7",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7.7"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9.7"],
]

build_system = "cmake"

uuid = "repository.OpenShadingLanguage"

# run rez-build -i or rez-release with CMake directives:
# rez-build -i -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.OSL_LOCATION = "{root}"
    env.OSL_ROOT = "{root}"
    env.OSL_INCLUDE_DIR = "{root}/include"
    env.OSL_LIBRARY_DIR = "{root}/lib64"

    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PATH.append("{root}/bin")