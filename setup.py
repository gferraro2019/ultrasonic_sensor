from setuptools import find_packages, setup

from ultrasonic_sensor import my_nodepub

package_name = "ultrasonic_sensor"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="g.ferraro",
    maintainer_email="giuseppe.ferraro@isae-supaero.fr",
    description="This package streams the data produced by an ultrasonic device.",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "my_nodepub = ultrasonic_sensor.my_nodepub:main",
            "my_nodesub = ultrasonic_sensor.my_nodesub:main",
        ],
    },
)
