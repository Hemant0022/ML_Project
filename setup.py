from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "ML Project",
    version = "0.1.0",
    packages = find_packages(),
    author = "Hemant Raj",
    author_email = "hemantraja85@outlook.com",
    install_requires = get_requirements('requirements.txt')
)
