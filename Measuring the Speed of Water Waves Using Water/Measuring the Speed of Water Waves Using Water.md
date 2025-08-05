# Measuring the Speed of Water Waves Using Water: Why Only Differences in the Speed of Light Are Observable in a Maxwell Universe  

An M. Rodriguez (an@preferredframe.com), Anes Palma
31 July 2025

## Abstract
Observers composed entirely of electromagnetic (EM) fields cannot determine the absolute speed of light $c$. Clocks count field cycles and rulers register field nodes; both rescale with any local change in the vacuum parameters $\varepsilon(x)$ and $\mu(x)$. Every laboratory therefore self-calibrates to the value $c_0 = 1/\sqrt{\mu_0\,\varepsilon_0}$ even if the underlying light speed $c(x)$ varies from place to place. Using elementary Maxwell theory and a water-wave analogy, we show why present-day cavity experiments can constrain only differences $\Delta c/c$, not the absolute magnitude of $c$.

### One-sentence summary
Because laboratory rulers and clocks are built from electromagnetic fields, Maxwell theory allows detection of only spatial or temporal *variations* in the speed of light—never its absolute value.

### Keywords
Maxwell electrodynamics; metrology; speed of light; Lorentz invariance; Fabry–Pérot cavity.

## Introduction
Michelson–Morley-type experiments and modern optical cavities show no sign of a preferred frame. While special relativity explains this by postulating a universal $c$, classical Maxwell theory offers a simpler reading: when measuring tools are built from the very field whose speed is sought, only differences in that speed can ever be observed.

## Operational Definition of $c$ in Maxwell Theory
In vacuum the fields satisfy  
$$
\nabla^{2}\mathbf{E} = \mu_0 \varepsilon_0 \,\partial_t^{2}\mathbf{E},
$$  
which fixes the characteristic speed  
$$
c_0 = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} .
$$  

A Fabry–Pérot cavity of fixed length $L$ enforces $n\lambda_n = 2L$. For the fundamental mode ($n = 1$) the wavelength is $\lambda_1 = 2L$. Using $c = \lambda/T$, the same mode provides the period $T_1 = \lambda_1/c$. If the local vacuum parameters shift to new values $(\mu,\varepsilon)$, both $\lambda_1$ and $T_1$ are multiplied by the same factor $\sqrt{\mu\varepsilon}$; their ratio $\lambda_1/T_1$ is unchanged, so any measurement of $c$ still returns $c_0$.

## Blindness of EM-Based Metrology

### Water-Wave Analogy
A fish tries to measure the speed $v$ of surface waves. Its rulers (successive crests) and clocks (periods between crests) both stretch if the surface tension varies. Absolute speed is invisible; only relative differences appear. EM observers face the same limitation.

### Interferometer logic
Most laboratory searches for anisotropy compare two orthogonal high-$Q$ Fabry–Pérot cavities on a slowly rotating stage. For the $m$-th longitudinal mode in arm $i$  
$$
\nu_i \;=\; \frac{m\,c(x_i)}{2L_i},\qquad i = x,y ,
$$  
so a directional dependence of $c(x)$ would modulate the beat note $\nu_x-\nu_y$ once per turn.  Experiments find no such modulation down to $|\Delta c|/c \le 10^{-18}$.  In our framework the setup samples the vacuum scaling factor *differentially*: it measures $c(x)$ **relative to** $f(p_x)$ versus $f(p_y)$ (see next section for $f(p)$).  If $f$ were uniform the two arms would differ only by construction tolerances, and constant-velocity motion would be completely invisible—precisely the conclusion of special relativity.  Orthogonal cavities are therefore sensitive only to a gradient $f(p_x) - f(p_y)$; a uniform offset cancels.

Detecting an *absolute* shift in $f(p)$ instead requires a one-arm, time-of-flight technique—e.g. sending a light pulse through a long fiber or free-space delay line and comparing the round-trip time against an independent clock.  Such single-path measurements would respond directly to the optical length  
$$
\mathcal{L}(x) = \int n_{\text{eff}}(x)\, \mathrm dx \;=\; \int f(p)\,\mathrm dx,
$$  
and could, in principle, reveal a uniform change in $f(p)$ rather than just a transverse gradient.

