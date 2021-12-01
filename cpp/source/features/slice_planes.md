Geometric data often has complex internal structures. Slice planes can be added to the scene to cull away parts of an object and inspect its interior. These planes can be manipulated either programmatically or manually in the GUI.

<video width=100% autoplay muted loop>
  <source src="/media/movies/slice_slide.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


**Example**: sweep a slice plane through the scene to produce the animation above

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"
#include <igl/readOBJ.h>

// Initialize Polyscope
polyscope::init();

// Read & register the mesh
Eigen::MatrixXd meshV;
Eigen::MatrixXi meshF;
igl::readOBJ(filename, meshV, meshF);
polyscope::SurfaceMesh* psMesh = polyscope::registerSurfaceMesh("input mesh", meshV, meshF);

// Add a slice plane
polyscope::SlicePlane* psPlane = polyscope::addSceneSlicePlane();
psPlane->setDrawPlane(true);  // render the semi-transparent gridded plane
psPlane->setDrawWidget(true);

// Animate the plane sliding along the scene
for (float t = 0.; t < 2. * M_PI; t += 2. * M_PI / 120) {
    float pos = std::cos(t) * .8 + .2;
    psPlane->setPose(glm::vec3{0., 0., pos}, glm::vec3{0., 0., -1.});

    // Take a screenshot at each frame
    polyscope::screenshot(false);
}
```

Slice planes can also be manipulated in the GUI under `[View] --> [Slice Planes]`, where you can add and remove slice planes and control whether they are active and widgets are visible. When a plane is active in the scene, you can drag the 3D widget to adjust its pose. Additionally, for each structure, `[Options] --> [Slice Planes]` allows you to toggle whether the slice plane effects that structure.


### Creating and modifying slice planes

??? func "`#!cpp SlicePlane* addSceneSlicePlane(bool initiallyVisible=false)`"
    
    ##### add slice plane
    
    Add a new slice plane to the scene. An arbitrary number of slices planes may be added.

    If `initiallyVisible = false`, then the widget and plane grid will be disabled by default, which is usually what one wants when creating a slice plane programatically.


??? func "`#!cpp void removeLastSceneSlicePlane()`"
    
    ##### remove slice plane
    
    Remove the most recently created slice plane.


??? func "`#!cpp const std::string SlicePlane::name`"
    
    ##### name

    The unique name of the slice plane, which can be accessed like `myPlane->name`.

??? func "`#!cpp void SlicePlane::setPose(glm::vec3 planePosition, glm::vec3 planeNormal)`"
    
    ##### set pose

    Set the position and orientation of the slice plane.

      - `planePosition` is any 3D position which the plane touches (the center of the plane)
      - `planeNormal` is a vector giving the normal direction of the plane, objects in this negative side of the plane will be culled
    

??? func "`#!cpp void SlicePlane::setActive(bool newVal)`"
    
    ##### active
 
    Set the slice plane to be active or not. If inactive, the slice plane will not have any effect on any structures in the scene, nor will it be shown in the GUI view.


??? func "`#!cpp bool SlicePlane::getActive()`"
    
    Test whether the slice plane is active.


??? func "`#!cpp void SlicePlane::setDrawPlane(bool newVal)`"
    
    ##### draw plane
    
    Set the slice plane to draw its plane (as a colored, semi-transparent grid). If `false` the slice plane will still slice objects, but the plane itself will not be rendered.


??? func "`#!cpp bool SlicePlane::getDrawPlane()`"
    
    Test whether the slice plane is drawing its plane.


??? func "`#!cpp void SlicePlane::setDrawWidget(bool newVal)`"
    
    ##### draw widget
    
    Set the slice plane to draw its control widget (a grey and colored cube with handles for translations and rotations). If `false` the slice plane will still slice objects, but the widget will not be rendered.

    Note that regardless of this setting, the widget will not be visible in any screenshots by default, because it is treated as part of the GUI interface, like the ImGUI widow panes.


??? func "`#!cpp bool SlicePlane::getDrawWidget()`"
    
    Test whether the slice plane is drawing its widget.


### Per-structure ignore slice planes

By default, every slice plane affects all content in the scene. However, we can also make a particular structure ignore a given slice plane, so that it only slices through some of the objects in the scene. This can be set in the GUI for each structure under `[Options] --> [Slice Planes]`, or programatically with the function below.

```cpp
polyscope::SurfaceMesh* psMesh = polyscope::registerSurfaceMesh("input mesh", meshV, meshF);
polyscope::SlicePlane* psPlane = polyscope::addSceneSlicePlane();
psMesh->setIgnoreSlicePlane(psPlane->name, true);
```

??? func "`#!cpp Structure* Structure::setIgnoreSlicePlane(std::string name, bool newValue)`"
    
    ##### ignore plane
    
    Set a slice plane to be ignored by the structure. If `newValue` is `true` the slice plane will be ignored, and if `false` it will be respected.

??? func "`#!cpp bool Structure::getIgnoreSlicePlane(std::string name)`"

    Get if a slice plane is currently being ignored by the structure.

### Cull whole elements

For some structures, slice planes can be set to discretely cull away whole elements, rather than slicing directly through the middle of an element.  This option can be set in the GUI for each structure under `[Options] --> [Slice Planes]`, or programatically with the function below.

![cull whole elements settings]([[url.prefix]]/media/cull_whole_elements.png)

```cpp
polyscope::SurfaceMesh* psMesh = polyscope::registerSurfaceMesh("input mesh", meshV, meshF);
polyscope::SlicePlane* psPlane = polyscope::addSceneSlicePlane();
psMesh->setCullWholeElements(false);
```

??? func "`#!cpp Structure* Structure::setCullWholeElements(bool newVal)`"
    
    ##### set cull whole elements

    If `true`, slice planes will affect this structure by culling whole elements (tets, triangles, points, etc), rather than slicing through the middle of the elements.

    Note that not all structures may support culling whole elements. If not supported, this setting will do nothing.
    
    Default: false.

??? func "`#!cpp bool Structure::getCullWholeElements()`"

    Get whether the cull whole elements setting is applied.

### Inspecting volume meshes

![slice plane volume inspect image]([[url.prefix]]/media/slice_plane_volume_inspect.png)

Slice planes can also _inspect_ volume meshes, rendering a surface where the structure is cut by the plane. Not only does this help to visualize the interior of the shape, but scalar and color quantities can be drawn along the plane to better inspect values on the interior of the mesh.

This can also be set in the UI under `[View] --> [Slice Planes] --> [Inspect]`. This option will only be available when there is at least one volume mesh in the scene.

If the volume mesh has a vertex scalar or vertex color quantity enabled, it will be automatically drawn on the inspecting slice plane.

??? func "`#!cpp void SlicePlane::setVolumeMeshToInspect(std::string meshName)`"

    Give the name of a volume mesh to inspect. Pass the empty string `""` to clear the inspection.

??? func "`#!cpp std::string SlicePlane::getVolumeMeshToInspect()`"

    Get the volume mesh being inspected.
