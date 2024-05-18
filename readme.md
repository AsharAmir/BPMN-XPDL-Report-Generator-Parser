# XPDL Parser and Report Generator

This repository contains a Python script for parsing XPDL (XML Process Definition Language) files and generating a comprehensive report on various BPMN (Business Process Model and Notation) elements.

## Features

- Parse XPDL files and count different BPMN elements.
- Generate a detailed report summarizing the counts of each element type.

## Requirements

- Python 3.x
- `xml.etree.ElementTree`
- `collections.Counter`

## Output
The script outputs a detailed report of BPMN elements, including:

- Pools
- Lanes
- Events (Total, Start, Intermediate, End)
- Tasks (Total, User, Service, Script, Manual, Sub-processes)
- Gateways (Total, Exclusive, Parallel, Inclusive)
- Artifacts (Total, Data Objects, Groups, Annotations)
- Connecting Objects (Sequence Flows, Message Flows, Associations)
