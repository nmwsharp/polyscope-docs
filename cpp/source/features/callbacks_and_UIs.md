### Intro

When `polyscope::show()` has been called, Polyscope will optionally invoke user-supplied callback function as each frame of the interface is redrawn. This callback can be used to build a program-specific GUI, update an animation, perform computation, etc.

See [Dear ImGui](https://github.com/ocornut/imgui) for documentation of UI commands.

??? func "`#!cpp std::function<void()> polyscope::state::userCallback`"
    
    ##### user callback

    A function which will be invoked on every main loop iteration by Polyscope, once `show()` has been called.

    If null, nothing will be invoked.

### Example

The code below creates the following UI using a callback.

![callback ui demo]([[url.prefix]]/media/callback_ui_demo.png)

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/point_cloud.h"

// Parameters which we will set in the callback UI.
int nPts = 2000;
float anotherParam = 3.14;

void mySubroutine() {

  // do something useful...

  // Register a structure
  std::vector<glm::vec3> points;
  for (int i = 0; i < nPts; i++) {
    points.push_back(
        glm::vec3{ polyscope::randomUnit(), 
                   polyscope::randomUnit(), 
                   polyscope::randomUnit()
                  });
  }
  polyscope::registerPointCloud("my point cloud", points);
}

// Your callback functions
void myCallback() {

  // Since options::openImGuiWindowForUserCallback == true by default, 
  // we can immediately start using ImGui commands to build a UI

  ImGui::PushItemWidth(100); // Make ui elements 100 pixels wide,
                             // instead of full width. Must have 
                             // matching PopItemWidth() below.

  ImGui::InputInt("num points", &nPts);             // set a int variable
  ImGui::InputFloat("param value", &anotherParam);  // set a float variable

  if (ImGui::Button("run subroutine")) {
    // executes when button is pressed
    mySubroutine();
  }
  ImGui::SameLine();
  if (ImGui::Button("hi")) {
    polyscope::warning("hi");
  }
  
  ImGui::PopItemWidth();
}

int main(int argc, char** argv) {

  /*
    ...your program setup...
  */ 

  // Initialize polyscope
  polyscope::init();

  // Specify the callback
  polyscope::state::userCallback = myCallback;

  // Give control to the polyscope gui
  polyscope::show();

  return EXIT_SUCCESS;
}

```



### Options

??? func "`#!cpp bool options::openImGuiWindowForUserCallback`"
    
    ##### open imgui window for user callback

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../callbacks_and_UIs) is invoked. This means you can immediately start making ui calls like `ImGui::Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `true`.


??? func "`#!cpp bool options::invokeUserCallbackForNestedShow`"
    
    ##### invoke user callback for nested show

    Suppose you call `polyscope::show()`, and within your callback, another instance of `polyscope::show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your `userCallback` to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope::show()`.

    Default: `false`.


??? func "`#!cpp bool options::giveFocusOnShow`"
    
    ##### give focus on show

    If true, the Polyscope window will request focus from the window manager whenever `show()` is called. If false, the focus state will be left unchanged.

    Default: `false`.


### Mouse Interactions

You can implement custom mouse behaviors on clicks and other actions within your per-frame callback function. Generally, you can use the mouse-related functions available via `ImGui` to implement a wide variety of behaviors.

**Example:** print a variety of info about a mouse click
```cpp

ImGuiIO& io = ImGui::GetIO();
if (io.MouseClicked[0]) { // if the left mouse button was clicked
  // gather values
  glm::vec2 screenCoords{io.MousePos.x, io.MousePos.y};
  glm::vec3 worldRay = polyscope::view::screenCoordsToWorldRay(screenCoords);
  glm::vec3 worldPos = polyscope::view::screenCoordsToWorldPosition(screenCoords);
  std::pair<polyscope::Structure*, size_t> pickPair = 
    polyscope::pick::pickAtScreenCoords(screenCoords);

  // print some values
  std::cout << "    io.MousePos.x: " << io.MousePos.x << " io.MousePos.y: " << io.MousePos.y << std::endl;
  std::cout << "    screenCoords.x: " << screenCoords.x << " screenCoords.y: " << screenCoords.y << std::endl;
  std::cout << "    worldRay: ";
  polyscope::operator<<(std::cout, worldRay) << std::endl;
  std::cout << "    worldPos: ";
  polyscope::operator<<(std::cout, worldPos) << std::endl;
  if (pickPair.first == nullptr) {
    std::cout << "    structure: " << "none" << std::endl;
  } else {
    std::cout << "    structure: " << pickPair.first << " element id: " << pickPair.second << std::endl;
  }
}
```

??? func "`#!cpp glm::vec3 view::screenCoordsToWorldRay(glm::vec2 screenCoords)`"
    
    ##### screen coords to world ray

    Convert a click location to a ray in world-space.


