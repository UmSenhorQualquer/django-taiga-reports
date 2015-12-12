import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-taiga-reports',
	version='0.0',
	packages=['django_taiga_reports'],
	include_package_data=True,
	zip_safe=False,
	license='BSD License',
	description='Django visualization for taiga-reports.',
	long_description=README,
	url='https://github.com/UmSenhorQualquer/django-taiga-reports',
	author='Ricardo Ribeiro',
	author_email='ricardojvr@gmail.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
	package_data={'django_taiga_reports': [
		'templates/*.html',
		'static/js/*',
		'static/css/*',
		'static/fonts/*',
		]
	},
)