# setup.py - Package setup for CDP1806E-R32 Emulator

from setuptools import setup, find_packages

setup(
    name="cdp1806e32",
    version="0.1",
    description="Emulator and toolchain for the CDP1806E-R32 RISC CPU",
    author="Your Name",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cdp1806e32-emulator = cdp1806e32_emulator:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)