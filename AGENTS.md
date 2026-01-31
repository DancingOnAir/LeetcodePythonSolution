# Leetcode Python Solution - Agents Guide

This repository contains Python solutions for Leetcode problems, organized by algorithm or data structure categories.

## 1. Build & Test Commands

Since this is a collection of standalone Python scripts, there is no centralized build process. Each file is self-contained.

### Running a Solution
To run a specific solution and its embedded tests:

```bash
python3 <category>/<problem_id>_<problem_name>.py
```

Example:
```bash
python3 Tree/0543_diameter_of_binary_tree.py
```

### Testing
- Tests are embedded directly in the solution file.
- Look for a function named `test_<problem_name>` (snake_case).
- The `if __name__ == '__main__':` block executes this test function.
- Tests use simple `assert` statements.
- **Action**: When adding a new solution, YOU MUST include a test function with at least the example cases provided in the problem description.

## 2. Code Style Guidelines

### File Naming
- **Format**: `<category>/<problem_id>_<problem_name_snake_case>.py`
- **Example**: `Tree/0543_diameter_of_binary_tree.py`
- Pad the problem ID with zeros to 4 digits (e.g., `0001`, `0543`).

### Structure
Each file should contain:
1.  **Imports**: Standard imports, typically `from typing import List, Optional, ...`.
2.  **Data Structure Definitions**: If the problem requires a specific data structure (e.g., `TreeNode`, `ListNode`), include the class definition at the top, after imports.
3.  **Solution Class**: A class named `Solution`.
4.  **Methods**: Implement the solution method(s) inside `Solution`.
    - Use the exact method signature provided by Leetcode.
    - Use **camelCase** for method names (as per Leetcode default).
5.  **Test Function**: A standalone function `test_...` outside the class.
6.  **Entry Point**: `if __name__ == '__main__':` block calling the test function.

### Type Hinting
- **Mandatory**: Use Python type hints for all method arguments and return values.
- **Imports**: Use `typing` module (e.g., `List[int]`, `Optional[TreeNode]`).

### Formatting & Conventions
- **Indentation**: 4 spaces.
- **Naming**:
    - Variables: snake_case (e.g., `max_val`, `cur_node`).
    - Solution Methods: camelCase (match Leetcode).
    - Helper Methods: snake_case (unless Leetcode requires otherwise).
- **Comments**:
    - Add comments for complex logic or specific algorithm steps (e.g., "dfs", "binary search").
    - Minimal docstrings required, but code should be self-explanatory.

### Error Handling
- Do not suppress errors with `try...except` unless part of the solution logic.
- Do not use `as any` or ignore type checkers generally, though strict type checking is not enforced by a CI pipeline here.

## 3. Example Template

```python
from typing import List, Optional

# Definition for a binary tree node (if applicable)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def exampleMethod(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Implementation
        return 1

def test_example_method():
    solution = Solution()
    # Test cases
    root = TreeNode(1)
    assert solution.exampleMethod(root) == 1, 'test case 1 failed'
    print('All tests passed')

if __name__ == '__main__':
    test_example_method()
```

## 4. Git & Workflow
- Ensure you are working in the correct category directory.
- If a category directory does not exist for the problem type (e.g., `SegmentTree`), create it.
- **Commit Messages**: format `category: problem_id problem_name` (e.g., `Tree: 0543 diameter of binary tree`).
