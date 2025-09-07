# Usage: run from anywhere inside the repo; renders the first *.md (depth ≤ 2).
render-pdf() {
  # 1) Resolve repo root (fallback: CWD)
  root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
  mapfile="$root/pnpmd.map"

  # 2) Pick first candidate Markdown (depth ≤ 2); skip dotfiles and name.*.md
  file="$(find . -maxdepth 2 -type f -name '*.md' \
           ! -name '.*' \
           ! -regex '.*\.[A-Za-z0-9_-]+\.md' \
           | head -n1)" || return 1
  [ -z "$file" ] && { echo "No candidate .md found (depth ≤ 2)."; return 1; }

  # Paths relative to repo root for container I/O
  rel="$(python3 - <<PY
import os; print(os.path.relpath("$file","$root"))
PY
)"; rel="${rel#./}"
  out_rel="${rel%.md}.pdf"
  pnp_rel="${rel%.md}.pnp.md"   # <-- interim file path (relative to repo root)

  # 3) Build sed script from pnpmd.map
  #    - /regex/=replacement → regex rule
  #    - literalLHS=RHS      → literal rule (LHS escaped)
  #    - if RHS starts with "\" (TeX macro), wrap as $RHS$ (math mode)
  tmp="$root/.pnpmd.sed"; : > "$tmp"
  if [ -f "$mapfile" ]; then
    echo "Using map: $mapfile"
    while IFS= read -r line || [ -n "$line" ]; do
      case "$line" in ''|\#*) continue ;; esac
      lhs="${line%%=*}"; rhs="${line#*=}"
      lhs="$(printf '%s' "$lhs" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
      rhs="$(printf '%s' "$rhs" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"

      esc_rhs="$(printf '%s' "$rhs" | sed 's/[\/&\\]/\\&/g')"
      if printf '%s' "$rhs" | grep -q '^[\\]'; then
        rep="\\\$$esc_rhs\\\$"   # wrap TeX macro in $...$
      else
        rep="$esc_rhs"
      fi

      if [ "${lhs#\/}" != "$lhs" ] && [ "${lhs%\/}" = "${lhs#\/}" ]; then
        pat="${lhs#\/}"; pat="${pat%\/}"
        printf 's/%s/%s/g\n' "$pat" "$rep" >> "$tmp"
      else
        esc_lhs="$(printf '%s' "$lhs" | sed 's/[][\/.^$*]/\\&/g')"
        printf 's/%s/%s/g\n' "$esc_lhs" "$rep" >> "$tmp"
      fi
    done < "$mapfile"
  else
    echo "No pnpmd.map at $mapfile; rendering raw input."
  fi

  # 4) Produce the interim .pnp.md (CRLF→LF + mappings), then render that file
  mkdir -p "$(dirname "$root/$pnp_rel")" 2>/dev/null || true

  if [ -s "$tmp" ]; then
    # write the normalized/mapped stream to pnp.md
    sed 's/\r$//' "$file" | sed -E -f "$tmp" > "$root/$pnp_rel" || {
      echo "❌ Failed to write $pnp_rel"; rm -f "$tmp"; return 1; }
  else
    # even without a map, normalize CRLF and still write pnp.md
    sed 's/\r$//' "$file" > "$root/$pnp_rel" || {
      echo "❌ Failed to write $pnp_rel"; return 1; }
  fi
  rm -f "$tmp"

  # render from the interim file (stable, debuggable)
  if ! docker run --rm -i -v "$root:/data" -w /data pandoc/latex \
        --toc --toc-depth=2 --number-sections --reference-links \
        --citeproc -M link-citations=true -F pandoc-crossref --standalone \
        --shift-heading-level-by=-1 "/data/$pnp_rel" -o "/data/$out_rel"; then
    echo "❌ Pandoc build failed."
    return 1
  fi

  echo "✅ Wrote $out_rel  (source: $pnp_rel)"
}
