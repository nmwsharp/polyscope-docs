#!/usr/bin/env python3
"""
Convert .pyi stub files to markdown documentation.
Produces a searchable API reference from nanobind-generated stubs.

WARNING: this file is LLM generated, don't trust it.
"""

import ast
import sys
from pathlib import Path


def simplify_annotation(node: ast.expr | None) -> str:
    """Convert an AST annotation node to a readable string."""
    if node is None:
        return ""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.Attribute):
        return f"{simplify_annotation(node.value)}.{node.attr}"
    if isinstance(node, ast.Subscript):
        base = simplify_annotation(node.value)
        # Simplify verbose annotations
        if base == "Annotated":
            # For Annotated[NDArray[...], ...] just show NDArray[...]
            if isinstance(node.slice, ast.Tuple) and node.slice.elts:
                return simplify_annotation(node.slice.elts[0])
        slice_str = simplify_annotation(node.slice)
        return f"{base}[{slice_str}]"
    if isinstance(node, ast.Tuple):
        return ", ".join(simplify_annotation(e) for e in node.elts)
    if isinstance(node, ast.List):
        return "[" + ", ".join(simplify_annotation(e) for e in node.elts) + "]"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return f"{simplify_annotation(node.left)} | {simplify_annotation(node.right)}"
    return ast.unparse(node)


def format_function(node: ast.FunctionDef, is_method: bool = False) -> str:
    """Format a function/method signature."""
    args = []
    for arg in node.args.args:
        if is_method and arg.arg == "self":
            continue
        ann = simplify_annotation(arg.annotation) if arg.annotation else ""
        if ann:
            args.append(f"{arg.arg}: {ann}")
        else:
            args.append(arg.arg)

    # Add defaults for keyword args
    num_defaults = len(node.args.defaults)
    if num_defaults:
        start = len(node.args.args) - num_defaults
        for i, default in enumerate(node.args.defaults):
            idx = start + i
            if is_method and node.args.args[idx].arg == "self":
                continue
            default_str = ast.unparse(default)
            # Find and update the arg
            arg_idx = idx - (1 if is_method else 0)
            if 0 <= arg_idx < len(args):
                args[arg_idx] = f"{args[arg_idx]} = {default_str}"

    ret = simplify_annotation(node.returns) if node.returns else ""
    ret_str = f" -> {ret}" if ret else ""

    # Multi-line format for functions with more than one argument
    if len(args) > 1:
        args_str = ",\n    ".join(args)
        return f"{node.name}(\n    {args_str},\n    ){ret_str}"
    else:
        return f"{node.name}({', '.join(args)}){ret_str}"


def parse_pyi(filepath: Path) -> dict:
    """Parse a .pyi file and extract classes, functions, and enums."""
    with open(filepath) as f:
        source = f.read()

    tree = ast.parse(source)

    result = {
        "classes": [],
        "functions": [],
        "enums": [],
        "constants": [],
    }

    seen_functions = set()  # Track overloaded functions

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Check if it's an enum
            is_enum = any(
                isinstance(base, ast.Attribute) and base.attr == "Enum"
                for base in node.bases
            )

            if is_enum:
                members = []
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                val = ast.unparse(item.value)
                                members.append(f"{target.id} = {val}")
                result["enums"].append({
                    "name": node.name,
                    "members": members,
                })
            else:
                # Regular class
                properties = []
                methods = []

                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        # Check for property
                        is_property = any(
                            isinstance(d, ast.Name) and d.id == "property"
                            for d in item.decorator_list
                        )
                        is_setter = any(
                            isinstance(d, ast.Attribute) and d.attr == "setter"
                            for d in item.decorator_list
                        )

                        if is_property:
                            ret = simplify_annotation(item.returns) if item.returns else ""
                            properties.append(f"{item.name}: {ret}")
                        elif is_setter:
                            pass  # Skip setters, we show the property type
                        else:
                            sig = format_function(item, is_method=True)
                            # Get docstring if any
                            docstring = ""
                            if (item.body and isinstance(item.body[0], ast.Expr)
                                and isinstance(item.body[0].value, ast.Constant)
                                and isinstance(item.body[0].value.value, str)):
                                docstring = item.body[0].value.value
                            methods.append({"sig": sig, "doc": docstring})

                result["classes"].append({
                    "name": node.name,
                    "properties": properties,
                    "methods": methods,
                })

        elif isinstance(node, ast.FunctionDef):
            sig = format_function(node)
            # Handle overloads - just add all signatures
            if node.name not in seen_functions:
                seen_functions.add(node.name)
                result["functions"].append({"name": node.name, "sigs": [sig]})
            else:
                # Find and append to existing
                for fn in result["functions"]:
                    if fn["name"] == node.name:
                        fn["sigs"].append(sig)
                        break

        elif isinstance(node, ast.Assign):
            # Module-level constants (skip enum duplicates)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    # Skip if it looks like an enum constant
                    if not any(target.id.startswith(e["name"].replace("class ", ""))
                              for e in result["enums"]):
                        val = ast.unparse(node.value)
                        result["constants"].append(f"{target.id}: {val}")

        elif isinstance(node, ast.AnnAssign) and node.target:
            if isinstance(node.target, ast.Name):
                ann = simplify_annotation(node.annotation)
                val = ast.unparse(node.value) if node.value else ""
                result["constants"].append(f"{node.target.id}: {ann} = {val}")

    return result


