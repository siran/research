% The PNP Markdown Standard – PNPMD v1.001
% Max Freet, An M. Rodríguez, Adrien Hale
% August 11, 2025

## Abstract

We define the PNP Plain Text Standard v1.001 (PNPMD v1.001).
It is based on mathematically aware Markdown using `$...$` and `$$...$$` LaTeX equation blocks.
The format eases compatibility with naive use of rendering engines that convert `.md` to various targets (`.pdf`, `.html`, etc.).

## One-Sentence Summary

PNPMD v1.001 is a minimal, human-readable *first*, mathematically aware, plain-text, Markdown standard for documents.

## Keywords

plain-text, research format, markdown, mathjax, html, PNPMD

## Introduction

The PNPMD v1.001 format provides a minimal yet complete Markdown structure for mathematically aware documents.
The format allows for naive use of tools like `pandoc` that render `.md` directly to PDF or HTML.
It keeps the format simple and human-readable *first*: a straight ASCII-text document.
It avoids relying on human-unreadable, unnecessary, or noisy LaTeX wrappers and PDF-only workflows.
Our goals are reproducibility, portability, and unambiguous interpretation.
It is also well-suited to version-controlled repositories.

In summary:

- human-readable *first*
- clear, simple, LaTeX, math-aware text
- ASCII art
- even tikki figures

## Structure

In summary,

- Header
- Abstract
- One-Sentence Summary
- Keywords
- Other body sections
- Corresponding Author
- References


In more detail,

- **Header**

First three lines:
```

% Title
% Author(s)
% Date

```

- **Abstract**

3–5 sentences: problem → method → result → significance.
Avoid citations or equations here.

- **One-Sentence Summary**

Single self-contained sentence summarizing the paper.

- **Keywords**

3–6 topical keywords.

- **Other Body Sections**

Recommendeded sections:

- Introduction — motivation, novelty, context.
- Theory / Framework — fundamental definitions and starting equations from first principles.
- Derivation — detailed steps, explicit approximations with justification.
- Results — final closed-form laws, constants, predictions; include numerical evaluations with units.
- Discussion — interpretation, implications, and limits.
- Conclusion — concise recap of contributions, assumptions, and scope.
- Next Work — proposed future directions.
- Appendices — supplementary derivations, datasets, or proofs.

6. **Corresponding Author**

- Immediately before References:

7. **References**

- Use DOI links where possible.
- Avoid footnote-style citations; inline references are sufficient.


## Formatting Rules

**Math**:

- Inline math: `$...$`
 Example: $E = mc^2$
- Display math blocks: `$$...$$`

 Example:
 $$
 F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
 $$

- **DO NOT USE** `\[...\]` and `\(...\)` either for inline or block math
- Always specify units. SI units preferred

Example: $R = 5.29177210903\times 10^{-11}\,\mathrm{m}$

**Characters**:

- UTF-8 encoding required.
- Although some Greek, math symbols, and Unicode arrows (→, ←) are allowed **only if** they are supported by the default `utf8` inputenc mapping in pdfLaTeX, $...$ is preferred.
- Any unmapped Unicode symbols must be replaced either by $...$ or their ascii counterpart.
- No inline math math format other that $...$ OR $$...$$.
- No math in abstract or metadata.

**Text emphasis**:

- Avoid bold, italics, and underlines unless essential for meaning.
- Decorative emphasis is not permitted.

**Section separation**:

- Separate sections with two blank lines (`\n\n`).
- Never use `---` (horizontal rules) to separate sections.

**Figures**:

- Optional; ASCII diagrams if needed.
 Example:

```
 Core
(  o  )
 \   /
  \_/
```

## Example Section

Theory
Let $U:\mathbb{R}^3\times\mathbb{R} \to \mathbb{R}$ be the scalar energy field.
The field strength is defined:
$$
F = d(*dU)
$$
Source-free dynamics satisfy:
$$
dF = 0, \quad d\!\star F = 0
$$
Energy density and Poynting vector:
$$
u = \frac{\varepsilon_0}{2}(E^2 + c^2 B^2), \quad \mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B}
$$

Results
For TE$_{11}$ mode geometry:
$$
\alpha = \frac{\kappa}{2\pi^2 R} \cdot \frac{e^2}{\varepsilon_0}
$$
Numerical value: $\alpha \approx 6.41\,\mathrm{eV}$.

## Conclusion

PNPMD v1.001 is a plain-text specification for mathematically aware documents.

## Next Work

A PNPMD v2 could extend this with optional metadata fields for ORCID, funding, and cross-references between related preprints.

## Corresponding author(s)

An Rodriguez: an@preferredframe.com

## References

1. Palma, A., Rodríguez, A. M., & Freet, M. (2025). Point–Not–Point: Deriving Maxwell Electrodynamics from a Scalar Energy Field and Explaining Particle–Wave Duality. DOI:[10.13140/RG.2.2.16877.91368](https://doi.org/10.13140/RG.2.2.16877.91368)
