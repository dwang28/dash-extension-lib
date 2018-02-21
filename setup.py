from setuptools import setup

exec (open('im_dash_extension_pack/version.py').read())

setup(
    name='im_dash_extension_pack',
    version=__version__,
    author='dwang28',
    packages=['im_dash_extension_pack'],
    include_package_data=True,
    license='MIT',
    description='Extend basic dash html library for better support of bootstrap and other html elements',
    install_requires=[]
)
