## About

Using [sbpack](https://github.com/rabix/sbpack) to update seven bridges workflow applications.

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
