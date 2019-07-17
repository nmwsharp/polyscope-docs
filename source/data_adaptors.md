Polyscope is designed as a lightweight general-purpose 3D visualization library. But there's a problem, because different codebases uses different C++ types to store their data: is an array of scalars a `std::vector<double>` or an `Eigen::VectorXf` or some other internal type? Codebases for 3D geometry are particularly guilty of this: there are probably several hundred distinct 3D vector x-y-z classes floating around github.

Rather than forcing the user to manually convert their data types to some Polyscope types, we implement a series of templated _adaptor_ functions, which attempt to read from the user types via a common set of strategies. These adaptors are applied to the inputs to nearly all Polyscope functions, allowing them to automatically accept user-defined types as inputs.

**You don't need to do anything special to use these adaptors!** They are applied internally to the arguments of nearly every Polyscope function, like the `vertices` and `faces` arguments of `registerSurfaceMesh("name", vertices, faces)`. This section outlines how the adaptors will try to read from your data, and how to extend them for unusual datatypes which are not automatically handled.

These functions live in `#include "polyscope/standardize_data_array.h"`. It's fairly well-commented---check it out to see how all this works under the hood!

--- 
## Fixed size vector types

These are 2D or 3D vectors whose size are known at compile time, commonly used to represent things like positions (3D), or UV coordinates (2D).

Examples of 3D vector types that Polyscope can read from out of the box include `glm::vec3`, `Eigen::Vector3d`, and `std::array<double, 3>` (likewise for 2D).

#### Hierarchy

Polyscope will attempt to access an input 2D vector in the following ways, in order of decreasing precedence:

  - any user-defined function (see below)
  - bracketed indices (like `vec[0]` and `vec[1]`)
  - members `x`,`y` (like `vec.x` and `vec.y`)
  - members `u`,`v` (like `vec.u` and `vec.v`)
  - members functions `real()`/`imag()` (like `vec.real()` and `vec.imag()`)

Polyscope will attempt to access an **input 3D vector** in the following ways, in order of decreasing precedence:

  - any user-defined function (see below)
  - bracketed indices (like `vec[0]`, `vec[1]`, and `vec[2]`)
  - members `x`,`y`,`z` (like `vec.x`, `vec.y`, and `vec.z`)

??? warning "using Eigen fixed-size vectorizable types"

    If you are using **fixed-sized, vectorizable** Eigen types like `Eigen::Vector2f` and `Eigen::Vector4f` as your 2D/3D vector types, there are special, tricky alignment rules imposed by Eigen which must be respected.  For instance, a `std::vector<Eigen::Vector2f>` is _not_ a valid type; using it will lead to tricky-to-debug segfaults.
    
    Polyscope makes a best effort to avoid problems when the caller's fixed vector type has alignment constraints, but beware---these are dangerous waters.

    See Eigen's documentation [here](https://eigen.tuxfamily.org/dox-devel/group__TopicPassingByValue.html) and [here](https://eigen.tuxfamily.org/dox-devel/group__TopicStlContainers.html) for more information.

??? note "extending vector access"

    #### Extending

    Suppose you have an in-house vector type which cannot be accessed by any strategy in the hierarchy above. You can define a custom function that accesses the elements of your type:
    ```cpp
    YOUR_TYPES_SCALAR adaptorF_custom_accessVector2Value(const YOUR_TYPE& v, unsigned int ind);
    ```
    The array adaptors will pick up this function and use it to access your type.

    Example:
    ```cpp
    // A vector2 type with unusual access
    struct UserVector2Custom {
      double foo;
      double bar;
    };

    // Define an accessor to teach Polyscope to read from your type
    double adaptorF_custom_accessVector2Value(const UserVector2Custom& v, unsigned int ind) {
      if (ind == 0) return v.foo;
      if (ind == 1) return v.bar;
      throw std::logic_error("bad access");
      return -1.;
    }

    // Now Polyscope functions can take this type as input!
    ```

    The same principle applies for 3D vectors, where the relevant function is named
    ```cpp
    YOUR_TYPES_SCALAR adaptorF_custom_accessVector3Value(const YOUR_TYPE& v, unsigned int ind);
    ```

