from setuptools import setup

version = '1.0.0'

setup(
    name = 'RPnickAPI',
    version=version,
    
    author='N1C1',
    author_email='rydsa708998@gmail.com',
    description='Генератор РП ников SAMP',
    
    long_description='Генератор РП ников для проектов SAMP, сайт который генерирует: "http://rp-nicks.aa-roleplay.ru/"',
    
    url='https://github.com/N1C1N1/RPnickAPI',
    download_url='https://github.com/N1C1N1/RPnickAPI/archive/v{}.zip'.format(version),
    packages=['RPnickAPI'],
    requires=['bs4', 'requests']
)