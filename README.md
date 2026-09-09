# File Organiser

A desktop application for organising and cleaning up messy directories.

File Organiser scans a selected folder, analyses its contents, identifies potential duplicates and other issues, and suggests a safe set of changes before anything is moved or modified.

The goal is to make file organisation **automatic without being dangerous**.

## Example Usage

Given a messy `Downloads` folder:

```text
Downloads/
├── IMG_1234.jpg
├── assignment-final.pdf
├── assignment-final-2.pdf
├── setup.exe
├── project.zip
├── holiday.png
└── lecture-notes.pdf
```

The application might suggest:

```text
Downloads/
├── Images/
│   ├── IMG_1234.jpg
│   └── holiday.png
├── Documents/
│   ├── assignment-final.pdf
│   └── lecture-notes.pdf
├── Applications/
│   └── setup.exe
├── Archives/
│   └── project.zip
└── Potential Duplicates/
    └── assignment-final-2.pdf
```

Before making any changes, the user can review the proposed operations and choose whether to apply them.

### Requirements

* Python 3.14+
* Windows, macOS, or Linux

## Project Goals

Particular areas of interest include:

* Filesystem programming
* Classification and rule-based systems
* Potential for ML algorithm integration to better sort files
* Software testing (TDD)
* Object-Orientated Principles
* Error handling and recovery
* Performance considerations when processing large numbers of files
