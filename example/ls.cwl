#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ls
stdout: output.txt
inputs:
  dir:
    type: Directory
    inputBinding:
      position: 1
outputs:
  example_out:
    type: stdout
