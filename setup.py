import os

from setuptools import setup, find_packages

setup(
        name='food_truck',
        version='0.1.0',
        description='Show me the food trucks in San Francisco.',
        long_description=('demonstration of how to package a web-app'),
        url='http://github.com/mlakewood/food_truck',
        license='MIT',
        author='Mark Lakewood',
        author_email='underplank@gmail.cpom',
        packages=find_packages(exclude=['tests*']),
        install_requires=["Flask==0.10.1",
                          "Flask-SQLAlchemy==1.0",
                          "Jinja2==2.7.1",
                          "MarkupSafe==0.18",
                          "gunicorn==18.0",
                          "gevent==1.0",
                          "requests==1.2.3",
                          ],
        include_package_data=True,
        entry_points = {
                'console_scripts': [
                    'create_db = food_trucks.scripts.create_db:main',
                    'load_data = food_trucks.scripts.load_data:main',
                    'dev_server = food_trucks.scripts.run_server:dev_server',
                    'run_server = food_trucks.scripts.run_server:run_server'
                    ]
            },
        package_data={'static': 'food_trucks/static/*',
                      'templates': 'food_trucks/templates/*'},
        classifiers=[
                    "Private :: Do Not Upload"
                    ],
)
