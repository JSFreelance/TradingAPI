#!/bin/bash

virtualenv project_venv
source project_venv/bin/activate
pip install -r requirements.txt
deactivate
