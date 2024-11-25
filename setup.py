from setuptools import find_packages, setup
# Used to make any folder as internal package, so that we can import anything from there
#On running this file, .egg-info file will be created
setup(
    name = 'Generative AI Project - Medical Chatbot',
    version= '0.0.0',
    author= 'Akash Prabhakar',
    author_email= 'akashprabhakar427@gmail.com',
    #find_packages() will try to find the __init__.py file and where it will find that, 
    # will consider that folder as local package. Here >> src folder
    packages= find_packages(),
    install_requires = []


)