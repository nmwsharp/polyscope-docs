Polyscope uses *matcaps* to render the appearance of objects in the scene, as opposed to more traditional configurations of lights and shading models, etc. A matcap is a small image of a material, which is sampled by the renderer to query the materials' appearance from a some angle. Scene information like lighting is implicitly baked in to the matcap image.

Most objects in Polyscope (surface meshes, point clouds, vectors, etc) expose a `#!cpp setMaterial(std::string)` option to choose a material for the object's appearance. Additionally, materials can generally be set in the UI from `[Options] --> [Material]`.

## Blended materials

In Polyscope, we often want to adjust set custom colors for rendered objects. This can be a constant color for the object (to distinguish structures in a scene), or a varying color across a surface (when color-mapping scalar quantities).  Traditionally, matcaps don't really support setting an albedo color like this, but we achieve the effect in Polyscope by blending between basis matcaps.

Instead of just using a single material image, we take four images of the material, representing basis red, green, blue, and black components.

![sample colormap](/media/materials/clay_r.jpg){: style="height:200px;"}
![sample colormap](/media/materials/clay_g.jpg){: style="height:200px;"}
![sample colormap](/media/materials/clay_b.jpg){: style="height:200px;"}
![sample colormap](/media/materials/clay_k.jpg){: style="height:200px;"}

At runtime, to generate a color from a triple of `rgb` values each in the range `[0,1]`, we sample the images like:

```cpp
outputColor = r * basis_r + g * basis_g + b * basis_b + (1. - r - g - b) * basis_k
```

Intuitively, this strategy presumes the underlying material has a light response which is a linear function of the color, plus another component which is independent of the color.  Crucially, Polyscope uses a linear lighting workflow and performs this blending on linear matcaps before tone-mapping, which is necessary for the results to look reasonable across the full color space.

Materials which which support this blending are denoted by `(rgb)` in the options menu.  Ordinary static matcaps consisting of a single image can still be used as materials, but will ignore any color maps or other options.

## Built-in materials

Polyscope supports the following built-in materials:

| **Name** | **String Key** |  **Blendable** | Image |
--- | --- | --- | ---
clay | `clay` | yes | ![clay image](/media/materials/clay_r.jpg){: style="width:100px;"}
wax | `wax` | yes | ![wax image](/media/materials/wax_r.jpg){: style="width:100px;"}
candy | `candy` | yes | ![candy image](/media/materials/candy_r.jpg){: style="width:100px;"}
mud[^1] | `mud` | no | ![mud image](/media/materials/mud.jpg){: style="width:100px;"}
ceramic[^1] | `ceramic` | no | ![ceramic image](/media/materials/ceramic.jpg){: style="width:100px;"}
jade[^1] | `jade` | no | ![jade image](/media/materials/jade.jpg){: style="width:100px;"}
normal[^1] | `normal` | no | ![normal image](/media/materials/normal.jpg){: style="width:100px;"}


[^1]: The matcaps are from the Blender matcap repository, available under a [CC0/public domain license](https://github.com/blender/blender/blob/master/release/datafiles/studiolights/matcap/license.txt). Thanks to the Blender community for contributing them!

## Loading custom materials

Custom matcaps can be loaded at runtime from image files and used anywhere materials are used. Loading can be performed with the UI from `[Appearance] --> [Materials] --> [Load material]`, or programatically using the function below. For blendable matcaps, if the single filename `mat.hdr` is given, Polyscope will try to load `mat_r.hdr`, `mat_g.hdr`, etc.

Ideally, matcap images should be linear `.hdr` images for best results, but any image will work. If other image formats are given, the input is assumed to be non-linear and will be inverse-tonemapped with `intensity=1` and `gamma=2.2` before use.  Most common image formats are accepted (anything `stb_image` can read).

??? func "`#!cpp void polyscope::loadStaticMaterial(std::string matName, std::string filename)`"

    ##### loadStaticMaterial

    Load a new static (non-blendable) material from a single image file `filename`. The new material will be called `matName`.


??? func "`#!cpp void polyscope::loadBlendableMaterial(std::string matName, std::array<std::string, 4> filenames)`"

    ##### loadBlendableMaterial 

    Load a new blendable material from image files `filenames`, corresponding to red, green, blue, and black basis materials. The new material will be called `matName`.


??? func "`#!cpp void polyscope::loadBlendableMaterial(std::string matName, std::string filenameBase, std::string filenameExt)`"

    ##### loadBlendableMaterial 

    Same as above, but the four filenames will be generated as `filenameBase + "_r" + filenameExt`, etc.

