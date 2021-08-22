### Intro

When `polyscope::show()` has been called, Polyscope will optionally invoke user-supplied callback function on every loop iteration. This callback can be used to build a program-specific GUI, update an animation, perform computation, etc.

See [ImGui](https://github.com/ocornut/imgui) for documentation of UI commands.

??? func "`#!cpp std::function<void()> polyscope::state::userCallback`"
    
    ##### user callback

    A function which will be invoked on every main loop iteration by Polyscope, once `show()` has been called.

    If null, nothing will be invoked.

### Example

The code below creates the following UI using a callback.

![callback ui demo]({{url.prefix}}/media/callback_ui_demo.png)

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

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../user_callback) is invoked. This means you can immediately start making ui calls like `ImGui::Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `true`.


??? func "`#!cpp bool options::invokeUserCallbackForNestedShow`"
    
    ##### invoke user callback for nested show

    Suppose you call `polyscope::show()`, and within your callback, another instance of `polyscope::show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your `userCallback` to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope::show()`.

    Default: `false`.

