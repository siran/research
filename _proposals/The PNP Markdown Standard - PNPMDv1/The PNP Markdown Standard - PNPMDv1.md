Perfect. Here’s your **original PNPMD v1.02** text, updated **to v1.03** with just one new, concise section on cross-references and sugar substitution (as actually implemented in your renderer). Everything else is left intact and stylistically consistent with the original document.

---

# The PNP Markdown Standard — PNPMD v1.03

Max Freet, An M. Rodriguez, Adrien Hale
October 2025

---

## One-Sentence Summary

PNPMD v1.03 is a minimal, human-readable *first*, mathematically aware, plain-text Markdown standard for scientific documents.

---

## Abstract

We define the PNP Plain Text Standard PNPMD v1.03 specification.

It is a human-readable *first*, plain-text document format, mathematically aware (using `$...$` and `$$...$$` LaTeX equation blocks) and based on Markdown standards.

The format eases compatibility with naive use of `pandoc`, the default renderer, which converts `.md` to `.pdf`, `.html`, or enhanced `.md` with numbering, links, and TOC.

---

## Keywords

plain-text, research format, markdown, mathjax, pandoc, PNPMD

---

## Introduction

PNPMD v1.03 provides a minimal yet complete Markdown structure for mathematically aware documents.
It keeps the format simple and human-readable *first*: a straight ASCII-text document.
It avoids noisy LaTeX wrappers and PDF-only workflows.
Goals: reproducibility, portability, unambiguous interpretation.

In summary:

* human-readable *first*
* clear, simple, LaTeX, math-aware text
* ASCII art, tikki, etc.

---

## (Suggested) Structure

* Header
* Abstract
* One-Sentence Summary
* Keywords
* Other body sections
* Corresponding Author
* References

### Header

Three lines:

```
% Title
% Author(s)
% Date
```

Title must be ASCII only (pdfLaTeX compatible).

### Abstract

3–5 sentences: problem → method → result → significance.
No citations or equations.

### One-Sentence Summary

One sentence summarizing the paper.

### Keywords

3–6 topical keywords.

### Other body sections (recommended)

Introduction, Theory/Framework, Derivation, Results, Discussion, Conclusion, Next Work, Appendices.

### Corresponding Author

Immediately before References.

### References

Use DOI links where possible.
Avoid footnote-style citations; inline references via `@refname` are encouraged.

---

## References and Cross-References

PNPMD keeps authoring pure plain text.
Cross-linking, numbering, and citations are produced automatically by Pandoc with the **`pandoc-crossref`** filter.

---

## Cross-Reference System and Sugar Substitutions

When using the **PNPMD rendering script**, several syntactic sugars are automatically expanded to Pandoc-compatible links:

| Author Syntax                     | Rendered Equivalent | Condition                             |
| --------------------------------- | ------------------- | ------------------------------------- |
| `{#id}`                           | `[]{#id}`           | for plain prose anchors (no colon)    |
| `@id`                             | `[id](#id)`         | if an anchor or header `{#id}` exists |
| `[label](@id)`                    | `[label](#id)`      | always                                |
| `[label](@sec:id)`                | `[label](#sec:id)`  | always                                |
| `@sec:`, `@fig:`, `@eq:`, `@tbl:` | unchanged           | handled by pandoc-crossref            |
| bare `#id`                        | `[](#id)`           | when not inside code or headings      |

Colon-prefixed anchors (e.g., `{#eq:wave}`) are reserved for crossref numbering and remain untouched.
Both section headers (`## Title {#id}`) and prose anchors (`[]{#id}`) are valid link targets.

This mechanism keeps documents plain-text and fully readable while still producing internally consistent, automatically numbered cross-references in PDF and HTML output.

---

## Formatting Rules

### Math

* Inline math: `$...$` (e.g., `$E = mc^2$`)
* Display math:

  ```
  $$
  F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
  $$
  ```
* Do not use `\[...\]` or `\(...\)`
* Always specify units (SI preferred)

### Characters

* UTF-8 required (pdfLaTeX compatible).
* Unicode symbols allowed only if supported by pdfLaTeX input; otherwise prefer `$...$` or ASCII.
* No math in Abstract or metadata.

### Text Emphasis

Avoid bold/italics/underline unless essential.

### Section Separation

* Separate sections with two blank lines.
* Never use `---` (horizontal rules) to separate sections.
* Do **not** number sections manually; Pandoc handles numbering automatically.

---

## Conclusion

PNPMD v1.03 is a plain-text specification for mathematically aware documents.
It standardizes minimal syntax, automatic cross-referencing, and deterministic conversion through Pandoc with CrossRef.
The format remains simple, portable, and human-readable.

---

## Corresponding author(s)

An M. Rodriguez — [an@preferredframe.com](mailto:an@preferredframe.com)

---

Would you like me to add a small appendix at the end listing the **canonical pandoc command** used for PNPMD v1.03 rendering (for reference in the spec)?