def generate_markdown(parsed: dict, prepend: str = "") -> str:
    """Generate markdown from parsed data."""
    lines = []
    if prepend:
        lines.append(prepend.rstrip())
        lines.append("")

    # Functions
    if parsed["functions"]:
        lines.append("## Functions\n")
        lines.append("```python")
        for fn in parsed["functions"]:
            for sig in fn["sigs"]:
                lines.append(sig)
        lines.append("```\n")

    # Classes
    if parsed["classes"]:
        lines.append("## Classes\n")
        for cls in parsed["classes"]:
            lines.append(f"### {cls['name']}\n")
            if cls["properties"]:
                lines.append("**Properties:**\n")
                lines.append("```python")
                for prop in cls["properties"]:
                    lines.append(prop)
                lines.append("```\n")
            if cls["methods"]:
                lines.append("**Methods:**\n")
                lines.append("```python")
                for method in cls["methods"]:
                    lines.append(method["sig"])
                lines.append("```\n")

    # Enums
    if parsed["enums"]:
        lines.append("## Enums\n")
        for enum in parsed["enums"]:
            lines.append(f"### {enum['name']}\n")
            lines.append("```python")
            for member in enum["members"]:
                lines.append(member)
            lines.append("```\n")

    # Constants
    if parsed["constants"]:
        lines.append("## Constants\n")
        lines.append("```python")
        for const in parsed["constants"]:
            lines.append(const)
        lines.append("```\n")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: pyi_to_markdown.py <input.pyi> [output.md]")
        print("       pyi_to_markdown.py <directory> [output_dir]")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    script_dir = Path(__file__).parent

    if input_path.is_file():
        # Single file mode
        output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".md")

        parsed = parse_pyi(input_path)
        module_name = input_path.stem

        # Check for prepend file
        prepend = ""
        prepend_file = script_dir / f"{module_name}.md"
        print("checking for", prepend_file)
        if prepend_file.exists():
            print("found prepend file: ", prepend_file)
            prepend = prepend_file.read_text()

        md = generate_markdown(parsed, prepend)

        output_path.write_text(md)
        print(f"Generated {output_path}")

    elif input_path.is_dir():
        # Directory mode
        output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path
        output_dir.mkdir(parents=True, exist_ok=True)

        for pyi_file in sorted(input_path.glob("*.pyi")):
            parsed = parse_pyi(pyi_file)
            module_name = pyi_file.stem

            # Check for prepend file
            prepend = ""
            prepend_file = script_dir / f"{module_name}.md"
            if prepend_file.exists():
                prepend = prepend_file.read_text()

            md = generate_markdown(parsed, module_name, prepend)

            output_path = output_dir / f"{module_name}.md"
            output_path.write_text(md)
            print(f"Generated {output_path}")

    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
