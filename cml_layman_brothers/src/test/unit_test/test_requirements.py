#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

def test_requirements():
    import pkg_resources
    from pkg_resources import DistributionNotFound, VersionConflict
    
    dependencies = [
        'setuptools==41.0.1',
        'sklearn==0.0',
        'matplotlib==3.2.2',
        'pandas==1.0.5',
        'numpy==1.19.0',
    ]
    
    pkg_resources.require(dependencies)
