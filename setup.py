from setuptools import find_packages , setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Anjana C S",
    author_email="anjanacs901@gmail.com",
    packages=find_packages(), # find constructor files , insatll the src folder as local package
    install_requires=[] # instal all from requirements.txt
)

# 