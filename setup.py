from setuptools import find_packages, setup

setup(
    name="mcqgener",
    version="0.0.1",
    author="Amir Bannani",
    author_email="amirbennenni@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "pyPDF", "google-generativeai"],
    packages=find_packages()
)