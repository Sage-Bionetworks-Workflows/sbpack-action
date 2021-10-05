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
    - name: sbpack push
      uses: include-dcc/sbpack-action@v0.0.1
      with:
        app_name: thomasyu888/test/testing
        workflow_path: example/hello_world_workflow.cwl
        auth_token: ${{secrets.SBG_AUTH_TOKEN }}
        api_endpoint: https://cavatica-api.sbgenomics.com/v2
```
