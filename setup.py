from distutils.core import setup

setup(
    name = 'Stocpy',
    version = '0.1.0',
    description = 'A Python package to retrieve stock data as well as Stock Symbols for the Indian Stock Market.',
    author = 'Aadhar',
    author_email = 'sachdevaaadhar@gmail.com',
    url = 'https://github.com/Aadhar96/Stockpy', 
    keywords= "market finance ticker stock stocks NSE BSE ".split()
    py_modules=['Stockpy'],
    install_requires=[
        # list of this package dependencies
        "requests >= 2.2.1",
        "pandas >= 0.16.1",
    ],
)