## Formal Derivation with Variable Vacuum Parameters
Let a scalar background $p(x)$—a proxy for local energy density—multiply both permittivity and permeability by the same positive factor $f(p)$:
$$
\varepsilon(x) = \varepsilon_0 f(p), \qquad
\mu(x)        = \mu_0 f(p).
$$  
The local wave speed is  
$$
c(x) = \frac{1}{\sqrt{\mu(x)\varepsilon(x)}} = \frac{c_0}{f(p)} .
$$  

### Constructing a ruler  
The cavity’s fundamental frequency becomes  
$$
\nu_{\text{ref}}(x) = \frac{c(x)}{2L} = \frac{c_0}{2L\,f(p)} .
$$  
The associated wavelength is  
$$
\lambda_{\text{ref}}(x) = \frac{c(x)}{\nu_{\text{ref}}(x)} = 2L ,
$$  
independent of $p(x)$. A rod made from $N$ such wavelengths has length  
$$
L_{\text{rod}} = N\lambda_{\text{ref}} = 2NL ,
$$  
also independent of $p(x)$.

### Constructing a clock  
The period of one oscillation is  
$$
T_{\text{ref}}(x) = \frac{1}{\nu_{\text{ref}}(x)} = \frac{2L\,f(p)}{c_0}.
$$  
Combining ruler and clock gives  
$$
\frac{L_{\text{rod}}}{T_{\text{ref}}(x)} = c_0 ,
$$  
showing that absolute variations in $c(x)$ remain hidden; only gradients in $f(p)$ could, in principle, be detected.

## Relation to General Relativity
General relativity expresses the same idea geometrically. A perturbed metric  
$$
g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}(p)
$$  
gives local null cones identical to those of special relativity, while global geodesics reproduce light-bending through an effective refractive index  
$$
n_{\text{eff}}(\mathbf{x}) \simeq 1 + \frac{2\Phi(\mathbf{x})}{c_0^{2}} .
$$  
The optical-metric formalism is therefore algebraically equivalent to Maxwell with variable $(\varepsilon,\mu)$.

## Conclusion
Maxwell electrodynamics implies that laboratories built from EM fields cannot measure the absolute speed of light. Their rulers and clocks scale together with any local change in $\varepsilon$ and $\mu$, leaving only spatial or temporal differences observable. The water-wave analogy captures the point: one cannot determine the speed of water waves using only water.

## Note from A. M. Rodriguez
The geometrical argument linking Maxwell theory to general relativity was developed entirely by Anes Palma.

## Suggested References
1. A. M. Rodriguez and A. Palma, *Hydrogen Atom Quantization from Purely Classical Maxwell Electromagnetic Fields*, Research Gate DOI 10.13140/RG.2.2.36143.04005 (2025)
2. A. Palma and A. M. Rodriguez, *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*, Research Gate DOI 10.13140/RG.2.2.19900.76167 (2025)
3. A. Palma and A. M. Rodriguez, *Emergent $-1/L^2$ Interaction Force in a Pure Maxwell Universe from Constant-Energy and Wave-Like Interactions*, Research Gate DOI 10.13140/RG.2.2.16128.14085 (2025)
4. R. Te Winkel and A. M. Rodriguez, *Daily Variations of the Amplitude of the Fringe Shifts Observed When an Air-Glass Mach–Zehnder Type Interferometer Is Rotated*, Research Gate DOI 10.13140/RG.2.2.16800.90886 (2024)
5. D. Mattingly, *Modern Tests of Lorentz Invariance*, Living Reviews in Relativity 8 (2005) 5
6. H. Müller et al., *Modern Michelson–Morley Experiment Using Cryogenic Optical Resonators*, Physical Review Letters 91 (2003) 020401
7. M. E. Tobar and P. Wolf, *Gravitational Wave Detection Using Electromagnetic Cavities*, Physical Review D 66 (2002) 024017
8. R. M. Wald, *General Relativity*, University of Chicago Press (1984)
9. J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley (1999)

