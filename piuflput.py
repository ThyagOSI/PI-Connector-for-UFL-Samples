# -*- coding: utf-8 -*-
""" piuflput.py

   Copyright 2015 OSIsoft, LLC.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

This python example sends file contents to the PI Connector for UFL REST endpoint

The syntax is: python piufl.py REST-URL file

Parameters:
    rest-ufl - The Address specified in the Data Source configuration of the Connector
    file - Data file to be processed by the Connector

Example:
    python piuflput.py https://<server>:5460/connectordata/value value.csv

	"""
import argparse
import requests
import sys

requests.packages.urllib3.disable_warnings()

# Process arguments

parser = argparse.ArgumentParser(description='POST file contents to PI Connector for UFL')
parser.add_argument('resturl',
                        help='REST endpoint address')
parser.add_argument('file',
                   help='Data file to be POST-ed')

args = parser.parse_args()

s = requests.session()
s.auth = ('', '')
# Read the file contents
with open(args.file,"r") as f:
    data = ''.join(f.readlines())
    request = s.put(args.resturl, data=data, verify=False)
    print(request.text)
    print(request.status_code)
