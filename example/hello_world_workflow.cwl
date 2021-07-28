cwlVersion: v1.0
class: Workflow

inputs:
  dir: Directory

outputs:
  cat_out:
    type: File
    outputSource: cat/example_out

steps:
  ls:
    run: ls.cwl
    in:
      dir: dir
    out:
      [example_out]

  cat:
    run: cat.cwl
    in:
      file: ls/example_out
    out:
      [example_out]
