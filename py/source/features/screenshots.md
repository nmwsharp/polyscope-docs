## Taking screenshots

Polyscope includes simple functionality for saving screenshots of the UI to disk. The imGUI windows will be automatically hidden when taking a screenshot.

Screenshots can be taken manually by pressing the `[screenshot]` button in the options UI window, or programmatically using the functions below. Clicking the UI button is equivalent to calling `screenshot()` below, generating a numbered screenshot file in the current directory.


???+ func "`#!python screenshot(filename=None, transparentBG=True)`"

    Saves a screenshot to the path given as `filename`, with format inferred from the file extension. 

    The extension should be one of `.png`, `.tga`, or `.bmp`.
    
    If no name is is given, screenshots are saved to the current directory, with file named like `screenshot_000000.tga` numbered automatically in increasing order. The numbering is reset to `0` for each run of the program; existing files will be silently overwritten.

    If `transparentBG` is `true`, the background will be rendered as transparent.
