Most quantities in Polyscope are associated with a particular structure, such as a `PointCloudScalarQuantity` on a `PointCloud`. In contrast, Polyscope uses the term _Floating Quantity_ to refer to generic quantities which can be added to any and all kinds of structures. You can also add them to the root level of the scene, not associated with any structure. 

Images are one example of a floating quantity in Polyscope. You might want to visualize a single image, not specific to any structure, by adding it to the scene at the root level. Or, you might have an image associated with a particular mesh, in which case you could add the image quantity to that `SurfaceMesh` structure.

!!! note "TL;DR What are floating quantities?"

    Floating quantities are quantities that are general and not specific to any kind of structure.

    You have two options for how to add them:

    - Add them as standalone quantities in the scene at the root level, like `polyscope.add_image_quantity(...)`.
    - Add them to _any_ structure of _any_ type, like `pointCloud.add_image_quantity(...)`. This can be useful to associate the quantity with a structure.


The sub-menus to the left give the various floating quantities available.
