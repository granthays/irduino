from distutils.core import setup

setup(
    name='irduino',
    version='0.0.1',
    author='Grant Hays',
    author_email='granthays@gmail.com',
    packages=['irduino'],
    scripts=['bin/IRduino-XBMC.py'],
    url='http://pypi.python.org/pypi/irduinio/',
    license='LICENSE.txt',
    description='An XBMC IR Remote Control protocol using Arduino',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyserial",
    ],
)
