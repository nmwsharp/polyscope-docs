## Using messages

We've all been there: a crucial error message gets printed to the terminal, but lost in a tempest of text---noticing that error message could have saved two hours of debugging.  Polyscope contains a simple system for showing message dialogs in the UI which are sure to be noticed but stay out of the way.

There are a few levels of messages available:

- **error** A very bad error; immediately shows and blocks the UI for user response.
- **warning** A medium priorty warning, shown the next time UI main loop executes. Warnings of the same type can be batched together, so these messages can be issued in a dense loop without drowning the program.
- **info** A low-priority message, which is just printed to `stdout`.

Messages can be dismissed by clicking the button in dialog box, or pressing `[space]`.

![messages demo](/media/messages_demo.png)

Example:
```python
import polyscope as ps
ps.init()

# Generate a single warning.
# Has no effect on the GUI until polyscope gets control flow
# back, which happens here in the show() call below.
ps.warning("Something went slightly wrong")

# Generate a lot of warnings. Becase all of these warnings 
# have the same base message (the first string), they will 
# be batched together and only shown as one dialog. The detail 
# message for the first such warning will also be shown.
for i in range(5000):
  ps.warning("Some problems come in groups", "some details: " + str(i))

# The previous warnings would be displayed here
ps.show()

# Generating an error.
# The UI will block and show this error immediately. After 
# the error is dismissed, the call will return.
ps.error("Resistance is futile.");
```


### Messages

??? func "`#!python info(message)`"
    
    ##### info

    Simply logs a message to `stdout`.


??? func "`#!python warning(message, detail="")`"
    
    ##### warning

    Create a warning message, to be displayed the next time the UI gets flow control. 

    When issuing a one-off warning, the `detail` field need not be used.  However, if issuing warnings in a loop, warnings with the same base `message` are batched together, so the UI doesn't get completely overwhelmed (see example above).


??? func "`#!python error(message)`"

    ##### error
  
    Generate an error, which is immediately shown in the GUI. After the error dialog is dismissed in the GUI, this function returns.
