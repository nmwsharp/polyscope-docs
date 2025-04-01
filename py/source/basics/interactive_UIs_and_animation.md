Polyscope enables you to create custom interactive UIs with your own GUI elements such as buttons, sliders, and textboxes which execute user-defined code. 

Likewise, there is no explicit built-in functionality for time-varying data in Polyscope, but you can easily create custom UIs to display and update your content.

In either case, you can create interactive UI elements with the excellent [Dear ImGui](https://github.com/ocornut/imgui) library, see below for more.

![callback ui demo]([[url.prefix]]/media/callback_ui_demo.png)

## Basic Flow for Interactive UIs and Animation

The first step is to get your code executing every frame while the Polyscope window is open and running.

You can specify a callback function which Polyscope will invoke on each frame while the window is active.  This callback can be used to build a program-specific GUI, update an animation, perform computation, etc.  With this approach, you simplify set the desired callback function, and then call `polyscope.show()` as usual.

Your callback function should have no arguments and no return value. To use state inside your callback, access it directly from the outer scope where your function was defined.

**Example:**
```python
import polyscope as ps
import polyscope.imgui as psim
import numpy as np

ps.init()

# track state
my_val = 10

def my_other_function():
    print("hello")

def callback():
    # Executed every frame

    # Update content in the scene
    ps.register_point_cloud("this frame point", np.random.rand(100, 3))

    # access state from the outer scope
    global my_val # note: python has weird rules about 'global' vs 'nonlocal'

    # Build a UI element to edit a parameter, which will 
    # appear in the onscreen panel
    _, my_val = psim.InputInt("my val", my_val)

    if psim.Button("run subroutine"):
        my_other_function()

ps.set_user_callback(callback)
ps.show()
```


??? func "`#!python set_user_callback(func)`"

    Set a function which will be called by polyscope on every UI draw iteration. The argument should be a Python function, which takes no arguments.


??? func "`#!python clear_user_callback()`"

    Clear the callback function.


!!! Note "callback sets up ImGui internally"

    By default, when the user callback executes, Polyscope will internally set up an `ImGui` pane for you to create UI elements in. You can immediately make calls like `psim.Button()` in the callback without any additional ImGui bookkeeping.

    This behavior is configurable with an option below.

!!! Warning "Updating data from main loop with `frame_tick()`"

    ##### Custom main loops 

    As described in [program structure]([[url.prefix]]/basics/flow/#program-structure), it is alternately possible to run the Polyscope window not by calling `show()`, but by writing your own main loop, and calling `frame_tick()` on each iteration.

    If you choose this route, you can also modify scene content by simple issuing polyscope calls like `register_surface_mesh()` at any point in your main loop.

    **However, you cannot issue ImGui calls at any point in your main loop.** This limitation is because Polyscope needs to set up the ImGui context, which is not available as your main loop executes.

    Fortunately, you can still use the user callback to create ImGui UIs. You can specify your callback function as above, and it will be executed each frame, even when running Polyscope from your own main loop.


!!! Note "Nested calls to `show()`"

    ##### Nested show

    When creating custom UIs, you may find you want to call `show()` to open the interactive window, *within a frame which is already executing the main loop*.

    For example, you might create a button which calls a user-specified function. Within that function, if you hit a bug, you could register some extra data to understand the problem, call `show()` to investigate, then exit the window and continue running the outer program loop.

    **This is a supported workflow!** It should be possible to arbitrarily recurse into the show function, interacting with the scene even as an outer loop is executing.

    By default the user callback will not be executed within any of these nested calls to show, only the outermost one (configurable with an option below). Be careful not write an recursion of calling `show()`!

### Options


??? func "`#!python set_open_imgui_window_for_user_callback(b)`"

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../../features/callbacks_and_UIs) is invoked. This means you can immediately start making ui calls like `polyscope.imgui.Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `True`.

??? func "`#!python set_invoke_user_callback_for_nested_show(b)`"

    Suppose you call `polyscope.show()`, and within your callback, another instance of `polyscope.show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your user callback to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope.show()`.

    Default: `False`.

??? func "`#!python set_give_focus_on_show(b)`"

    If true, the Polyscope window will request focus from the window manager whenever `show()` is called. If false, the focus state will be left unchanged.

    Default: `False`.

## Updating Animated Data

Once you have code executing per-frame, you can issue Polyscope commands on each invocation to update the data.

The simplest approach is to just re-call structure-registration or quantity-adder functions with the updated data. Adding new structures/quantities with the same name will replace any existing ones, they will even [inherit any options which have been set]([[url.prefix]]/basics/parameters/#persistent-values). This should be fast enough for small-medium sized data at interactive rates.

Additionally, some structures have special more-efficient functions which update the structure in-place, if you are not changing the number of elements (e.g. [`SurfaceMesh.update_vertex_positions()`]([[url.prefix]]/structures/surface_mesh/basics/#updating-a-mesh)). Currently, if you are changing the number of elements (number of points in a point cloud, or number of vertices or connectivity of a mesh), you have no choice but to register a whole new structure.

**Example:** A typical basic setup for playing time-series data

```py
import polyscope as ps
import polyscope.imgui as psim
import numpy as np

# a list of your data for each frame
n_timestep = 50
n_pts = 1000
per_frame_points = np.random.rand(n_timestep, n_pts, 3) # random sample data

# UI state
curr_frame = 0
auto_playing = True

def myCallback(): # gets executed per-frame

  # Python scope resolution quirks
  # may need `nonlocal` rather than `global`` if your callback is 
  # defined inside another function
  global curr_frame, auto_playing

  update_frame_data = False
  _, auto_playing = psim.Checkbox("Autoplay", auto_playing)

  # Advance the frame
  if auto_playing:
    update_frame_data = True
    curr_frame = (curr_frame + 1) % n_timestep

  # Slider to manually scrub through frames  
  slider_updated, curr_frame = psim.SliderInt("Curr Frame", curr_frame, 0, n_timestep-1)
  update_frame_data = update_frame_data or slider_updated

  # Update the scene content if-needed
  if update_frame_data:
    ps.register_point_cloud("frame points", per_frame_points[curr_frame,:,:])

ps.init()

# set the scene scale manually so it doesn't jump around 
# as the data changes
ps.set_automatically_compute_scene_extents(False)
ps.set_length_scale(1)
ps.set_bounding_box((-1., -1., -1.), (1., 1., 1.))

ps.set_user_callback(myCallback) # specify the per-frame function

# give control to the main loop, blocks until window is exited
ps.show()
```

## Custom UIs with ImGui

Polyscope integrates with the [Dear ImGui](https://github.com/ocornut/imgui) library, a widely-used framework for creating prototype/demo UIs and widgets. It implements a huge variety of GUI elements including buttons, sliders, text boxes, color pickers, trees, tables, etc.

The Polyscope python package includes bindings to a significant subset of ImGui in the `polyscope.imgui` submodule. 

These bindings are not yet exhaustively documented, but they follow the naming conventions of ImGui as closely as possible for simplicity. Documentation of ImGui functions and parameters lives [here](https://github.com/ocornut/imgui/blob/master/imgui.h), and  you can find the list of bound functions, types, and enums [here](https://github.com/nmwsharp/polyscope-py/blob/master/src/cpp/imgui.cpp). Common usage should be covered by the example below.

**Example:** Create the following UI in a Python callback

![callback ui demo]([[url.prefix]]/media/imgui_py_demo.png)

```python
import polyscope as ps
import polyscope.imgui as psim

# A bunch of parameters which we will manipulate via the UI defined below.
# There is nothing special about these variables, you could manipulate any other 
# kind of Python values the same way, such as entries in a dict, or class members.
is_true1 = False
is_true2 = True
ui_int = 7
ui_float1 = -3.2
ui_float2 = 0.8
ui_color3 = (1., 0.5, 0.5)
ui_color4 = (0.3, 0.5, 0.5, 0.8)
ui_angle_rad = 0.2
ui_text = "some input text"
ui_options = ["option A", "option B", "option C"]
ui_options_selected = ui_options[1]

def my_function():
    # ... do something important here ...
    print("executing function")

# Define our callback function, which Polyscope will repeatedly execute while running the UI.
# We can write any code we want here, but in particular it is an opportunity to create ImGui 
# interface elements and define a custom UI.
def callback():

    # If we want to use local variables & assign to them in the UI code below, 
    # we need to mark them as nonlocal. This is because of how Python scoping 
    # rules work, not anything particular about Polyscope or ImGui.
    # Of course, you can also use any other kind of python variable as a controllable 
    # value in the UI, such as a value from a dictionary, or a class member. Just be 
    # sure to assign the result of the ImGui call to the value, as in the examples below.
    # 
    # If these variables are defined at the top level of a Python script file (i.e., not
    # inside any method), you will need to use the `global` keyword instead of `nonlocal`.
    nonlocal is_true1, is_true2, ui_int, ui_float1, ui_float2, ui_color3, ui_color4, ui_text, ui_options_selected, ui_angle_rad
    

    # == Settings
   
    # Use settings like this to change the UI appearance.
    # Note that it is a push/pop pair, with the matching pop() below.
    psim.PushItemWidth(150)


    # == Show text in the UI

    psim.TextUnformatted("Some sample text")
    psim.TextUnformatted("An important value: {}".format(42))
    psim.Separator()
    

    # == Buttons

    if(psim.Button("A button")):
        # This code is executed when the button is pressed
        print("Hello")

    # By default, each element goes on a new line. Use this 
    # to put the next element on the _same_ line.
    psim.SameLine() 
    
    if(psim.Button("Another button")):
        # This code is executed when the button is pressed
        my_function()
 

    # == Set parameters

    # These commands allow the user to adjust the value of variables.
    # It is important that we assign the return result to the variable to
    # update it. 
    # For most elements, the return is actually a tuple `(changed, newval)`, 
    # where `changed` indicates whether the setting was modified on this 
    # frame, and `newval` gives the new value of the variable (or the same 
    # old value if unchanged).
    #
    # For numeric inputs, ctrl-click on the box to type in a value.
   
    # Checkbox
    changed, is_true1 = psim.Checkbox("flag1", is_true1) 
    if(changed): # optionally, use this conditional to take action on the new value
        pass 
    psim.SameLine() 
    changed, is_true2 = psim.Checkbox("flag2", is_true2) 
    
    # Input ints
    changed, ui_int = psim.InputInt("ui_int", ui_int, step=1, step_fast=10) 

    # Input floats using two different styles of widget
    changed, ui_float1 = psim.InputFloat("ui_float1", ui_float1) 
    psim.SameLine() 
    changed, ui_float2 = psim.SliderFloat("ui_float2", ui_float2, v_min=-5, v_max=5)

    # Input colors
    changed, ui_color3 = psim.ColorEdit3("ui_color3", ui_color3)
    psim.SameLine() 
    changed, ui_color4 = psim.ColorEdit4("ui_color4", ui_color4)

    # Input text
    changed, ui_text = psim.InputText("enter text", ui_text)

    # Combo box to choose from options
    # There, the options are a list of strings in `ui_options`,
    # and the currently selected element is stored in `ui_options_selected`.
    psim.PushItemWidth(200)
    changed = psim.BeginCombo("Pick one", ui_options_selected)
    if changed:
        for val in ui_options:
            _, selected = psim.Selectable(val, ui_options_selected==val)
            if selected:
                ui_options_selected = val
        psim.EndCombo()
    psim.PopItemWidth()
    

    # Use tree headers to logically group options

    # This a stateful option to set the tree node below to be open initially.
    # The second argument is a flag, which works like a bitmask.
    # Many ImGui elements accept flags to modify their behavior.
    psim.SetNextItemOpen(True, psim.ImGuiCond_FirstUseEver)
   
    # The body is executed only when the sub-menu is open. Note the push/pop pair!
    if(psim.TreeNode("Collapsible sub-menu")):
        
        psim.TextUnformatted("Detailed information")
        
        if(psim.Button("sub-button")):
            print("hello")

        # There are many different UI elements offered by ImGui, many of which
        # are bound in python by Polyscope. See ImGui's documentation in `imgui.h`,
        # or the polyscope bindings in `polyscope/src/cpp/imgui.cpp`.
        changed, ui_angle_rad = psim.SliderAngle("ui_float2", ui_angle_rad, 
                v_degrees_min=-90, v_degrees_max=90)
        
        psim.TreePop()

    psim.PopItemWidth()


ps.init() 
ps.set_user_callback(callback)
ps.show()
```

## Mouse Interactions

You can implement custom mouse behaviors on clicks and other actions within your per-frame callback function. ImGui exposes the state of the mouse and whether a click occurred via `psim.GetIO()`.


??? Note "Temporarily disable default mouse camera movement"

    If you implement your own interactions like clicking-and-dragging objects onscreen, you'll find that the Polyscope view camera unintentionally moves in response to these motions. You can temporarily disable the camera motion like:

    ```python
    if doing_interaction and psim.IsMouseClicked(1): 
        ps.set_do_default_mouse_interaction(False)
        # ... do your interaction

    if not doing_interaction:
        # re-enable the default mouse motions after you're done
        ps.set_do_default_mouse_interaction(True)
    ```

??? func "`#!python screen_coords_to_world_ray(screen_coords)`"

    Convert a click location to a ray in world-space.

??? func "`#!python screen_coords_to_world_position(screen_coords)`"

    Convert a click location to a location in world-space, by reading from the scene's depth buffer.

??? func "`#!python set_do_default_mouse_interaction(b)`"

    Use this function to (temporarily) disable Polyscope's default mouse clicking/panning/zooming response to mouse movements, so that they will not conflict with your own implemented operations

    If `True`, Polyscope will perform its usual responses to mouse operations, `False` will disable.


### Picking, Selection, and Querying the Scene

"Picking" refers to querying the content under the cursor in the rendered image.  Polyscope implements render buffer-based picking, to efficiently get the object and element under the cursor even on large complex scenes.

??? func "`#!python pick(screen_coords=None, buffer_inds=None)`"

    Evaluate a "pick" query to get the contents of the rendered view at a specified location.  One of `screen_coords` or `buffer_inds` should be passed as the input location, but not both.  The return is a `PickResult` class, see below. 

    Screen coordinates and buffer indices both refer to a location in the rendered 2d image. Screen coordinates are real-valued, whereas buffer indices are integer. On some platforms they may be identical, but on others with high-DPI screens, they may differ. In the common-case of getting mouse positions from ImGui, you want screen coords.


**Example:** picking a faces from a mesh
```python
# inside the user-callback, or other code which runs each frame
myMesh = # ...  your added mesh ... */

# make only faces clickable in the mesh
myMesh.set_selection_mode('faces_only')

# get the mouse location from ImGui
io = psim.GetIO()
if io.MouseClicked[0]: # if clicked
  screen_coords = io.MousePos
  pick_result = polyscope.pick(screen_coords=screen_coords)

  # check out pick_result.is_hit, pick_result.structureName, pick_result.depth, etc

  # get additional information if we clicked on a mesh
  if(pick_result.isHit and pick_result.structure_name == "myMesh"):
    print(pick_result.structure_data) # additional dictionary of element type, coords, etc.
  

```

A pick query returns a combined struct with info such as what structure was clicked on, and depth of the point in the scene.

```python
class PickResult:
    self.is_hit =               # did we hit anything?
    self.structure_type_name =  # structure type which was hit, like "Point Cloud"
    self.structure_name =       # name of structure which was hit, like "my_points"
    self.screen_coords =        # coordinates of the query location
    self.buffer_inds =          # render buffer indices of the query location
    self.position =             # 3d position which was hit, in world space
    self.depth =                # depth to the hit, in world units
    self.local_index =          # structure-specific index of the element which was hit
    self.structure_data =       # a dictionary of additional fields for the clicked structure
```

Additionally, many structures will report additional information about the pick, in the `structure_data` field. For instance, a `SurfaceMesh` gives info on whether a vertex/face/edge/etc was clicked on, the index of that element, and barycentric coordinates of the click within a face.

Polyscope also maintains a stateful selection, displayed in the UI to provide information about the content of the scene. It can be accessed via `get_selection()`, `reset_selection()`, `have_selection()`.


## Overriding Built-In UI Behavior

If desired, you can circumvent Polyscope's standard ImGui style and UI panes, in ordered to build dramatically customized applications.


The option `build_gui` can be used to entirely disable all of Polyscope's ImGui UI elements, allowing you to build your own UI. Polyscope will still initialize ImGui and invoke its drawing routines each frame.

??? func "`#!python set_build_gui(b)`"
    
    This option can be used to disable all of Polyscope's ImGui UI elements, which may be useful for advanced applications which wish to build a fully-custom UI on top of Polyscope.

    If false, Polyscope will not create any ImGui UIs at all, but will still set up ImGui and invoke its render steps each frame. The allows advanced users to create their own UIs totally from scratch and circumvent the standard Polyscope UIs.

    Default: `True`.

The functions `build_polyscope_gui()`, `build_structure_gui()`, `build_pick_gui()`, and `build_user_gui_and_invoke_callback()`
 can be used to manually build pieces of the UI one at a time. If you are giving control to the UI via `show()`, you call the first 3 to reproduce the standard UI.