---
## Array size

The three array adaptor variants below (scalar array, vector array, and nested array) all assume the ability to read the size of an input array. 

#### Hierarchy

Polyscope will attempt to read the length of an input array in the following ways, in decreasing order of precedence:

  - any user-defined function (see below)
  - a `.rows()` member function (like `inputData.rows()`)
  - a `.size()` member function (like `inputData.size()`)

??? note "extending array size"

    #### Extending

    Suppose you have an in-house array type whose length cannot be read by any strategy in the hierarchy above. You can define a custom function that reads the length like:
    ```cpp
    size_t adaptorF_custom_size(const YOUR_ARRAY_TYPE& c);
    ```
    The array adaptors will pick up this function and use it to access your type.

    Example:
    ```cpp
    // Array with custom length function called "bigness()"
    struct UserArray {
      std::vector<double> myData;
      size_t bigness() const { return myData.size(); }
    };

    // Size function for custom array
    size_t adaptorF_custom_size(const UserArray& c) { return c.bigness(); }
    ```

---
## Scalar arrays

A scalar array is a long list of values, like a `float` at each point in a point cloud, or an `int` at each vertex of a mesh. We will use the type `S` to refer to the inner scalar type of an array, like `float` in `std::vector<float>`.

Examples of scalar arrays that Polyscope can read from out of the box include `std::vector<float>`, `Eigen::VectorXd`, and `std::list<int>`.

#### Hierarchy

Polyscope will attempt to access an input scalar array in the following ways, in order of decreasing precedence:

  - any user-defined function (see below)
  - bracketed index access (like `array[i]`)
  - parenthesis index access (like `array(i)`)
  - for-each iteration (like `array.begin()`, `array.end()`)

??? note "extending scalar array access"

    #### Extending

    Suppose you have an in-house array type whose elements cannot be accessed by any strategy in the hierarchy above. You can define a custom function that converts your arrays to a `std::vector<S>` like
    ```cpp
    std::vector<YOUR_SCALAR_TYPE> adaptorF_custom_convertToStdVector(const YOUR_ARRAY_TYPE& c) {
    ```
    The array adaptors will pick up this function and use it to access your type.

    Example:
    ```cpp
    // User array with unusual access
    struct UserArrayFuncAccess {
      std::vector<double> myData;
      size_t size() const { return myData.size(); }
    };

    std::vector<double> adaptorF_custom_convertToStdVector(const UserArrayFuncAccess& c) {
      std::vector<double> out;
      for (auto x : c.myData) {
        out.push_back(x);
      }
      return out;
    }
    ```
---

## Arrays of vectors

These are arrays of values where each element of the array is itself a fixed-size vector type, like the 3D position of each point in a point cloud, or a list of edges in a graph. Note that these arrays must have an inner dimension which is fixed and known at compile time.

Examples of vector arrays that Polyscope can read from out of the box include `std::vector<glm::vec3>`, `Eigen::Matrx<N,3>`, and `std::list<std::array<int,2>>`.

#### Hierarchy

Polyscope will attempt to access an input array of vectors in the following ways, in order of decreasing precedence:

   - any user-defined function (see below)
   - dense parenthesis access (like `array(i,j)`)
   - double bracket access (like `array[i][j]`)
   - outer type bracket-accessible, inner type anything convertible to Vector2/3 (like `array[i].x`)
   - outer type iterable, inner type anything convertible to Vector2/3 (like `for(auto vec : array)` and `vec.u`).
   - outer type iterable, inner type bracket-accessible (like `for(auto vec : array)` and `vec[7]`)

