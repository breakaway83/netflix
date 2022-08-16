from setuptools import setup, find_packages

setup(
    name="exploit_automation",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click"
    ],
    python_requires=">=3.10.5",
    entry_points={
        'console_scripts': [
            'exploit_automation = exploit_automation:cli',
        ],
    },
)
