Many structures and quantities in Polyscope have optional values which can be set to control their appearance or behavior, such as the radius of points in a point cloud or the color of a mesh. These values can generally be manually adjusted in the GUI, or set programmatically in code.

This page documents special features in Polyscope which provide extra functionality while setting these parameters.


## Sticky values

## Scaled values

Specifying appearance (such as the radius of points in a point cloud) in global length units can be inconvenient; its generally much easier to set values relatively, which respect to some reasonable length scale.
The `ScaledValue` type tracks such represents such values, if we set `ScaledValue s = 7.`, then `s.get()` will return `7. * state::lengthScale` when used.
Most length-valued parameters in Polyscope use this mechanism, and thus are relative by default.

```cpp
using namespace polyscope;
PointCloud* psCloud = polyscope::getPointCloud("my cloud");

// radius will be 0.05 * lengthScale when used
psCloud->pointRadius = ScaledValue<double>::relative(0.05); 
psCloud->pointRadius = 0.05; // shorthand, same as previous
```

However, sometimes you might want to actually use an absolute value for a parameter, for instance to get exactly the same appearance between runs of a program on different data. To support that, scaled values can optionally be set as absolute values, which will _not_ be scaled before use.

```cpp
// radius will be 1.6 when used
psCloud->pointRadius = ScaledValue<double>::absolute(1.6) 
psCloud->pointRadius = absoluteValue(1.6); // shorthand, same as previous
```

Note that scaled values can be (and often are) used as _sticky values_, as described above; the two concepts are complementary. 