??? func "`#!cpp glm::vec3 view::screenCoordsToWorldPosition(glm::vec2 screenCoords)`"
    
    ##### screen coords to world position

    Convert a click location to a location in world-space, by reading from the scene's depth buffer.


??? func "`#!cpp std::pair<polyscope::Structure*, size_t> pick::pickAtScreenCoords(glm::vec2 screenCoords)`"
    
    ##### pick at screen coords

    Evaluate a "pick" query to get the object onscreen at a given location. Returns a pointer to the structure (or `nullptr` if none), and an index to an element within the structure. The meaning of this index is specific to the structure, for instance for surface meshes it is a packed layout of vertices, then faces, etc.
    

### Custom UIs


If desired, you can circumvent Polyscope's standard ImGui style and UI panes, in ordered to build dramatically customized applications.

!!! warning

    Circumventing the standard Polyscope user interface should be considered "advanced" usage. You are more likely to encounter bugs, and you may need to look at the Polyscope source to understand the behavior. The functions listed in this section may change in future versions of Polyscope.


Two callback functions are made available to configure the appearance of Polyscope's ImGui panes. These callbacks are invoked internally by Polyscope during the setup process. If desired, you can set them to your own custom functions to use alternate styles.

**Example:**
```cpp
// clearing the callback will fall back on default imgui styles
polyscope::options::configureImGuiStyleCallback = nullptr;

// alternately, set a custom callback 
// (which in this case simply configures the imgui light style)
polyscope::options::configureImGuiStyleCallback = []() { ImGui::StyleColorsLight(); };

// clearing the fonts callback will fall back on default imgui fonts
polyscope::options::prepareImGuiFontsCallback = nullptr;

// initialize polyscope
polyscope::init();

// ... the rest of your program as usual
```

??? func "`#!cpp std::function<void()> options::configureImGuiStyleCallback`"
    
    ##### imgui style callback

    A callback function which will be invoked when an ImGui context is created (which may happen several times as Polyscope runs). By default, this is set to invoke `configureImGuiStyle()` from Polyscope's `imgui_config.cpp`, but you may assign your own function to create custom styles. If this callback is null, the default ImGui style will be used.

??? func "`#!cpp std::function<std::tuple<ImFontAtlas*, ImFont*, ImFont*>()> options::prepareImGuiFontsCallback`"
    
    ##### imgui fonts callback

    A callback function which will be invoked exactly once during initialization to construct a font atlas for ImGui to use. The callback should return a tuple of three pointers: a newly created global shared font atlas, a regular font, and a mono font. By default, this is set to invoke `prepareImGuiFonts()` from Polyscope's `imgui_config.cpp`, but you may assign your own function to create custom styles. If this callback is null, default fonts will be used.

    This callback is invoked when `polycope::init()` is called, so if you are going to customize it you **must** do so before `init()`.

    The default implementation of this callback looks something like the following. You can customize your own version of this function to modify any Polyscope fonts, or if you simply want to load additional fonts, do so at the commented note below.

    ```cpp
    std::tuple<ImFontAtlas*, ImFont*, ImFont*> prepareImGuiFonts() {
      ImGuiIO& io = ImGui::GetIO();

      // outputs
      ImFontAtlas* globalFontAtlas;
      ImFont* regularFont;
      ImFont* monoFont;

      { // add regular font
        ImFontConfig config;
        regularFont = io.Fonts->AddFontFromMemoryCompressedTTF(render::getLatoRegularCompressedData(),
                                                               render::getLatoRegularCompressedSize(), 18.0f, &config);
      }

      { // add mono font
        ImFontConfig config;
        monoFont = io.Fonts->AddFontFromMemoryCompressedTTF(render::getCousineRegularCompressedData(),
                                                            render::getCousineRegularCompressedSize(), 16.0f, &config);
      }

      // Add your own additional fonts here

      io.Fonts->Build();
      globalFontAtlas = io.Fonts;

      return std::tuple<ImFontAtlas*, ImFont*, ImFont*>{globalFontAtlas, regularFont, monoFont};
    }
    ```



The option `buildGui` can be used to entirely disable all of Polyscope's ImGui UI elements, allowing you to build your own UI. Polyscope will still initialize ImGui and invoke its drawing routines each frame.


??? func "`#!cpp bool options::buildGui`"
    
    ##### build gui

    This option can be used to disable all of Polyscope's ImGui UI elements, which may be useful for advanced applications which wish to build a fully-custom UI on top of Polyscope.

    If false, Polyscope will not create any ImGui UIs at all, but will still set up ImGui and invoke its render steps each frame. The allows advanced users to create their own UIs totally from scratch and circumvent the standard Polyscope UIs.

    Default: `true`.

The functions `buildPolyscopeGui()`, `buildStructureGui()`, `buildPickGui()`, and `buildUserGuiAndInvokeCallback()` can be used to manually build pieces of the UI one at a time.
