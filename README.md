# Maya Python Completions for Visual Studio Code

These are some stubs files that assist vscode via jedi in autocompleting commands used in the Maya Python codebase.

## How to use

* Clone this repo to a local folder on disk. (eg `/home/savio/vscode/maya-completion`)

* In your vscode `settings.json` add this local path as a autoComplete extraPath 

  ```
  "python.autoComplete.extraPaths": ["/home/savio/vscode/maya-completion"]
  ```

## Requirements

* [Visual Studio Code](https://code.visualstudio.com/)
* [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
