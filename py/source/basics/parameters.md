Many structures and quantities in Polyscope have optional values which can be set to control their appearance or behavior, such as the radius of points in a point cloud or the color of a mesh. These values can generally be manually adjusted in the GUI, or set programmatically in code.

This page documents special features in Polyscope which provide extra functionality while setting these parameters.


## Persistent values

In Polyscope, if you manually set the color of points in a point cloud (for instance), then register a new point cloud with the same name overwriting the original, the new point cloud will inherit the old point cloud's color. This functionality, and other similar behavior, is implemented via _persistent values_.

Persistent values are lightweight wrappers around a variable which on-construction look up the variable in a global cache, and if a cache entry exists take the cached value instead. Any time the variable is written to, its value is recorded in the global cache. Generally, the cache key includes the name of a structure (and quantity if applicable), so a cached variable will only be picked up when names match.

Generally, the user should not manually interact with persistent values ever, all you need to know is that some variables may "magically" remember their old values by pulling them from a cache.
```python
ps_cloud = ps.get_point_cloud("my cloud")
ps_cloud.set_color((0.5, 0.5, 0.5))
# the persistent value is recorded in the cache

# ... later ...

new_cloud = ps.register_point_cloud("my cloud", new_points);
# new_cloud will automatically pick up the pointColor we set above, 
# since this point cloud has the same name
```
Note that this persistence behavior applies even when variables are manually manipulated in the GUI.

## Scaled values

Specifying appearance (such as the radius of points in a point cloud) in global length units can be inconvenient; its generally much easier to set values relatively, which respect to some reasonable length scale.
Many Polyscope parameters take a `relative` option, which is usually `True` by default, to set lengths relatively.

```python
ps_cloud = ps.get_point_cloud("my cloud")

# radius will be 0.05 * lengthScale when used
ps_cloud.set_radius(0.05); 
ps_cloud.set_radius(0.05, relative=True); # same as previous (default is True)
```

However, sometimes you might want to actually use an absolute value for a parameter, for instance to get exactly the same appearance between runs of a program on different data. To support that, scaled values can optionally be set as absolute values, which will _not_ be scaled before use.

```python
# radius will be 1.6 when used
ps_cloud.set_radius(1.6, relative=False)
```

Note that scaled values can be (and often are) used as _persistent values_, as described above; the two concepts are complementary. 
