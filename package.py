name = "osl"

version = "1.8.12"

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
    "openexr-2.2.0",
    "oiio-1.8.9",
]

private_build_requires = [
    "cmake",
    "gcc",
    "llvm",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7", "boost-1.70.0"]
]

build_system = "cmake"

uuid = "repository.OpenShadingLanguage"

def commands():
    env.OSL_LOCATION = "{root}"
    env.OSL_ROOT = "{root}"
    env.OSL_INCLUDE_DIR = "{root}/include"
    env.OSL_LIBRARY_DIR = "{root}/lib"
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PATH.append("{root}/bin")
    env.PAYTHONPATH.append("{root}/lib/python/")
    env.PAYTHONPATH.append("{root}/lib/python3/")
