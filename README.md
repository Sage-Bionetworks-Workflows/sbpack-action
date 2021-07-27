## About

Github Action to upload files to [CAVATICA](https://cavatica.sbgenomics.com/).

## Usage
To update application in seven bridges platforms, authentication tokens and there must be prexisting projects and applications.

```
name: ci

on:
  push:
    branches: master

jobs:
  update_application:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: upload file

```
