#!/usr/bin/env bash

pytest tests/ --cov-report term --cov-report html --cov-config .coveragerc --cov=.