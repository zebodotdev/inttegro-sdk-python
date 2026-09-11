from __future__ import annotations

import ast
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).parents[1] / "src" / "inttegro"
NON_RESOURCE_PACKAGES = {"async_resources", "resources", "__pycache__"}


def _following_string(body: list[ast.stmt], index: int) -> str | None:
    if index + 1 >= len(body):
        return None
    following = body[index + 1]
    if (
        isinstance(following, ast.Expr)
        and isinstance(following.value, ast.Constant)
        and isinstance(following.value.value, str)
    ):
        return following.value.value
    return None


class GeneratedDocumentationTests(unittest.TestCase):
    """Keep generated API documentation complete as the contract evolves."""

    def test_every_generated_type_and_field_is_documented(self) -> None:
        failures: list[str] = []
        for directory in sorted(PACKAGE_ROOT.iterdir()):
            if (
                not directory.is_dir()
                or directory.name in NON_RESOURCE_PACKAGES
                or not (directory / "__init__.py").exists()
            ):
                continue
            for path in sorted(directory.glob("*.py")):
                if path.name == "__init__.py":
                    continue
                tree = ast.parse(path.read_text(), filename=str(path))
                generated = "Generated from the Inttegro API contract" in (
                    ast.get_docstring(tree) or ""
                )
                for node in tree.body:
                    if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                        if not ast.get_docstring(node):
                            failures.append(f"{path}:{node.lineno} {node.name} has no docstring")
                        if not generated:
                            continue
                        for index, member in enumerate(node.body):
                            if isinstance(member, ast.AnnAssign) and isinstance(
                                member.target, ast.Name
                            ):
                                field_doc = _following_string(node.body, index)
                                if field_doc is None:
                                    failures.append(
                                        f"{path}:{member.lineno} {node.name}.{member.target.id} "
                                        "has no field documentation"
                                    )
                                elif not all(
                                    marker in field_doc
                                    for marker in ("Python type:", "wire name:", "JSON type:")
                                ):
                                    failures.append(
                                        f"{path}:{member.lineno} {node.name}.{member.target.id} "
                                        "does not document its Python and wire shapes"
                                    )
                            elif (
                                isinstance(member, ast.Assign)
                                and len(member.targets) == 1
                                and isinstance(member.targets[0], ast.Name)
                                and isinstance(member.value, ast.Constant)
                                and isinstance(member.value.value, str)
                            ):
                                if _following_string(node.body, index) is None:
                                    failures.append(
                                        f"{path}:{member.lineno} {node.name}."
                                        f"{member.targets[0].id} has no enum value documentation"
                                    )
                    elif generated and isinstance(node, ast.AnnAssign) and isinstance(
                        node.target, ast.Name
                    ):
                        index = tree.body.index(node)
                        alias_doc = _following_string(tree.body, index)
                        if alias_doc is None:
                            failures.append(
                                f"{path}:{node.lineno} {node.target.id} type alias has no documentation"
                            )
                        elif "selects between" in alias_doc:
                            failures.append(
                                f"{path}:{node.lineno} {node.target.id} type alias uses generic documentation"
                            )
        self.assertEqual([], failures, "\n".join(failures))

    def test_documentation_does_not_describe_compatibility_aliases(self) -> None:
        failures: list[str] = []
        for path in sorted(PACKAGE_ROOT.rglob("*.py")):
            if "backwards-compatible" in path.read_text().lower():
                failures.append(f"{path} describes a compatibility layer")
        self.assertEqual([], failures, "\n".join(failures))

    def test_resource_clients_and_operations_are_documented(self) -> None:
        failures: list[str] = []
        for area in ("resources", "async_resources"):
            for path in sorted((PACKAGE_ROOT / area).glob("*.py")):
                if path.name == "__init__.py":
                    continue
                tree = ast.parse(path.read_text(), filename=str(path))
                if not ast.get_docstring(tree):
                    failures.append(f"{path}:1 module has no docstring")
                for node in ast.walk(tree):
                    if isinstance(
                        node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
                    ) and not node.name.startswith("_"):
                        node_doc = ast.get_docstring(node) or ""
                        if not node_doc:
                            failures.append(
                                f"{path}:{node.lineno} {node.name} has no docstring"
                            )
                        if isinstance(node, ast.ClassDef) and "Access this service" in node_doc:
                            expected_client = (
                                "AsyncInttegroClient" if area == "async_resources" else "InttegroClient"
                            )
                            other_client = (
                                "InttegroClient" if area == "async_resources" else "AsyncInttegroClient"
                            )
                            expected_accessor = f"``{expected_client}.{path.stem}``"
                            if expected_accessor not in node_doc or f"``{other_client}." in node_doc:
                                failures.append(
                                    f"{path}:{node.lineno} {node.name} does not document its "
                                    f"concrete {expected_accessor} accessor"
                                )
        self.assertEqual([], failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
