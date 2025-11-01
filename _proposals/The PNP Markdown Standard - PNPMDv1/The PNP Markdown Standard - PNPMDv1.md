% PNPMD Markdown specification — PNPMD v1.03
% Max Freet, An M. Rodriguez, Adrien Hale
% October 2025


## One-Sentence Summary

PNPMD v1.03 is a minimal, human-readable-*first*, mathematically aware, plain-text Markdown standard for documents.


## Abstract

PNPMD is a specificies for human-readable-*first*, plain-text, math-aware, markdown standard. Honor's Pandoc's flavored markdown. Uses Pandoc's cross-referencing filter (eq, fig, table, etc), and adds some syntax sugar to ease cross-referencing and citations.


## Keywords

plain-text, research format, markdown, mathjax, pandoc, PNPMD


## Introduction

PNPMD v1.03 provides a complete Markdown structure for mathematically aware documents.

It keeps the format plain-text and human-readable-*first*.

It avoids noisy LaTeX wrappers and PDF-only workflows.

## (Suggested) Structure

* Header
* One-Sentence Summary
* Abstract
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


### One-Sentence Summary

One sentence summarizing the paper.


### Abstract

3–5 sentences: problem → method → result → significance.

No citations or equations.


### Keywords

3–6 topical keywords.


### Other Body Sections (Recommended)

Introduction, Theory/Framework, Derivation, Results, Discussion, Conclusion, Future Work, Appendices.


### Corresponding Author

Immediately before References.


### References

Use DOI links where possible.


## References and Cross-References

Cross-linking, numbering, and citations are produced automatically by Pandoc with the `pandoc-crossref` filter.


## Cross-Reference System and Sugar Substitutions

When using the **PNPMD rendering script**, several syntactic sugars are automatically expanded to Pandoc-compatible links:

- `{#id}` → `[]{#id}`: For plain prose anchors (no colon).

- `@id` → `[label](#id)`: If a `[label]{#id}` exists

  - `@id` → `[@id](#id)`: otherwise

- `[label](@id)` → `[label](#id)`: Always.

- `[label](@sec:id)` → `[label](#sec:id)`: Always.

- `@sec:`, `@fig:`, `@eq:`, `@tbl:` → *(unchanged)*:
  Handled by `pandoc-crossref`.

- bare `#id` → `[](#id)`: When not inside code blocks,
  headings, or existing links.

Colon-prefixed anchors (e.g., `{#eq:wave}`) are reserved for cross-reference numbering and remain untouched.


## Formatting Rules

### Math

* Inline math: `$...$` (e.g., `$E = mc^2$`)
* Display math:

```
$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$ {#eq:sampleeq}
```

renders as:

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$ {#eq:sampleeq}

And can be referenced as `@eq:sampleeq`, like so:

See @eq:sampleeq

* Do not use `\[...\]` or `\(...\)`
* Always specify units (SI preferred)


### Characters

* UTF-8 required (pdfLaTeX-compatible)
* Unicode symbols allowed only if supported by pdfLaTeX input; otherwise prefer `$...$` or ASCII


### Text Emphasis

Avoid bold/italics/underline unless essential.

Clarity is primary. Don’t pollute the document with unnecessary visual noise.


### Section Separation

* Separate sections with two blank lines
* Never use `---` (horizontal rules) to separate sections
* Do **not** number sections manually; Pandoc handles numbering automatically


## Conclusion

PNPMD v1.03 is a plain-text specification for mathematically aware documents.

It standardizes minimal syntax, automatic cross-referencing, and deterministic conversion through Pandoc with `pandoc-crossref`.

The format remains simple, portable, and human-readable.

PNPMD: where notation and meaning remain human before machine.


## Corresponding Author

An M. Rodriguez: an@preferredframe.com


## Suggested references

Max Freet et al, *The PNP Markdown Standard - PNPMDv1.md*, v1.02,
https://github.com/siran/research/commit/d05ab25e2a78596d201dc6d03cc9cc8efee5c019
{#pnpmd}
