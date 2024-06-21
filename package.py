name = "osl"

version = "1.13.7.0"

description = \
    """
    Open Shading Language (OSL) is a small but rich language for programmable
    shading in advanced renderers and other applications, ideal for describing
    materials, lights, displacement, and pattern generation.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "pugixml",
    "oiio-2.5.9.0", # it will bring OpenEXR, boost, etc
]

private_build_requires = [
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
    ["python-3.10"],
]

build_system = "cmake"
uuid = "repository.OpenShadingLanguage"

# run rez-build -i or rez-release with CMake directives:
# rez-build -i -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass


def commands():
    env.OSL_LOCATION = "{root}"
    env.OSL_ROOT = "{root}"
    env.OSL_INCLUDE_DIR = "{root}/include"
    env.OSL_LIBRARY_DIR = "{root}/lib64"

    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    env.PATH.append("{root}/bin")
