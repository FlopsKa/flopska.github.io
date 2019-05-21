Title: A Hint of Eclipse in Visual Code
Date: 2019-05-21
Category: computer science

Professionally I am a heavy eclipse user. I heard that IntelliJ is better by now
but I have yet to make the switch. However, the focus of eclipse clearly is Java
programming. For my own projects I tend to use python - and while vim is awesome
I prefer the support of Microsoft's Visual Code.

# Eclipse shortcuts in Visual Code

The Eclipse IDE has its own (huge) set of shortcuts: to move around code, to
search, to refactor, to run tests, to run a gradle task, ... . The list is
endless. Some time ago we literally printed the standard shortcuts on two sheets
of paper and marked the ones we knew - so that we could focus on memorizing the
rest.

Compared to all the support eclipse provides when refactoring java, the support
of Visual Code seems minimal. Checking the section 'Refactoring' in the
[documentation](https://code.visualstudio.com/docs/python/editing), we can:

- Extract Variable
- Extract Method
- Sort Imports

Don't ask me why there is no __Inline__ - but at least there is something.

The refactoring actions can be called from the command palette (`Ctrl+Shift+P`).
Additionally one can provide one's own keyboard shortcuts. Because I don't want to
memorize some (arbitrary) new set of commands I stick with the ones I know from
eclipse.

So, in order to define the settings: Open the command palette, search for
`Shortcuts` and open the JSON-Config.

```json
[
    {
        "key": "shift+alt+l",
        "command": "python.refactorExtractVariable"
    },
    {
        "key": "shift+alt+m",
        "command": "python.refactorExtractMethod"
    },
    {
        "key": "ctrl+shift+o",
        "command": "python.sortImports"
    }
]
```

Copy and paste the lines above, eh voilá. Now commit these to memory and get
used to refactoring in python :)