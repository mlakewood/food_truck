#!/bin/sh

SRC_DIR=/home/ubuntu/food_truck
BUILD_DIR=/home/ubuntu/food_truck-build

rm -Rf $BUILD_DIR

mkdir -p $BUILD_DIR
virtualenv $BUILD_DIR/virt
cd $SRC_DIR
$BUILD_DIR/virt/bin/python setup.py install

fpm -s dir -t deb -n food-truck -v 0.1 -d "python,python-dev,postgresql" /home/ubuntu/food_truck-build/=/home/ubuntu/foodtruck.com
