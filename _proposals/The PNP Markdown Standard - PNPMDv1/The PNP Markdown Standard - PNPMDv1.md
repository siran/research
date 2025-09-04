% The PNP Markdown Standard – PNPMD v1.02
% Max Freet, An M. Rodríguez, Adrien Hale
% August 21, 2025

## Abstract

We define the PNP Plain Text Standard PNPMD v1.02 specification.

It is a human-readable *first*, plain-text document format, mathematically aware (using `$...$` and `$$...$$` LaTeX equation blocks) and based on Markdown standards.

The format eases compatibility with naive use of `pandoc`, the default renderer, which converts `.md` to `.pdf`, `.html`, or enhanced `.md` with numbering, links, and TOC.

## One-Sentence Summary

PNPMD v1.02 is a minimal, human-readable *first*, mathematically aware, plain-text Markdown standard for documents.

## Keywords

plain-text, research format, markdown, mathjax, html, PNPMD

PNPMD v1.02 provides a minimal yet complete Markdown structure for mathematically aware documents.
It keeps the format simple and human-readable *first*: a straight ASCII-text document.
It avoids noisy LaTeX wrappers and PDF-only workflows.
Goals: reproducibility, portability, unambiguous interpretation.

In summary:

- human-readable *first*
- clear, simple, LaTeX, math-aware text
- ASCII art
- even tikki figures

## Structure

- Header
- Abstract
- One-Sentence Summary
- Keywords
- Other body sections
- Corresponding Author
- References

**Header:**
```

% Title
% Author(s)
% Date

```

**Abstract:** 3–5 sentences: problem → method → result → significance. No citations or equations.

**One-Sentence Summary:** one sentence summarizing the paper.

**Keywords:** 3–6 topical keywords.

**Other body sections (recommended):** Introduction, Theory/Framework, Derivation, Results, Discussion, Conclusion, Next Work, Appendices.

**Corresponding Author:** immediately before References.

**References:**
- Use DOI links where possible.
- Avoid footnote-style citations; inline references via `@refname` are encouraged.

## Naive Pandoc Support (extension from v1.001)

PNPMD uses Pandoc as the default renderer. PDFs, HTML, and enhanced Markdown (with TOC, numbering, links) are **by-products**. The plain-text manuscript remains human-first.

### Plain Anchor Convention

- **Author shorthand:** anchors may be written naturally in PNPMD:
```

## A Long Section #short

## A Long Section

\#short

## A Long Section (#short)

## A Long Section \[#short]

```
Figures:
```

!\[diagram.png]
*This is the setup* #fig\:setup

```

- **Formatter pipeline:** all shorthand anchors are rewritten in `pandoc.md` into Pandoc-compatible IDs with a `pnpref:` namespace:
```

## A Long Section {#pnpref\:short}

![This is the setup](diagram.png){#pnpref\:fig\:setup}

```

- **References:**
- `@short` → `@pnpref:short`
- `@fig:setup` → `@pnpref:fig:setup`
- With `pandoc-crossref`, these render as numbered links:
  - sections: “see § 2.3”
  - figures: “see Figure 1”
  - equations: `@eq:…` → “(3)”

- **Summary:** PNPMD authors only ever write `#hash` and `@hash`. The formatter expands them into `{#pnpref:hash}` and `@pnpref:hash` so Pandoc-crossref resolves numbering and linking.

### Citations

- Syntax: `@key` or `[@key, pp. 33–35]`.
- A `.bib` file is generated from the `## (Suggested) References` section.
- Pandoc options: `--citeproc --bibliography=generated.bib -M link-citations=true`.
- Result: in-text citations hyperlinked to bibliography entries.

### TOC and numbering

- `--toc --toc-depth=2`: auto two-level TOC if none written.
- `--number-sections`: section numbering.
- Equation/figure/section numbering from cross-references requires `pandoc-crossref`.

### Reference-style links

- `--reference-links` rewrites `[text](url)` into `[text][1]` with link definitions (Markdown targets only).
- Purely cosmetic; no effect on citations or anchors.

## Formatting Rules

**Math:**
- Inline: `$...$`
- Display: `$$...$$`
- No `\[...\]` or `\(...\)`
- Always specify units

**Characters:**
- UTF-8 required
- Greek/math symbols only if supported by pdfLaTeX utf8
- Otherwise use `$...$` or ASCII

**Emphasis:** avoid unless essential.

**Sections:** separate with blank lines. No `---`.

**Figures:** ASCII diagrams allowed. Example:
```

Core
(  o  )
\   /
\_/

```

## Example Section

Theory
Let $U:\mathbb{R}^3\times\mathbb{R} \to \mathbb{R}$ be the scalar energy field.
$$ F = d(*dU) $$
Source-free dynamics:
$$ dF = 0, \quad d\!\star F = 0 $$

Results
For TE$_{11}$ mode geometry:
$$
\alpha = \frac{\kappa}{2\pi^2 R} \cdot \frac{e^2}{\varepsilon_0}
$$
Numerical value: $\alpha \approx 6.41\,\mathrm{eV}$.

## Conclusion

PNPMD v1.02 is a plain-text specification for mathematically aware documents.

## Next Work

A PNPMD v2 could extend this with optional metadata for ORCID, funding, and cross-links between related preprints.

## Corresponding author(s)

An Rodriguez: an@preferredframe.com

## References

1. Palma, A., Rodríguez, A. M., & Freet, M. (2025). Point–Not–Point: Deriving Maxwell Electrodynamics from a Scalar Energy Field and Explaining Particle–Wave Duality. DOI:[10.13140/RG.2.2.16877.91368](https://doi.org/10.13140/RG.2.2.16877.91368)

---

## Changes from v1.001 → v1.02

- Added **Naive Pandoc Support** section.
- Defined **Plain Anchor Convention**: `#hash` shorthand in PNPMD → `{#pnpref:hash}` in `pandoc.md`.
- Clarified support for `#fig:…`, `#eq:…`, `#tbl:…`.
- Explicitly noted that `pandoc-crossref` resolves `@id` references to numbered links.
- `.bib` is auto-generated from `## (Suggested) References`.
- Added notes on TOC, section numbering, and cosmetic reference links.
- Strengthened inline citation rule: “Avoid footnote-style citations; inline `@refname` encouraged.”