Notice that two these options make use of the [fixed-sized vector adaptors](#fixed-size-vector-types). Once Polyscope can read the elements of `SOME_VEC3_TYPE`, it can also read from `std::vector<SOME_VEC3_TYPE>`, etc.

The sizes of the inner vector type are generally not checked by Polyscope, so be sure you're passing in something with the right dimensions! If a function expects an array of 3D vectors, don't give it an array of 2D vectors.

#### Extending

??? note "extending array-of-vectors access"

    #### Extending

    Suppose you have an in-house array-of-vectors type whose elements cannot be accessed by any strategy in the hierarchy above. You can define a custom function that converts your arrays to a `std::vector<S>` like
    ```cpp
    std::vector<std::array<SCALAR_T,N>> adaptorF_custom_convertArrayOfVectorToStdVector(const YOUR_ARRAY_TYPE& c) 
    ```
    The array adaptors will pick up this function and use it to access your type. Really, the return type of this method can anything that supports `.size()` and bracket access; `std::vector<std::vector<>>` would also work. 
    The size of the inner vector is not checked, so be sure it's right!

    Example:
    ```cpp
    // An array of vectors with an unusual access scheme
    struct UserArrayVectorCustom {
      std::list<SOME_TYPE> vals;
      size_t size() const { return vals.size(); }
    };

    // Define a custom access function
    std::vector<std::array<double, 3>>
    adaptorF_custom_convertArrayOfVectorToStdVector(const UserArrayVectorCustom& inputData) {
      std::vector<std::array<double, 3>> out;
      for (auto v : inputData.vals) {
        out.push_back({v.x(), v.y(), v.z()});
      }
      return out;
    }
    ```

---
## Nested arrays

These are arrays-of-arrays, like the list of vertex indices for each face in a polygon mesh. Unlike the arrays-of-vectors above, the dimensions of the inner arrays need not be known at compile time, and can vary (though arrays with fixed-sized inner dimension are also valid input).

Examples of vector arrays that Polyscope can read from out of the box include `std::vector<std::vector<int>>`, `Eigen::Matrix<double,N,3>`, and `std::vector<std::list<size_t>>`.

#### Hierarchy

Polyscope will attempt to access a nested array in the following ways, in order of decreasing precedence:

   - any user defined function
   - dense callable (parenthesis) access on a type that supports `array.rows()` and `array.cols()` (like `array(i,j)`).
   - outer type bracket-accessible, inner type anything that can be accessed as a scalar array (like `array[i][j]`)
   - outer type parenthesis-accessible, inner type anything that can be accessed as a scalar array (like `array(j)[i]`)
   - outer type iterable, inner type anything that can be accessed as a scalar array (like `for(auto inner : array)` and `inner[7]`).


Notice that several of these options make use of the [scalar array adaptors](#scalar-arrays). Once Polyscope can read from `YOUR_ARRAY<S>`, it can also read from `std::vector<YOUR_ARRAY<S>>`, etc.

??? note "extending nested array access"

    #### Extending

    Suppose you have an in-house nested array type whose elements cannot be accessed by any strategy in the hierarchy above. You can define a custom function that converts your arrays to a `std::vector<std::vector<S>>` like
    ```cpp
    std::vector<std::vector<S>> adaptorF_custom_convertNestedArrayToStdVector(const YOUR_NESTED_ARRAY& inputData) {

    ```
    The array adaptors will pick up this function and use it to access your type. 

    Example:
    ```cpp
    // A nested list type with unusual access
    struct UserNestedListCustom {
      std::list<std::vector<int>> vals;
      size_t size() const { return vals.size(); }
    };
    std::vector<std::vector<int>> adaptorF_custom_convertNestedArrayToStdVector(const UserNestedListCustom& inputData) {
      std::vector<std::vector<int>> out;
      for (auto v : inputData.vals) {
        std::vector<int> inner;
        for (auto x : v) {
          inner.push_back(x);
        }
        out.push_back(inner);
      }
      return out;
    }
    ```

---
## Debugging

One downside to our "clever" use of templates is that compiler error messages can be borderline incomprehensible. Generally, the best debugging strategy is to carefully read the documentation and ensure you are passing in data that makes sense. In most cases, the problem is something simple, like passing a 3D vector where a 2D vector is needed, or mixing up the order of arguments.

However, if you are deep in the weeds trying to debug why your type isn't matching against the template hierarchy (or why a custom function isn't being used), consider adding the define
```cpp
#define POLYSCOPE_NO_STANDARDIZE_FALLTHROUGH
```
anywhere before the Polyscope includes. This will cause most compilers to print the long scary list of all template substitutions which were considered and rejected, which you can slowly parse to aid you on your quest.
