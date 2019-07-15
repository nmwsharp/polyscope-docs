Polyscope is designed as a lightweight general-purpose 3D visualization library. But there's a problem, because different codebases uses different C++ types to store their data: is an array of scalars a `std::vector<double>` or an `Eigen::VectorXf` or some other internal type? Codebases for 3D geometry are particularly guilty of this: I suspect there are at least 1000 distinct 3D vector x-y-z classes floating around github.

Rather than forcing the user to manually convert their data types to some Polyscope types, we implement a series of templated _adaptor_ functions, which attempt to read from the user types via a common set of strategies. These adaptors are applied to the inputs to nearly all Polyscope functions, allowing them to automatically accept user-defined types as inputs.



`#include "polyscope/standardize_data_array.h"`

### Scalar arrays

In our terminology, an _array_ stores a list of 

An array stores an ordered list of values, like a `std::vector<float>` or a 


### Fixed vector types

These are 2D or 3D vectors.


## Extending to your types

If your codebase uses a datatype that cannot be accessed in any of the methods described above, you can provide a function overload which will let Polyscope access it.

??? warning "Overload ambiguity"

    Because we use function overloading to resolve adaptors, there must be _exactly_ one valid accessor function for your data type.

    This means, for instance, that if you type already has a `T.size()` method (and thus the default accessor described above is valid), and then you _also_ define a custom `adaptorF_size` overload as below, you will get errors about ambiguous function overloads.

    The fix is simple: don't define custom adaptor overloads unless you actually need them.

### Using a nonstandard array class

Two functions must be available for a user-defined type `T` to serve as an array:

 - A size adaptor `size_t adaptorF_size(const T& c)`
 - A accessor adaptor `TODO`


Here is an example in which we provide size and access adaptors to use an in-house array type with Polyscope.

```cpp
struct CustomArray {
  std::vector<double> myData;
  size_t bigness() const { return myData.size(); }
};
CustomArray arr_customarray{{0.1, 0.2, 0.3, 0.4, 0.5}};

// Size function for custom array
size_t adaptorF_size(const CustomArray& c) { return c.bigness(); }

// Polyscope includes must come after adaptor functions are declared, so they are visible
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"
```


### Using a nonstandard fixed vector class

