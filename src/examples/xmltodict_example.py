# CCSDS-NDM: CCSDS Navigation Data Messages Read/Write Library
#
# Copyright (C) 2020 CCSDS-NDM Project Team
#
# Licensed under GNU GPL v3.0. See LICENSE.rst for more info.
"""
xmltodict example.

"""
import os
from builtins import print
from pathlib import Path
from pprint import pprint

import xmltodict

if __name__ == '__main__':
    # print working directory
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    print(f"current working directory is {ROOT_DIR}.")

    # check file location
    xml_file_path = Path(ROOT_DIR, "..", "sample_xml",
                         "cdm_example_section4.xml")

    print(f"xml file path : {xml_file_path.resolve()}")
    print(f"file exists   : {xml_file_path.exists()}")

    # read XML file
    pprint(xmltodict.parse(xml_file_path.read_text()))
