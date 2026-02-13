#!/usr/bin/env python3
"""
Lovable PRD Builder — Assembly Script

Combines the four PRD documents and the Knowledge Base summary
into a single packaged output for easy distribution.
"""

import os
import sys
from pathlib import Path


def assemble_prd(input_dir: str, output_file: str = "full-prd-package.md"):
    """Assemble all PRD documents into a single markdown file."""

    docs = [
        ("masterplan.md", "MASTERPLAN"),
        ("implementation-plan.md", "IMPLEMENTATION PLAN"),
        ("design-guidelines.md", "DESIGN GUIDELINES"),
        ("app-flow-pages-and-roles.md", "APP FLOW, PAGES & ROLES"),
        ("lovable-knowledge-base.md", "LOVABLE KNOWLEDGE BASE SUMMARY"),
    ]

    input_path = Path(input_dir)
    output_path = input_path / output_file

    sections = []
    missing = []

    for filename, title in docs:
        filepath = input_path / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            sections.append(f"{'=' * 60}\n# {title}\n{'=' * 60}\n\n{content}\n\n")
        else:
            missing.append(filename)

    if missing:
        print(f"Warning: Missing documents: {', '.join(missing)}")

    if sections:
        assembled = (
            "# Complete PRD Package\n\n"
            "This file combines all PRD documents for easy reference.\n"
            "For Lovable.dev, use the individual files or the Knowledge Base summary.\n\n"
            + "\n".join(sections)
        )
        output_path.write_text(assembled, encoding="utf-8")
        print(f"Assembled PRD package saved to: {output_path}")
    else:
        print("Error: No documents found to assemble.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python assemble_prd.py <input-directory> [output-filename]")
        print("Example: python assemble_prd.py ./output full-prd-package.md")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "full-prd-package.md"
    assemble_prd(input_dir, output_file)
