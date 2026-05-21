Polyscope enables you to create custom interactive UIs with your own GUI elements such as buttons, sliders, and textboxes which execute user-defined code. 

Likewise, there is no explicit built-in functionality for time-varying data in Polyscope, but you can easily create custom UIs to display and update your content.

In either case, you can create interactive UI elements with the excellent [Dear ImGui](https://github.com/ocornut/imgui) library, see below for more.

![callback ui demo]([[url.prefix]]/media/callback_ui_demo.png)


## Basic Flow for Interactive UIs and Animation

The first step is to get your code executing every frame while the Polyscope window is open and running.

You can specify a callback function which Polyscope will invoke on each frame while the window is active.  This callback can be used to build a program-specific GUI, update an animation, perform computation, etc.  With this approach, you simplify set the desired callback function, and then call `polyscope::show()` as usual.

Your callback function should have no arguments and no return value. To use state inside your callback, either access it statically, or capture-bind the state like a lambda.

**Example:** Minimal callback setup
```cpp
#include "polyscope/polyscope.h"

// Track state statically outside of your callback (or bind like a lambda)
int myVal = 10;

void myCallback() { // gets executed per-frame

  // Update content in the scene
  polyscope::registerPointCloud("this frame point", my_points);

  // Build a UI element to edit a parameter, which will 
  // appear in the onscreen panel
  ImGui::InputInt("my val", &myVal); 

  if (ImGui::Button("run subroutine")) {
    callSomeOtherFunction();
  }
}

int main(int argc, char** argv) {
  polyscope::init();
  polyscope::state::userCallback = myCallback; // specify the callback
  polyscope::show();
  return EXIT_SUCCESS;
}
```

??? func "`#!cpp std::function<void()> polyscope::state::userCallback`"

    A function which will be invoked on every main loop iteration by Polyscope, once `show()` has been called.

    If null, nothing will be invoked, set the callback to `nullptr` to clear it.


!!! Note "callback sets up ImGui internally"

    By default, when the user callback executes, Polyscope will internally set up an `ImGui` pane for you to create UI elements in. You can immediately make calls like `ImGui::Button()` in the callback without any additional ImGui bookkeeping.

    This behavior is configurable with an option below.


!!! Warning "Updating data from main loop with `frameTick()`"

    ##### Custom main loops 

    As described in [program structure]([[url.prefix]]/basics/flow/#program-structure), it is alternately possible to run the Polyscope window not by calling `show()`, but by writing your own main loop, and calling `frameTick()` on each iteration.

    If you choose this route, you can also modify scene content by simple issuing polyscope calls like `registerSurfaceMesh()` at any point in your main loop.

    **However, you cannot issue ImGui calls at any point in your main loop.** This limitation is because Polyscope needs to set up the ImGui context, which is not available as your main loop executes.

    Fortunately, you can still use the user callback to create ImGui UIs. You can specify your callback function as above, and it will be executed each frame, even when running Polyscope from your own main loop.

!!! Note "Nested calls to `show()`"

    ##### Nested show

    When creating custom UIs, you may find you want to call `show()` to open the interactive window, *within a frame which is already executing the main loop*.

    For example, you might create a button which calls a user-specified function. Within that function, if you hit a bug, you could register some extra data to understand the problem, call `show()` to investigate, then exit the window and continue running the outer program loop.

    **This is a supported workflow!** It should be possible to arbitrarily recurse into the show function, interacting with the scene even as an outer loop is executing.

    By default the user callback will not be executed within any of these nested calls to show, only the outermost one (configurable with an option below). Be careful not write an recursion of calling `show()`!

### Options

??? func "`#!cpp bool options::openImGuiWindowForUserCallback`"

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../callbacks_and_UIs) is invoked. This means you can immediately start making ui calls like `ImGui::Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `true`.


??? func "`#!cpp bool options::invokeUserCallbackForNestedShow`"

    Suppose you call `polyscope::show()`, and within your callback, another instance of `polyscope::show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your `userCallback` to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope::show()`.

    Default: `false`.


??? func "`#!cpp bool options::giveFocusOnShow`"

    If true, the Polyscope window will request focus from the window manager whenever `show()` is called. If false, the focus state will be left unchanged.

    Default: `false`.

## Updating Animated Data

Once you have code executing per-frame, you can issue Polyscope commands on each invocation to update the data.

The simplest approach is to just re-call structure-registration or quantity-adder functions with the updated data. Adding new structures/quantities with the same name will replace any existing ones, they will even [inherit any options which have been set]([[url.prefix]]/basics/parameters/#persistent-values). This should be fast enough for small-medium sized data at interactive rates.

Additionally, some structures have special more-efficient functions which update the structure in-place, if you are not changing the number of elements (e.g. [`SurfaceMesh::updateVertexPositions()`]([[url.prefix]]/structures/surface_mesh/basics/#updating-a-mesh)). Currently, if you are changing the number of elements (number of points in a point cloud, or number of vertices or connectivity of a mesh), you have no choice but to register a whole new structure.

**Example:** A typical basic setup for playing time-series data

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/point_cloud.h"

// a list of your data for each frame
std::vector<std::vector<glm::vec3>> perFramePoints; 

// UI state
int currFrame = 0;
bool autoPlaying = true;

void myCallback() { // gets executed per-frame
  bool updateFrameData = false;

  ImGui::Checkbox("Autoplay", &autoPlaying);

  // Advance the frame
  if(autoPlaying) {
    updateFrameData = true;
    currFrame = (currFrame + 1) % perFramePoints.size();
  }

  // Slider to manually scrub through frames  
  bool sliderUpdated = ImGui::SliderInt("Curr Frame", &currFrame, 0, perFramePoints.size()-1);
  updateFrameData = updateFrameData || sliderUpdated;

  // Update the scene content if-needed
  if(updateFrameData) {
    polyscope::registerPointCloud("frame points", perFramePoints[currFrame]);
  }
}

int main(int argc, char** argv) {

  // Create sample point cloud data
  int nFrames = 100;
  for (int t = 0; t < nFrames; t++) {
    std::vector<glm::vec3> points;
    for (size_t i = 0; i < 3000; i++) {
      points.push_back( glm::vec3{polyscope::randomUnit() - .5, polyscope::randomUnit() - .5, polyscope::randomUnit() - .5});
    }
    perFramePoints.push_back(points);
  }

  polyscope::init();

  // set the scene scale manually so it doesn't jump around 
  // as the data changes
  polyscope::options::automaticallyComputeSceneExtents = false;
  polyscope::state::lengthScale = 1.;
  polyscope::state::boundingBox = 
      std::tuple<glm::vec3, glm::vec3>{ {-1., -1., -1.}, {1., 1., 1.} };

  polyscope::state::userCallback = myCallback; // specify the callback
  polyscope::show();
  return EXIT_SUCCESS;
}
```


## Transformation Gizmos

Transformation gizmos allow users adjust the rotation/translation/scale of objects in the scene. You can create your own gizmos to manipulate any transformations or positions within interactive UIs.

Each gizmo wraps a `4x4` homogenous transformation matrix and updates it in response to edits. Every structure has a built-in widget to adjust its transformation, which can be enabled from the [structure options]([[url.prefix]]/structures/structure_management/#transforms), in addition to any custom gizmos you might create. The onscreen gizmos are drawn using ImGui, with help from the excellent [ImGuizmo](https://github.com/CedricGuillemet/ImGuizmo) library.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/transform_gizmo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

```cpp
#include "polyscope/polyscope.h"

// create a new gizmo in the scene
polyscope::TransformationGizmo* gizmo1 = polyscope::addTransformationGizmo("my_gizmo");
// if no name is given, a name is automatically generated
polyscope::TransformationGizmo* gizmo2 = polyscope::addTransformationGizmo();

// configure which motions are allowed
gizmo1->setAllowTranslation(true);
gizmo1->setAllowRotation(false);
gizmo1->setAllowScaling(true);
gizmo1->setInteractInLocalSpace(false);

// adjust the appearance
gizmo1->setGizmoSize(0.5f);

// read off the current transform described by the gizmo
glm::mat4 currentT = gizmo1->getTransform();
glm::vec3 translation = gizmo1->getPosition(); // if you only care about the center/translation
// see also setTransform(), setPosition()

// remove gizmos
gizmo2->remove();
polyscope::removeTransformationGizmo("my_gizmo");
```

??? func "`#!cpp polyscope::addTransformationGizmo(std::string name = "", glm::mat4* transformToWrap = nullptr)`"

    Create and add a new transformation gizmo to the scene. If no name is given, a unique name will be automatically generated.

    If `transformToWrap` is provided, the gizmo will manipulate that matrix directly; otherwise, it will create and manage its own internal matrix.

    Returns a (non-owning) pointer to the newly created gizmo.


??? func "`#!cpp TransformationGizmo* getTransformationGizmo(std::string name)`"

    Get a user-created transformation gizmo by name.


??? func "`#!cpp void removeTransformationGizmo(TransformationGizmo* gizmo)`"

    Remove a user-created transformation gizmo by pointer.


??? func "`#!cpp void removeTransformationGizmo(std::string name)`"

    Remove a user-created transformation gizmo by name.


??? func "`#!cpp void removeAllTransformationGizmos()`"

    Remove all user-created transformation gizmos from the scene.


??? note "Other transform gizmo member functions"

    Management:
    ```cpp
      void TransformationGizmo::remove() 
    ```

    Get/set the transform:
    ```cpp
      glm::mat4 TransformationGizmo::getTransform()
      void TransformationGizmo::setTransform(glm::mat4 newT)
    ```

    Get/set the position (translation component of transform):
    ```cpp
      glm::vec3 TransformationGizmo::getPosition()
      void TransformationGizmo::setPosition(glm::vec3 newPos)
    ```

    Configure whether interaction allows rotation/translation/scaling:
    ```cpp
      bool TransformationGizmo::getAllowTranslation();
      void TransformationGizmo::setAllowTranslation(bool newVal);
      bool TransformationGizmo::getAllowRotation();
      void TransformationGizmo::setAllowRotation(bool newVal);
      bool TransformationGizmo::getAllowScaling();
      void TransformationGizmo::setAllowScaling(bool newVal);
    ```

    If true, interactions are interpreted in the local space of the gizmo; if false, in world space:
    ```cpp
      bool TransformationGizmo::getInteractInLocalSpace();
      void TransformationGizmo::setInteractInLocalSpace(bool newVal);
    ```

    Adjust the visual size of the gizmo, 1.0 is the default:
    ```cpp
      float TransformationGizmo::getGizmoSize();
      void TransformationGizmo::setGizmoSize(float newVal);
    ```

    Construct an ImGui UI to set values and toggle options. Must be called inside an active ImGui window:
    ```cpp
      void TransformationGizmo::buildInlineTransformUI();
    ```

## Custom UIs with ImGui

Polyscope integrates with the [Dear ImGui](https://github.com/ocornut/imgui) library, a widely-used framework for creating prototype/demo UIs and widgets. It implements a huge variety of GUI elements including buttons, sliders, text boxes, color pickers, trees, tables, etc.

We will not reproduce the ImGui documentation here, visit the ImGui github page for more information on how to use it, mainly in the source files `imgui.h` and `imgui_demo.cpp`. Or search for examples across the web!

![callback ui demo]([[url.prefix]]/media/imgui_py_demo.png)


### 2D Plots with ImPlot

Polyscope also provides [ImPlot](https://github.com/epezent/implot) for creating little inline 2D plots like line plots, scatter plots, and histograms in the UI panes. As with ImGui, please see ImPlot's pages for documentation.

## Mouse Interactions

You can implement custom mouse behaviors on clicks and other actions within your per-frame callback function. `ImGui` exposes the state of the mouse and whether a click occurred via `ImGui::GetIO()`.

??? Note "Temporarily disable default mouse camera movement"

    If you implement your own interactions like clicking-and-dragging objects onscreen, you'll find that the Polyscope view camera unintentionally moves in response to these motions. You can temporarily disable the camera motion like:

    ```cpp
    if(doing_interaction && ImGui::IsMouseClicked(1)) {
        polyscope::options::doDefaultMouseInteraction = false;
        // ... do your interaction
    }

    if(!doing_interaction) {
        // re-enable the default mouse motions after you're done
        polyscope::options::doDefaultMouseInteraction = true;
    }
    ```

??? func "`#!cpp glm::vec3 view::screenCoordsToWorldRay(glm::vec2 screenCoords)`"

    Convert a click location to a ray in world-space.

??? func "`#!cpp glm::vec3 view::screenCoordsToWorldPosition(glm::vec2 screenCoords)`"

    Convert a click location to a location in world-space, by reading from the scene's depth buffer.

??? func "`#!cpp bool state::doDefaultMouseInteraction`"

    Use this option to (temporarily) disable Polyscope's default mouse clicking/panning/zooming response to mouse movements, so that they will not conflict with your own implemented operations

    If `true`, Polyscope will perform its usual responses to mouse operations, `false` will disable.

### Picking, Selection, and Querying the Scene

"Picking" refers to querying the content under the cursor in the rendered image.  Polyscope implements render buffer-based picking, to efficiently get the object and element under the cursor even on large complex scenes. 

??? func "`#!cpp PickResult pickAtScreenCoords(glm::vec2 screenCoords)`"

    Evaluate a "pick" query to get the contents of the rendered view at a specified location. The return is a `PickResult` struct, see below.

    See also `#!cpp PickResult pickAtBufferInds(glm::ivec2 bufferInds)` for a variant which takes buffer indices as an argument instead.

    Screen coordinates and buffer indices both refer to a location in the rendered 2d image. Screen coordinates are real-valued, whereas buffer indices are integer. On some platforms they may be identical, but on others with high-DPI screens, they may differ. In the common-case of getting mouse positions from ImGui, you want screen coords.


**Example:** picking a faces from a mesh
```cpp
// inside the user-callback, or other code which runs each frame
polyscope::SurfaceMesh myMesh = /* ...  your added mesh ... */ ;

// make only faces clickable in the mesh
myMesh->setSelectionMode(MeshSelectionMode::FacesOnly);

// get the mouse location from ImGui
ImGuiIO& io = ImGui::GetIO();
if (io.MouseClicked[0] && !io.WantCaptureMouse) { // if clicked
  glm::vec2 screenCoords{io.MousePos.x, io.MousePos.y};
  polyscope::PickResult pickResult = polyscope::pickAtScreenCoords(screenCoords);

  // check out pickResult.isHit, pickResult.structureName, pickResult.depth, etc

  // get additional information if we clicked on a mesh
  if(pickResult.isHit && pickResult.structure == myMesh) {
    polyscope::SurfaceMeshPickResult meshPickResult = 
      myMesh->interpretPickResult(pickResult);

    if(meshPickResult.elementType == polyscope::MeshElement::Face) {
      std::cout << "clicked face " << meshPickResult.index << std::endl;
    }
  }
}
```

A pick query returns a combined struct with info such as what structure was clicked on, and depth of the point in the scene.

```cpp
struct PickResult {
  bool isHit = false;                    // did we hit anything?
  Structure* structure = nullptr;        // pointer to the structure under the cursor
  Quantity* quantity = nullptr;          // pointer to the quantity under the cursor (most quantities cannot be picked, you pick the structure instead)
  WeakHandle<Structure> structureHandle; // same as .structure, but with lifetime tracking
  std::string structureType = "";        // structure type which was hit, like "Point Cloud"
  std::string structureName = "";        // name of structure which was hit, like "my_points"
  std::string quantityName = "";         // name of quantity which was hit (most quantities cannot be picked, you pick the structure instead)
  glm::vec2 screenCoords;                // coordinates of the query location
  glm::ivec2 bufferInds;                 // render buffer indices of the query location
  glm::vec3 position;                    // 3d position which was hit, in world space
  float depth;                           // depth to the hit, in world units
  uint64_t localIndex = INVALID_IND_64;  // structure-specific index of the element which was hit
};
```

Additionally, many structures can report additional information about the pick, if they were clicked on, via the `interpretPickResult()` function. For instance, a `SurfaceMesh` can decode whether a vertex/face/edge/etc was clicked on, the index of that element, and barycentric coordinates of the click within a face.


Polyscope also maintains a stateful selection, displayed in the UI to provide information about the content of the scene. It can be accessed via `getSelection()`, `resetSelection()`, `haveSelection()`.

## Overriding Built-In UI Behavior

If desired, you can circumvent Polyscope's standard ImGui style and UI panes, in ordered to build dramatically customized applications.

!!! warning

    Circumventing the standard Polyscope user interface should be considered "advanced" usage. You are more likely to encounter bugs, and you may need to look at the Polyscope source to understand the behavior. The functions listed in this section may change in future versions of Polyscope.

The appearance of the ImGui UI panes can be significantly customized and styled.  See the ImGui documentation (and examples such as [this](https://github.com/ocornut/imgui/issues/707)) for styling options. Polyscope must be able to re-apply the style each time a new context is created, so it must be registered in a callback function rather than set just once.

Two callback functions are made available to configure the appearance of Polyscope's ImGui panes. These callbacks are invoked internally by Polyscope during the setup process. If desired, you can set them to your own custom functions to use alternate styles.  See the ImGui documentation (and examples such as [this](https://github.com/ocornut/imgui/issues/707)) for styling options. Polyscope must be able to re-apply the style each time a new context is created, so it must be registered in a callback function rather than set just once.

**Example:**
```cpp

// set a custom callback 
// (which in this case simply configures the imgui light style)
polyscope::options::configureImGuiStyleCallback = []() {
   ImGui::StyleColorsLight(); 

   // or, implement your own custom imgui style here
};


// initialize polyscope
polyscope::init();

// ... the rest of your program as usual
```

??? func "`#!cpp std::function<void()> options::configureImGuiStyleCallback`"

    A callback function which will be invoked when an ImGui context is created (which may happen several times as Polyscope runs). By default, this is set to invoke `configureImGuiStyle()` from Polyscope's `imgui_config.cpp`, but you may assign your own function to create custom styles. If this callback is null, the default ImGui style will be used.

??? func "`#!cpp std::function<std::tuple<ImFontAtlas*, ImFont*, ImFont*>()> options::prepareImGuiFontsCallback`"

    A callback function which will be invoked exactly once during initialization to construct a font atlas for ImGui to use. The callback should return a tuple of three pointers: a newly created global shared font atlas, a regular font, and a mono font. By default, this is set to invoke `prepareImGuiFonts()` from Polyscope's `imgui_config.cpp`, but you may assign your own function to create custom styles. If this callback is null, default fonts will be used.

    This callback is invoked when `polycope::init()` is called, so if you are going to customize it you **must** do so before `init()`.

    The default implementation of this callback looks something like the following. You can customize your own version of this function to modify any Polyscope fonts, or if you simply want to load additional fonts, do so at the commented note below.

    ```cpp
    std::tuple<ImFontAtlas*, ImFont*, ImFont*> prepareImGuiFonts() {

      ImGuiIO& io = ImGui::GetIO();

      // DPI scaling
      ImVec2 windowSize{static_cast<float>(view::windowWidth), static_cast<float>(view::windowHeight)};
      ImVec2 bufferSize{static_cast<float>(view::bufferWidth), static_cast<float>(view::bufferHeight)};
      ImVec2 imguiCoordScale = {bufferSize.x / windowSize.x, bufferSize.y / windowSize.y};

      // outputs
      ImFontAtlas* fontAtlas = nullptr; // right now this is unused by the caller, but I don't want to change
                                        // this callback signature until I'm more confident about how this
                                        // should work. (And it might be changing in an upcoming imgui version)
      ImFont* regularFont;
      ImFont* monoFont;

      float fontSize = 16.0 * options::uiScale;
      fontSize = std::max(1.0f, std::roundf(fontSize));

      { // add regular font
        ImFontConfig config;
        config.RasterizerDensity = std::max(imguiCoordScale.x, imguiCoordScale.y);
        regularFont = io.Fonts->AddFontFromMemoryCompressedTTF(/* add font */);
      }

      { // add mono font
        ImFontConfig config;
        config.RasterizerDensity = std::max(imguiCoordScale.x, imguiCoordScale.y);
        monoFont = io.Fonts->AddFontFromMemoryCompressedTTF(*/ add font */);
      }

      // load additional fonts here

      io.Fonts->Build();

      return std::tuple<ImFontAtlas*, ImFont*, ImFont*>{fontAtlas, regularFont, monoFont};
    }
    ```



The option `buildGui` can be used to entirely disable all of Polyscope's ImGui UI elements, allowing you to build your own UI. Polyscope will still initialize ImGui and invoke its drawing routines each frame.


??? func "`#!cpp bool options::buildGui`"
    
    This option can be used to disable all of Polyscope's ImGui UI elements, which may be useful for advanced applications which wish to build a fully-custom UI on top of Polyscope.

    If false, Polyscope will not create any ImGui UIs at all, but will still set up ImGui and invoke its render steps each frame. The allows advanced users to create their own UIs totally from scratch and circumvent the standard Polyscope UIs.

    Default: `true`.

The functions `buildPolyscopeGui()`, `buildStructureGui()`, `buildPickGui()`, and `buildUserGuiAndInvokeCallback()` can be used to manually build pieces of the UI one at a time. If you are giving control to the UI via `show()`, you call the first 3 to reproduce the standard UI.

??? func "`#!cpp int options::rightGuiPaneWidth`"

    The width of the right GUI pane.

    Default: `500`.

## Miscellaneous

??? func "`#!cpp std::function<void(const std::vector<std::string>&)> state::filesDroppedCallback`"

    #### files dropped callback

    This callback function is invoked whenever the user drags-and-drops file(s) onto the Polyscope window. Specify your own function implement custom behaviors like loading data.

    Default: `nullptr` (no callback)
