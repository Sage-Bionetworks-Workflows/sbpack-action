#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: cat
stdout: output.txt
inputs:
  file:
    type: File
    inputBinding:
      position: 1
outputs:
  example_out:
    type: stdout