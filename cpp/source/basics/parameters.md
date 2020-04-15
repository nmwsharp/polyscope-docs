Many structures and quantities in Polyscope have optional values which can be set to control their appearance or behavior, such as the radius of points in a point cloud or the color of a mesh. These values can generally be manually adjusted in the GUI, or set programmatically in code.

This page documents special features in Polyscope which provide extra functionality while setting these parameters.


## Persistent values

In Polyscope, if you manually set the color of points in a point cloud (for instance), then register a new point cloud with the same name overwriting the original, the new point cloud will inherit the old point cloud's color. This functionality, and other similar behavior, is implemented via _persistent values_.

Persistent values are lightweight wrappers around a variable which on-construction look up the variable's in a global cache, and if a cache entry exists take the cached value instead. Any time the variable is written to, its value is recorded in the global cache. Generally, the cache key includes the name of a structure (and quantity if applicable), so a cached variable will only be picked up when names match.

Generally, the user should not manually interact with persistent values ever, all you need to know is that some variables may "magically" remember their old values by pulling them from a cache.
```cpp
PointCloud* psCloud = polyscope::getPointCloud("my cloud");
psCloud->setPointColor(glm::vec3(0.5, 0.5, 0.5));  
// the persistent value is recorded in the cache

// ... later ...

PointCloud* newCloud = polyscope::registerPointCloud("my cloud", new_points);
// newCloud will automatically pick up the pointColor we set above, 
// since this point cloud has the same name
```
Note that this persistence behavior applies even when variables are manually manipulated in the GUI.

??? note "for implementors"

    If writing custom Polyscope library code (e.g. your own custom structures and quantities), here's what you need to know to use persistent values.

    The class `PersistentValue<T>` is templated on the underlying scalar type, like `PersistentValue<double>`. Only a predefined set of types can be used as template arguments because the corresponding global cache must be allocated. See `persistent_value.h` for a listing, which currently includes `bool`, `float`, `double`, `ScaledValue<float>`, `ScaledValue<double>`, `glm::vec3`, and `gl::ColorMapID`.

    Construct a persistent value like
    ```cpp
    PersistentValue<float> myVar("unique_name", 0.5)
    ```
    the variable will the cached value if one exists, and if not take the value `0.5` (and add it to the cache).  Remember to use a globally unique name for the for the name argument; in structures you can use a concatenation of the type name, structure name, and (if applicable) quantity name.

    To access a persistent value, call `myVar.get()`, which returns a reference to the underlying value.

    In some occasions, in particular when using ImGui, you may need to write to a value directly via the pointer from `&myVar.get()`. This is problematic, because the variable does not know it has been written to and thus needs to update the cache. The function `myVar.manuallyUpdated()` can be called to notify the persistent value that it needs to update the cache. The paradigm for using a persistent value with ImGui then looks like
    ```cpp
    if (ImGui::SliderFloat("some text", &myVar.get())) {
      myVar.manuallyChanged();
    }
    ```

## Scaled values

Specifying appearance (such as the radius of points in a point cloud) in global length units can be inconvenient; its generally much easier to set values relatively, which respect to some reasonable length scale.
The `ScaledValue` type tracks such represents such values, if we set `ScaledValue s = 7.`, then `s.asAbsolute()` will return `7. * state::lengthScale` when used.
Most length-valued parameters in Polyscope use this mechanism, and thus are relative by default.

```cpp
using namespace polyscope;
PointCloud* psCloud = polyscope::getPointCloud("my cloud");

// radius will be 0.05 * lengthScale when used
psCloud->pointRadius = ScaledValue<double>::relative(0.05); 
psCloud->pointRadius = relativeValue(0.05); // shorthand, same as previous
psCloud->pointRadius = 0.05; // shorthand, same as previous
```

However, sometimes you might want to actually use an absolute value for a parameter, for instance to get exactly the same appearance between runs of a program on different data. To support that, scaled values can optionally be set as absolute values, which will _not_ be scaled before use.

```cpp
// radius will be 1.6 when used
psCloud->pointRadius = ScaledValue<double>::absolute(1.6) 
psCloud->pointRadius = absoluteValue(1.6); // shorthand, same as previous
```

Note that scaled values can be (and often are) used as _persistent values_, as described above; the two concepts are complementary. 

??? note "for implementors"

    If writing custom Polyscope library code (e.g. your own custom structures and quantities), here's what you need to know to use scaled values.

    The class `ScaledValue<T>` is templated on the scalar type, which basically just needs to support scalar multiplicaiton.

    The examples above show how to construct scaled values as relative or absolute.

    If you want to get the value represented by the `ScaledValue` as an absolute quantity, use `ScaledValue<T>::asAbsolute()`, which scales by `state::lengthScale` if the value is relative.

    Use `ScaledValue<T>::getValuePtr` to get a pointer to the underlying `T`, for instance if using ImGui. A basic ImGui pattern to manipulate the variable looks like:
    ``` cpp
    ImGui::SliderFloat("value ", value.getValuePtr());
    ```

    If the value is a persistent scaled value, like `PersistentValue<ScaledValue<float>>`, it can be used like:
    ```cpp
    // example persistent scaled value
    PersistentValue<ScaledValue<float>>> myVal("unique name", relativeValue(0.03));

    // access
    float myValInWorldCoords = myVal.get().asAbsolute();
    
    // use with ImGUI
    if (ImGui::SliderFloat("my val", myVal.get().getValuePtr())) {
      myVal.manuallyChanged();
    }
    ```
