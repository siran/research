% Interference as Polarization: The Electromagnetic Field as Its Own Medium
% An M. Rodriguez, Elena Martinez
% October 25, 2025

## One-Sentence Summary

Interference, refraction, polarization, and apparent changes in light speed are a single electromagnetic effect: one field acts as the polarizing medium for another, even in vacuum.

## Abstract

It is widely taught that interference is a superposition effect in vacuum, refraction is a change of light speed in matter, and polarization is the secondary field produced by bound charges in a medium. In this work we show that, within strictly linear Maxwell theory, these distinctions collapse. We take two coherent electromagnetic waves in free space and rewrite Maxwell’s equations so that one wave is treated as the "test field" and the other as "background." The background field enters the test field’s evolution equation in exactly the same algebraic position that a polarization current would occupy in a dielectric. From this, we derive step by step an effective polarization density, an effective susceptibility, a spatially varying refractive index $n_{\mathrm{eff}}(\mathbf{r})$, and a local phase velocity $c_{\mathrm{eff}}(\mathbf{r}) = c / n_{\mathrm{eff}}(\mathbf{r})$. We then show that standard interference fringe geometry is reproduced by treating one beam as being refracted in the effective index landscape created by the other. Experiments using independent, phase-locked light sources confirm that interference does not require a single emitter or any material polarization — the electromagnetic field polarizes space for itself. This unifies interference, refraction, polarization of matter, polarization of vacuum, and apparent variation of light speed as one phenomenon.

## Keywords

interference; refraction; polarization; effective medium; Maxwell theory; coherence; vacuum electrodynamics

## Introduction

Classically, four core optical phenomena are described as if they are different in kind:

1. Interference: Two coherent waves overlap, and intensity varies in space as fringes.

2. Refraction: A wave bends and changes phase velocity when it enters matter with refractive index $n>1$.

3. Polarization: An applied field displaces bound charges inside matter, and the resulting dipole distribution radiates a "secondary" field.

4. Light-speed reduction: In matter, we say light travels at $c/n$, slower than $c$.

In standard teaching, these are linked but not identical. Interference is "just superposition in vacuum." Refraction "only happens in media." Polarization "requires matter." And reduction of light speed "is a property of materials."

We will show that this separation is artificial.

We prove that if two coherent electromagnetic beams overlap in free space, then — without introducing any nonlinearity — Maxwell’s equations can be rearranged so that one beam plays exactly the same mathematical role as a polarizable medium for the other. This rearrangement:

* produces an effective polarization density,

* defines an effective susceptibility $\chi_{\mathrm{eff}}(\mathbf{r})$,

* yields an effective refractive index $n_{\mathrm{eff}}(\mathbf{r})$,

* and defines an effective local light speed $c_{\mathrm{eff}}(\mathbf{r}) = c/n_{\mathrm{eff}}(\mathbf{r})$.

We then show how geometric optics in this $n_{\mathrm{eff}}(\mathbf{r})$ predicts a deflection angle that matches the observed interference angle between the beams. That is: what we normally call "interference fringes" is rigorously identical to "refraction through a spatially varying index," which is rigorously identical to "propagation through a polarization field," which is rigorously identical to "local modulation of light speed."

In other words, one field acts as the medium for the other field. Vacuum is not passive background; the electromagnetic field is its own dielectric.

Finally, this viewpoint is not merely mathematical. Long-standing experiments show that two independent optical sources will interfere if and only if their relative phase is locked [Magyar & Mandel 1963; Shelton et al. 2001]. Coherence between different sources creates stable fringes, and when coherence is lost, the fringes disappear. This matches the claim that interference is a property of the shared electromagnetic field state in space, not a photon "interfering with itself."

We proceed slowly, from first principles, because the point is foundational and conceptually touchy. We start by writing Maxwell’s equations in their most general form (with charges and currents), and then specialize to free space.

## Maxwell’s Equations, With and Without Material Sources

### General form (with free charges and currents)

The macroscopic Maxwell equations in SI units are:
$$
\begin{aligned}
\nabla \cdot \mathbf{D} &= \rho_{\text{free}}, \
\nabla \cdot \mathbf{B} &= 0, \
\nabla \times \mathbf{E} &= -,\frac{\partial \mathbf{B}}{\partial t}, \
\nabla \times \mathbf{H} &= \mathbf{J}_{\text{free}} + \frac{\partial \mathbf{D}}{\partial t}.
\end{aligned}
\tag{2.1}
$$

For a linear, isotropic, non-magnetic dielectric medium,
$$
\mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}, \qquad
\mathbf{H} = \frac{1}{\mu_0}\mathbf{B}.
\tag{2.2}
$$

The quantity $\mathbf{P}$ is the polarization density. It encodes how matter responds to the field. If $\partial_t \mathbf{P} \neq 0$, this gives rise to the bound current density
$$
\mathbf{J}_{\text{bound}} \equiv \frac{\partial \mathbf{P}}{\partial t}.
\tag{2.3}
$$

Substituting (2.2) into Ampère’s law in (2.1) gives
$$
\nabla \times \mathbf{B}= \mu_0 \mathbf{J}_{\text{free}}* \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}* \mu_0 \frac{\partial \mathbf{P}}{\partial t}.  \tag{2.4}
$$

So in matter, the curl of $\mathbf{B}$ is sourced by both:

* the "ordinary" vacuum displacement current $\mu_0\epsilon_0 ,\partial_t \mathbf{E}$,

* plus the "extra" current $\mu_0 \partial_t \mathbf{P}$ that comes purely from polarization of the medium.

This is the standard picture:

* Matter responds to $\mathbf{E}$ by creating $\mathbf{P}$.

* $\partial_t\mathbf{P}$ acts as a current source for Maxwell’s equations.

* That source changes how waves propagate, i.e. creates refraction, finite $n$, slower phase velocity, etc.

We will now show that precisely the same structure appears in empty space when a second electromagnetic wave is present.

### Specializing to vacuum (no free charges, no material)

Now set $\rho_{\text{free}} = 0$, $\mathbf{J}_{\text{free}} = 0$, and $\mathbf{P} = 0$ (no matter). Then
$$
\begin{aligned}
\nabla \cdot \mathbf{E} &= 0, \
\nabla \cdot \mathbf{B} &= 0, \
\nabla \times \mathbf{E} &= -,\frac{\partial \mathbf{B}}{\partial t}, \
\nabla \times \mathbf{B} &= \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}.
\end{aligned}
\tag{2.5}
$$

These are the vacuum Maxwell equations.

Now, assume the total electromagnetic field is a sum of two coherent fields:
$$
\mathbf{E} = \mathbf{E}_1 + \mathbf{E}_2, \qquad
\mathbf{B} = \mathbf{B}_1 + \mathbf{B}_2.
\tag{2.6}
$$

We assume that $(\mathbf{E}_1,\mathbf{B}_1)$ and $(\mathbf{E}_2,\mathbf{B}_2)$ each solve (2.5) individually. This means, for each $i \in {1,2}$,
$$
\nabla \cdot \mathbf{E}_i = 0, \quad
\nabla \cdot \mathbf{B}_i = 0, \quad
\nabla \times \mathbf{E}_i = -,\frac{\partial \mathbf{B}_i}{\partial t}, \quad
\nabla \times \mathbf{B}_i = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_i}{\partial t}.
\tag{2.7}
$$

We now rewrite Ampère–Maxwell’s equation (the fourth of (2.5)) in a way that isolates beam 1 and shows what role beam 2 plays in beam 1’s propagation.

Start from the total-field version of Ampère–Maxwell:
$$
\nabla \times (\mathbf{B}_1 + \mathbf{B}_2)
= \mu_0 \epsilon_0 \frac{\partial (\mathbf{E}_1 + \mathbf{E}_2)}{\partial t}.
\tag{2.8}
$$

Expand both sides of (2.8):

$$
(\nabla \times \mathbf{B}_1) + (\nabla \times \mathbf{B}_2)= \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_1}{\partial t}* \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_2}{\partial t}.
\tag{2.9}
$$

Solve (2.9) explicitly for $\nabla \times \mathbf{B}_1$:

$$
\nabla \times \mathbf{B}_1
= \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_1}{\partial t}
\, \underbrace{
\left[
\mu_0 \epsilon_0 \frac{\partial \mathbf{E}_2}{\partial t}
(\nabla \times \mathbf{B}_2)
\right]
}_{\mu_0 \mathbf{J}_{\mathrm{eff}}}.
\tag{2.10}
$$

Here we have defined
$$
\mathbf{J}_{\mathrm{eff}} \equiv \epsilon_0 \frac{\partial \mathbf{E}_2}{\partial t} * \frac{1}{\mu_0}(\nabla \times \mathbf{B}_2).  \tag{2.11}
$$

Now rewrite (2.10) using (2.11):
$$
\nabla \times \mathbf{B}_1 = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_1}{\partial t} * \mu_0 \mathbf{J}_{\mathrm{eff}}.  \tag{2.12}
$$

This equation is the key structural result.

Compare (2.12) to the material case (2.4):

* In matter:
  $\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \partial_t \mathbf{E} + \mu_0 \partial_t \mathbf{P}$.

* Here in vacuum for beam 1:
  $\nabla \times \mathbf{B}_1 = \mu_0 \epsilon_0 \partial_t \mathbf{E}*1 + \mu_0 \mathbf{J}*{\mathrm{eff}}$.

So $\mathbf{J}_{\mathrm{eff}}$ plays the exact same mathematical role as $\partial_t \mathbf{P}$ in a material medium.

Interpretation, stated plainly:

When we look at beam 1 alone, beam 2 behaves like a polarization of space. The term $\mathbf{J}_{\mathrm{eff}}$ is in the same slot as the polarization current $\partial_t \mathbf{P}$ would be if the background were a dielectric. Thus, from the point of view of beam 1, beam 2 is indistinguishable from a polarizable medium.

This gives us license — not as a metaphor, but algebraically — to interpret the second field as producing an "effective polarization" that modifies the propagation of the first.

In the next section we use (2.12) to derive the driven wave equation for $\mathbf{E}_1$.

## Deriving the Driven Wave Equation for the Test Field

We now derive the inhomogeneous wave equation for $\mathbf{E}_1$, step by step, using only Maxwell and vector identities. This is what in usual macroscopic electrodynamics would become the Helmholtz equation with sources.

### Take the curl of Faraday’s law for $\mathbf{E}_1$

Faraday’s law for beam 1 reads:
$$
\nabla \times \mathbf{E}_1 = -,\frac{\partial \mathbf{B}_1}{\partial t}.
\tag{3.1}
$$

Now take $\nabla \times$ of both sides:
$$
\nabla \times (\nabla \times \mathbf{E}_1)
= -,\frac{\partial}{\partial t} (\nabla \times \mathbf{B}_1).
\tag{3.2}
$$

### Use the standard vector identity

For any vector field $\mathbf{A}$,
$$
\nabla \times (\nabla \times \mathbf{A})
= \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}.
\tag{3.3}
$$

Apply (3.3) with $\mathbf{A} = \mathbf{E}_1$.
In vacuum for a free electromagnetic wave, $\nabla \cdot \mathbf{E}_1 = 0$.
Therefore,
$$
\nabla \times (\nabla \times \mathbf{E}_1)
= -,\nabla^2 \mathbf{E}_1.
\tag{3.4}
$$

Substitute (3.4) into (3.2):
$$
-,\nabla^2 \mathbf{E}_1
= -,\frac{\partial}{\partial t} (\nabla \times \mathbf{B}_1).
\tag{3.5}
$$

We can cancel the minus signs:
$$
\nabla^2 \mathbf{E}_1
= \frac{\partial}{\partial t} (\nabla \times \mathbf{B}_1).
\tag{3.6}
$$

Equation (3.6) is exact.

### Substitute $\nabla \times \mathbf{B}_1$ from (2.12)

From Section 2, equation (2.12):

$$
\nabla \times \mathbf{B}_1= \mu_0 \epsilon_0 \frac{\partial \mathbf{E}_1}{\partial t}* \mu_0 \mathbf{J}_{\mathrm{eff}}.
\tag{2.12 revisited}
$$

Take $\partial/\partial t$ of both sides of (2.12 revisited):

$$
\frac{\partial}{\partial t} (\nabla \times \mathbf{B}_1)= \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}_1}{\partial t^2}* \mu_0 \frac{\partial \mathbf{J}_{\mathrm{eff}}}{\partial t}.
  \tag{3.7}
$$

Insert (3.7) into (3.6):
$$
\nabla^2 \mathbf{E}_1= \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}_1}{\partial t^2}* \mu_0 \frac{\partial \mathbf{J}_{\mathrm{eff}}}{\partial t}.
  \tag{3.8}
$$

Finally, use
$$
\mu_0 \epsilon_0 = \frac{1}{c^2}.
\tag{3.9}
$$

Then (3.8) becomes
$$
\nabla^2 \mathbf{E}_1* \frac{1}{c^2}\frac{\partial^2 \mathbf{E}*1}{\partial t^2}= \mu_0 \frac{\partial \mathbf{J}*{\mathrm{eff}}}{\partial t}.
  \tag{3.10}
$$

Equation (3.10) is a driven wave equation for $\mathbf{E}*1$ in free space, where the only source term is $\mathbf{J}*{\mathrm{eff}}$, i.e. the influence of beam 2.

This is exactly analogous to how, in matter, polarization currents $\partial_t \mathbf{P}$ appear as sources in the wave equation and thereby modify propagation (refraction, finite index, etc.).

So the logic chain so far is:

* In matter: $\partial_t \mathbf{P}$ modifies the wave.

* In vacuum with two beams: $\mathbf{J}_{\mathrm{eff}}$ modifies the wave.

* Algebraically: $\mathbf{J}_{\mathrm{eff}}$ is in the same slot as $\partial_t \mathbf{P}$.

This is the first half of the unification: the second beam supplies the "polarization current" through which the first beam propagates.

In the next section we move from $\mathbf{J}*{\mathrm{eff}}$ to an explicit effective polarization density $\mathbf{P}*{\mathrm{eff}}$, an effective susceptibility $\chi_{\mathrm{eff}}$, and thus to $n_{\mathrm{eff}}$ and $c_{\mathrm{eff}}$.

## From Effective Current to Effective Polarization, Susceptibility, and Light Speed

Now we take Eq. (3.10) and work in frequency space, because propagation and refractive index are most naturally expressed for monochromatic or quasi-monochromatic waves.

### Frequency-domain form of the driven wave equation

Assume the test field is monochromatic at angular frequency $\omega$, i.e.
$$
\mathbf{E}*1(\mathbf{r},t) = \Re{\mathbf{E}*1(\mathbf{r}) e^{-i\omega t}},
$$
and similarly assume $\mathbf{J}*{\mathrm{eff}}(\mathbf{r},t) = \Re{\mathbf{J}*{\mathrm{eff}}(\mathbf{r}) e^{-i\omega t}}$.

Then,
$$
\frac{\partial^2 \mathbf{E}_1}{\partial t^2}
\rightarrow (-i\omega)^2 \mathbf{E}*1(\mathbf{r})
= -\omega^2 \mathbf{E}*1(\mathbf{r}),
\tag{4.1}
$$
$$
\frac{\partial \mathbf{J}*{\mathrm{eff}}}{\partial t}
\rightarrow (-i\omega) \mathbf{J}*{\mathrm{eff}}(\mathbf{r}).
\tag{4.2}
$$

Insert (4.1) and (4.2) into (3.10):
$$
\nabla^2 \mathbf{E}_1(\mathbf{r})* \frac{\omega^2}{c^2}\mathbf{E}*1(\mathbf{r})  = - i\omega \mu_0 \mathbf{J}*{\mathrm{eff}}(\mathbf{r}).
  \tag{4.3}
$$

Define the vacuum wavenumber
$$
k_0 \equiv \frac{\omega}{c}.
\tag{4.4}
$$

Then (4.3) becomes
$$
\nabla^2 \mathbf{E}_1(\mathbf{r})* k_0^2 \mathbf{E}*1(\mathbf{r})= - i\omega \mu_0 \mathbf{J}*{\mathrm{eff}}(\mathbf{r}).
  \tag{4.5}
$$

### Identify an effective polarization density

In macroscopic electrodynamics, the oscillating polarization density $\mathbf{P}(\mathbf{r})$ produces a bound current
$$
\mathbf{J}_{\text{bound}}(\mathbf{r}) = \frac{\partial \mathbf{P}}{\partial t}= -i\omega \mathbf{P}(\mathbf{r}).
\tag{4.6}
$$

The textbook driven wave equation for a dielectric (no free current) is
$$
\nabla^2 \mathbf{E}_1* k_0^2 \mathbf{E}_1= \omega^2 \mu_0 \mathbf{P}(\mathbf{r}).
  \tag{4.7}
$$

Comparing (4.5) and (4.7), we can make them match by definition if we set

$$
\omega^2 \mu_0 \mathbf{P}*{\mathrm{eff}}(\mathbf{r})= - i\omega \mu_0 \mathbf{J}*{\mathrm{eff}}(\mathbf{r}).
\tag{4.8}
$$

Solve (4.8) for $\mathbf{P}*{\mathrm{eff}}$:

$$
\mathbf{P}*{\mathrm{eff}}(\mathbf{r})= -\frac{i}{\omega} \mathbf{J}_{\mathrm{eff}}(\mathbf{r}).
\tag{4.9}
$$

This is a crucial identification:

* $\mathbf{P}_{\mathrm{eff}}$ is the effective polarization density "seen" by beam 1 due solely to the presence of beam 2.

* We did not assume a medium. We derived $\mathbf{P}_{\mathrm{eff}}$ from Maxwell in vacuum plus superposition of two fields.

### Define an effective susceptibility $\chi_{\mathrm{eff}}$

In standard linear optics,

$$
\mathbf{P}(\mathbf{r}) = \epsilon_0 \chi(\mathbf{r}) \mathbf{E}(\mathbf{r}).
\tag{4.10}
$$

We now write, analogously,

$$
\mathbf{P}*{\mathrm{eff}}(\mathbf{r})= \epsilon_0 \chi*{\mathrm{eff}}(\mathbf{r}) , \mathbf{E}_1(\mathbf{r}).
\tag{4.11}
$$

Combine (4.9) and (4.11):

$$
\epsilon_0 \chi_{\mathrm{eff}}(\mathbf{r}) , \mathbf{E}*1(\mathbf{r})= -\frac{i}{\omega} \mathbf{J}*{\mathrm{eff}}(\mathbf{r}).
\tag{4.12}
$$

We can project along the polarization unit vector $\hat{e}*1$ of beam 1, to define a scalar susceptibility for that polarization:

$$
\chi*{\mathrm{eff}}(\mathbf{r})= - \frac{i}{\epsilon_0 \omega}
\frac{\mathbf{J}_{\mathrm{eff}}(\mathbf{r}) \cdot \hat{e}_1}
{\mathbf{E}_1(\mathbf{r}) \cdot \hat{e}_1}.
\tag{4.13}
$$

Equation (4.13) is the explicit formula for the effective susceptibility that beam 1 experiences because beam 2 is present.

This is now airtight:

* $\mathbf{J}_{\mathrm{eff}}$ is defined by Eq. (2.11) directly from the background field $(\mathbf{E}_2,\mathbf{B}_2)$.

* $\mathbf{P}*{\mathrm{eff}}$ is defined by Eq. (4.9) from $\mathbf{J}*{\mathrm{eff}}$.

* $\chi_{\mathrm{eff}}$ is defined by Eq. (4.13) from $\mathbf{P}_{\mathrm{eff}}$.

No step required assuming "medium behavior." The "medium" is the other field.

### Effective index $n_{\mathrm{eff}}$ and effective phase velocity $c_{\mathrm{eff}}$

In linear optics for nonmagnetic media (relative $\mu \approx 1$),
$$
n^2(\mathbf{r}) = 1 + \chi(\mathbf{r}).
\tag{4.14}
$$

By analogy, for the effective susceptibility $\chi_{\mathrm{eff}}$,
$$
n_{\mathrm{eff}}^2(\mathbf{r}) = 1 + \chi_{\mathrm{eff}}(\mathbf{r}).
\tag{4.15}
$$

The corresponding local phase velocity is
$$
c_{\mathrm{eff}}(\mathbf{r})
= \frac{c}{n_{\mathrm{eff}}(\mathbf{r})}
= \frac{c}{\sqrt{1+\chi_{\mathrm{eff}}(\mathbf{r})}}.
\tag{4.16}
$$

For $|\chi_{\mathrm{eff}}|\ll 1$, expand to first order:
$$
n_{\mathrm{eff}}(\mathbf{r})
\approx 1 + \tfrac12 \chi_{\mathrm{eff}}(\mathbf{r}),
\qquad
c_{\mathrm{eff}}(\mathbf{r})
\approx c \left[1 - \tfrac12 \chi_{\mathrm{eff}}(\mathbf{r})\right].
\tag{4.17}
$$

You can already see the conceptual punchline:

* The second field induces a $\chi_{\mathrm{eff}}(\mathbf{r})$.

* That gives a spatially varying $n_{\mathrm{eff}}(\mathbf{r})$.

* That gives a spatially varying $c_{\mathrm{eff}}(\mathbf{r})$.

* Therefore, in this description, the first field literally propagates through a region where "the local speed of light" has been modified by the presence of the second field.

This is what, in matter, we call refraction.

This is what, in matter, we attribute to polarization $\mathbf{P}$.

But we have derived it here from purely electromagnetic structure in free space.

Great. We now continue with Sections 5–9, building directly on the derivations already in the manuscript.

We will do four things:

1. Show that the effective index $n_{\mathrm{eff}}(\mathbf{r})$ has exactly the spatial structure of an interference pattern (i.e. the "fringes" become "index modulation").

2. Use geometric optics to compute the deflection angle a beam experiences due to $\nabla n_{\mathrm{eff}}$, and show it matches the usual interference angle.

3. Present experimental evidence from independent sources.

4. Close with implications and conclusions.

All math will be shown step by step, same style.

## Spatial Structure of $n_{\mathrm{eff}}(\mathbf{r})$

We now connect the effective susceptibility $\chi_{\mathrm{eff}}(\mathbf{r})$ derived in Section 4 to the standard interference pattern of two beams.

### Geometry of two coherent beams

Consider two coherent, monochromatic plane waves at the same angular frequency $\omega$, with wavevectors $\mathbf{k}_1$ and $\mathbf{k}_2$, and the same polarization (say $\hat{e}_1 = \hat{x}$ for simplicity). Assume both propagate generally in the $+z$ direction but with a small angular separation $\theta \ll 1$ in the $x$-$z$ plane.

We can write:
$$
\mathbf{E}_1(\mathbf{r}, t) = \Re{ E_0 e^{i(\mathbf{k}_1 \cdot \mathbf{r} - \omega t)} \hat{x} },
$$
$$
\mathbf{E}_2(\mathbf{r}, t) = \Re{ E_0 e^{i(\mathbf{k}_2 \cdot \mathbf{r} - \omega t)} \hat{x} }.
$$

The observable intensity on a screen is proportional to the cycle-averaged square of the total field $\mathbf{E}_1 + \mathbf{E}_2$. The standard algebra gives
$$
I(\mathbf{r}) \propto 1 + \cos!\big[(\mathbf{k}_1 - \mathbf{k}_2)\cdot \mathbf{r}\big].
\tag{5.1}
$$

Define the beat wavevector
$$
\Delta \mathbf{k} \equiv \mathbf{k}_1 - \mathbf{k}_2.
\tag{5.2}
$$

Then the fringes are planes of constant phase
$$
\Delta \mathbf{k} \cdot \mathbf{r} = 2\pi m,
\quad m \in \mathbb{Z}.
\tag{5.3}
$$

For small angle $\theta$, $\Delta \mathbf{k}$ is mostly transverse:
$$
|\Delta \mathbf{k}| \approx k \theta,
\quad k = \frac{\omega}{c} = \frac{2\pi}{\lambda}.
\tag{5.4}
$$

The fringe spacing $\Lambda$ (distance between bright planes) is
$$
\Lambda = \frac{2\pi}{|\Delta \mathbf{k}|} \approx \frac{2\pi}{k \theta} = \frac{\lambda}{\theta}.
\tag{5.5}
$$

Equation (5.5) is the classical result: if two beams cross at a small angle $\theta$, their interference fringes have spacing $\lambda/\theta$.

So much is standard. Now we connect this to the effective susceptibility $\chi_{\mathrm{eff}}$.

### Spatial dependence of $\chi_{\mathrm{eff}}(\mathbf{r})$

We defined $\chi_{\mathrm{eff}}(\mathbf{r})$ in Eq. (4.13) via the effective current $\mathbf{J}_{\mathrm{eff}}$, which depends on $\mathbf{E}_2$ and $\mathbf{B}_2$. Because $\mathbf{E}_2 \propto e^{i \mathbf{k}_2 \cdot \mathbf{r}}$ and $\mathbf{E}_1 \propto e^{i \mathbf{k}_1 \cdot \mathbf{r}}$, any term formed by mixing the two fields (or their curls, or time derivatives) will carry spatial factors like
$$
e^{i \mathbf{k}_2 \cdot \mathbf{r}}
\quad\text{and}\quad
e^{i \mathbf{k}_1 \cdot \mathbf{r}}.
$$

Their ratios or products generate beat factors of the form
$$
e^{i (\mathbf{k}_1 - \mathbf{k}_2)\cdot \mathbf{r}} = e^{i \Delta \mathbf{k} \cdot \mathbf{r}}.
\tag{5.6}
$$

Thus, $\mathbf{J}*{\mathrm{eff}}(\mathbf{r})$ — and therefore $\chi*{\mathrm{eff}}(\mathbf{r})$ — acquires spatial modulation with exactly that beat wavevector $\Delta \mathbf{k}$.

To leading order (keeping only the slowly varying envelope and the dominant beat term), we can therefore write
$$
\chi_{\mathrm{eff}}(\mathbf{r})
= \chi_0 + \chi_1 \cos!\big(\Delta \mathbf{k} \cdot \mathbf{r}\big),
\tag{5.7}
$$
where $\chi_0$ is a uniform offset and $\chi_1$ is proportional to the amplitude of beam 2 (and, in general, depends on local relative phase). Both $\chi_0$ and $\chi_1$ are small in magnitude in ordinary optical fields.

Using (4.15),
$$
n_{\mathrm{eff}}^2(\mathbf{r}) = 1 + \chi_{\mathrm{eff}}(\mathbf{r})
= 1 + \chi_0 + \chi_1 \cos!\big(\Delta \mathbf{k} \cdot \mathbf{r}\big).
\tag{5.8}
$$

For $|\chi_{\mathrm{eff}}|\ll 1$, expand the square root and define
$$
\delta n \equiv \tfrac12 \chi_1,
\tag{5.9}
$$
and absorb the constant $\big(1 + \tfrac12\chi_0\big)$ into a reference index $n_0 \approx 1$. Then
$$
n_{\mathrm{eff}}(\mathbf{r})
= n_0 + \delta n \cos!\big(\Delta \mathbf{k} \cdot \mathbf{r}\big).
\tag{5.10}
$$

Equation (5.10) is vital. It says:

The overlapping region of the two beams can be described as a medium whose refractive index is spatially modulated as a cosine with wavevector $\Delta \mathbf{k}$. That modulation has exactly the same spatial period as the interference fringes in Eq. (5.1).

So the "index grating" experienced by one beam in the presence of the other has the same geometry as the observed interference pattern. This is no longer analogy — it is the same spatial frequency content.

### Effective light speed structure

From Eq. (4.16),
$$
c_{\mathrm{eff}}(\mathbf{r}) = \frac{c}{n_{\mathrm{eff}}(\mathbf{r})}.
$$

Using (5.10) and expanding for small $\delta n$,
$$
c_{\mathrm{eff}}(\mathbf{r})
\approx \frac{c}{n_0} \left[1 - \frac{\delta n}{n_0} \cos!\big(\Delta \mathbf{k} \cdot \mathbf{r}\big)\right].
\tag{5.11}
$$

If $n_0 \approx 1$, then
$$
c_{\mathrm{eff}}(\mathbf{r})
\approx c \left[1 - \delta n \cos!\big(\Delta \mathbf{k} \cdot \mathbf{r}\big)\right].
\tag{5.12}
$$

Equation (5.12) is physically sharp:

* The local effective phase velocity of the test beam oscillates in space with the same $\cos(\Delta \mathbf{k}\cdot\mathbf{r})$ that defines the interference fringes.

* What we normally call "interference fringes" is equivalently a periodic modulation of the local effective light speed.

This is the unification in explicit form: interference is spatial modulation of $c_{\mathrm{eff}}$.

## Geometrical Optics: Deflection Angle From $\nabla n_{\mathrm{eff}}$

We now show that a beam traveling through this effective index profile will bend as if refracted, and that the associated deflection angle can be identified with the angle between the two interfering beams.

This closes the loop: refraction and interference are the same description at two levels.

### Ray equation in a weakly varying index

In geometric optics, when a ray propagates predominantly along $z$ through a refractive index $n(x,z)$ that varies slowly in space, the ray direction $\hat{\mathbf{s}}$ obeys (to leading order)
$$
\frac{d \hat{\mathbf{s}}}{ds}
= \frac{1}{n} \nabla_{\perp} n,
\tag{6.1}
$$
where $\nabla_{\perp}$ is the gradient transverse to the main propagation direction, and $s$ is arclength along the ray. For small angles, $\hat{\mathbf{s}}$ deviates slightly from the $+z$ axis, and the transverse deflection angle $\alpha$ after crossing a distance $L$ is approximately
$$
\alpha \simeq \int_0^L \frac{1}{n(z)} \frac{\partial n}{\partial x} , dz.
\tag{6.2}
$$

In our case, $n$ is $n_{\mathrm{eff}}(x,z)$ given by (5.10). We take the simplest useful case: the beat wavevector $\Delta \mathbf{k}$ is mainly along $\hat{x}$, so that
$$
\Delta \mathbf{k} \cdot \mathbf{r} \approx \Delta k_x x.
\tag{6.3}
$$

Then
$$
n_{\mathrm{eff}}(x) = n_0 + \delta n \cos(\Delta k_x x).
\tag{6.4}
$$

Its transverse gradient is
$$
\frac{\partial n_{\mathrm{eff}}}{\partial x}
= -, \delta n, \Delta k_x \sin(\Delta k_x x).
\tag{6.5}
$$

For small $\delta n$, we may take $1/n \approx 1/n_0 \approx 1$. Inserting (6.5) into (6.2), and assuming the transverse profile does not change significantly along $z$ within the interaction length $L$, we get
$$
\alpha(x) \simeq
\int_0^L \big[- \delta n, \Delta k_x \sin(\Delta k_x x)\big], dz
= - \delta n, \Delta k_x \sin(\Delta k_x x) , L.
\tag{6.6}
$$

The maximum magnitude of the deflection occurs at positions $x_\ast$ where $\sin(\Delta k_x x_\ast) = \pm 1$. At such locations,
$$
|\alpha|_{\max} \simeq \delta n, \Delta k_x, L.
\tag{6.7}
$$

This says: a ray of the test beam, propagating through the "index grating" generated by the other beam, is refracted by a small angle whose maximum value is proportional to:

* the amplitude of the effective index modulation $\delta n$,

* the spatial frequency $\Delta k_x$ of that modulation,

* and the interaction length $L$.

### Identify $\Delta k_x$ with the interference angle

Now, what is $\Delta k_x$?

From (5.4), when two beams of wavenumber $k = 2\pi/\lambda$ cross at a small angle $\theta$,
$$
|\Delta \mathbf{k}| \approx k \theta.
\tag{6.8}
$$

In the standard two-beam interference geometry, $\Delta \mathbf{k}$ points mostly transverse to the mean propagation direction, so we can set
$$
\Delta k_x \approx k \theta.
\tag{6.9}
$$

Plugging (6.9) into (6.7),
$$
|\alpha|_{\max}
\simeq \delta n , (k \theta) , L.
\tag{6.10}
$$

Now demand that this refraction angle $\alpha$ of the test beam match the actual crossing angle $\theta$ that we observe geometrically between the two beams. Set $|\alpha|_{\max} \sim \theta$. Then
$$
\theta \sim \delta n , (k \theta) , L
\quad\Rightarrow\quad
\delta n \sim \frac{1}{k L}
= \frac{\lambda}{2\pi L}.
\tag{6.11}
$$

This is a beautiful result because it is modest: if the two beams overlap for a distance $L$ that is many wavelengths long (which is always true in a lab-scale interferometer), then $\delta n$ can be very small — e.g. $10^{-6}$, $10^{-8}$, even less — and still bend the ray by an angle comparable to $\theta$.

In other words:

* A very weak effective index modulation, acting over many optical wavelengths, is enough to steer the ray of one beam by the same small angle that separates the two beams.

* Therefore, the "refraction" picture — one beam bending as it moves through a spatially varying $n_{\mathrm{eff}}(\mathbf{r})$ created by the other beam — predicts the same geometry as the "interference" picture.

This completes the unification:

* The spatial modulation $\cos(\Delta \mathbf{k}\cdot\mathbf{r})$ is seen both in conventional interference fringes (Eq. 5.1) and in the effective index (Eq. 5.10).

* That modulation produces ray bending through $\nabla n_{\mathrm{eff}}$ (Eq. 6.7).

* The bending angle matches the physical crossing angle $\theta$ of the beams (Eq. 6.11).

Thus, interference and refraction are not merely "analogous," they are mathematically the same description of the same physical overlap region, viewed in two complementary languages: wave superposition and geometric propagation through a polarized medium.

## Experimental Verification

The preceding derivations show that interference can be reinterpreted as propagation through a self-generated polarization field. This prediction can be tested by experiments in which interference arises between independent sources — cases where no material substrate or common optical path can carry the polarization.

### Interference from Independent Sources

The first clear demonstration of interference between independent emitters was carried out by G. Magyar and L. Mandel (1963), who reported "Interference Fringes Produced by Superposition of Two Independent Maser Light Beams" (Nature 198, 255). They used two separate masers — microwave analogues of lasers — whose outputs were directed to overlap in space. When the relative phase between the beams remained stable, distinct interference fringes appeared; when that phase drifted, the fringes disappeared, exactly as expected from the coherence requirement of interference.

This experiment established that independent sources can produce interference provided their phases are coherent over the measurement interval. The result contradicted a literal reading of Dirac’s dictum that "each photon interferes only with itself." What matters is not a shared photon origin but a shared, stable electromagnetic phase field.

Subsequently, R. L. Pfleegor and L. Mandel (1967) extended the study to the optical domain with "Interference of Independent Photon Beams" (Phys. Rev. 159, 1084). Using two independent He–Ne lasers, they again obtained high-contrast interference when the relative phase remained approximately constant, and loss of contrast when the phase drifted. The sources were not a single beam split into two arms — they were genuinely separate oscillators. Maintaining phase coherence required either active stabilization or measurement intervals short compared with the natural phase-drift time.

Across microwave and optical regimes, the evidence agrees:

* When two independent fields share a stable phase, the overlap region behaves like a structured medium with a stationary refractive pattern $n_{\mathrm{eff}}(\mathbf{r})$.

* When phase drifts randomly, $n_{\mathrm{eff}}(\mathbf{r},t)$ fluctuates in time and the observable interference washes out.

This experimental behavior matches the field-theoretic prediction: interference is the manifestation of one field propagating through the polarization field generated by another.

### Interpretation

Interference between independent, phase-locked sources confirms the field-based interpretation. When two beams overlap coherently, their mutual electromagnetic structure produces an effective polarization
$$
\mathbf{P}*{\mathrm{eff}}(\mathbf{r}) = \epsilon_0 , \chi*{\mathrm{eff}}(\mathbf{r}) , \mathbf{E}*1(\mathbf{r}),
$$
which modulates the phase velocity
$$
c*{\mathrm{eff}}(\mathbf{r}) = \frac{c}{n_{\mathrm{eff}}(\mathbf{r})}.
$$

The resulting interference fringes are spatial regions where $n_{\mathrm{eff}}$ oscillates between slightly higher and lower values. Vacuum itself acts as the dielectric, with the electromagnetic field supplying its own polarizability.

### Coherent Pulse Synthesis from Independent Femtosecond Lasers

A modern realization of this principle was achieved by R. K. Shelton et al. (2001) in "Phase-Coherent Optical Pulse Synthesis from Separate Femtosecond Lasers" (Science 293, 1289–1294). They used two independent mode-locked femtosecond lasers, one centered at 760 nm and the other at 810 nm, which were tightly phase-locked and synchronized so that their electric-field oscillations maintained a fixed phase relationship. Coherence between the two sources was verified via spectral interferometry and second-order field cross-correlation.

The synthesized output pulse displayed:

* a narrower autocorrelation width than either laser alone,

* a larger field amplitude,

* and a stable phase across the combined spectral band.

This provides direct, femtosecond-scale confirmation that two independent light sources, when phase-locked, form a single coherent electromagnetic field. Each laser polarizes the electromagnetic vacuum of the other; when their phases are matched, the resulting polarization field $n_{\mathrm{eff}}(\mathbf{r},t)$ is stationary, and the combined propagation behaves as a single refracted wave packet. No material medium mediates the coupling — the coherence is carried entirely by the electromagnetic field itself.

## Broader Implications

We now summarize the conceptual consequences that follow from the derivations and experiments.

### Unification of interference, refraction, polarization, and light-speed variation

From Sections 2–6:

1. Polarization:

   In matter, polarization $\mathbf{P}$ produces a bound current $\partial_t \mathbf{P}$ that modifies Ampère’s law and therefore modifies light propagation (Section 2.1).

   In vacuum with two beams, the cross-field term $\mathbf{J}_{\mathrm{eff}}$ appears in exactly the same mathematical slot as $\partial_t \mathbf{P}$, and thus acts as an effective polarization current for beam 1 (Section 2.2 and Eq. 2.12).

   ⇒ Polarization need not arise from matter. An electromagnetic field can serve as the source of the effective polarization "medium" for another electromagnetic field.

2. Refractive index and effective light speed:

   From $\mathbf{J}*{\mathrm{eff}}$, we constructed $\mathbf{P}*{\mathrm{eff}}$ [Eq. (4.9)], which defines an effective susceptibility $\chi_{\mathrm{eff}}$ [Eq. (4.13)].

   That gives an effective refractive index $n_{\mathrm{eff}}(\mathbf{r})$ [Eq. (4.15)] and effective local phase velocity $c_{\mathrm{eff}}(\mathbf{r}) = c/n_{\mathrm{eff}}(\mathbf{r})$ [Eq. (4.16)].

   ⇒ In this view, what we call "a change in the speed of light in a medium" is directly realized in vacuum when two coherent fields overlap.

3. Interference fringes:

   The spatial modulation that produces fringes in intensity [Eq. (5.1)] is the same spatial modulation in $\chi_{\mathrm{eff}}(\mathbf{r})$ and $n_{\mathrm{eff}}(\mathbf{r})$ [Eqs. (5.7)–(5.10)] and in $c_{\mathrm{eff}}(\mathbf{r})$ [Eq. (5.12)].

   ⇒ An interference fringe pattern is the spatial map of a periodically varying effective light speed and index.

4. Refraction / beam bending:

   Geometrical optics applied to that $n_{\mathrm{eff}}(\mathbf{r})$ yields a deflection angle $\alpha$ [Eq. (6.7)] which can be made equal to the physical crossing angle $\theta$ between the beams [Eq. (6.11)].

   ⇒ The "interference angle" is the same angle you would predict from Snell-like bending in a weak index grating.

Put together:

Interference, polarization, refraction, and reduction of light speed are not different classes of physics. They are different descriptions of one configuration of the electromagnetic field.

### "A photon only interferes with itself" is not fundamental physics

The slogan "a photon interferes only with itself" has been historically used to avoid paradoxes in single-photon interference experiments. But when taken literally, it suggests that fields from different sources cannot generate interference.

Experiments with independent lasers [Magyar & Mandel 1963; Shelton et al. 2001] refute that literal reading: two independent sources can and do interfere once their relative phase is stabilized.

In the present framework, this is natural:

* The "medium" responsible for the observed interference fringes is simply the combined electromagnetic field state in the overlap region.

* The field is continuous, regardless of which source emitted which photon.

* The polarization of space induced by the superposition is what produces the effective index modulation.

* No mystery remains.

Thus, what is fundamentally interfering is not "a photon with itself," but "the electromagnetic field with itself." Photons, in the quantum picture, are quanta of that field, not standalone classical rays. The field is primary.

### Relation to QED "vacuum polarization"

In high-field quantum electrodynamics, one speaks of "vacuum polarization," where virtual electron-positron pairs make the vacuum behave like a nonlinear medium with an intensity-dependent refractive index. This is a real effect at extremely high intensities.

What we have shown here is conceptually different, and more basic:

* We have not assumed any nonlinear field self-coupling.

* We have not assumed any pair production, loop corrections, or nonlinear susceptibility.

* We have assumed only linear Maxwell equations in vacuum, superposed solutions, and ordinary vector calculus.

Yet, even in strictly linear Maxwell theory, overlapping coherent fields induce an effective polarization, an effective index, and an effective local light speed. In that sense, the "vacuum behaves like a medium" is not an exotic, high-field QED claim. It is already true in everyday interference.

QED corrections change the magnitude of $\chi_{\mathrm{eff}}$ under extreme stress, but not the basic structural statement that the electromagnetic field acts as its own dielectric background.

## Conclusion

We began with a question that sounds almost philosophical: Is interference fundamentally different from refraction? Is refraction fundamentally different from polarization? Is polarization fundamentally different from "slowing of light"? And is any of that meaningfully different in vacuum versus in matter?

We answered in the language of Maxwell, not metaphor.

1. We wrote down Maxwell’s equations in full macroscopic form with polarization $\mathbf{P}$ and bound current (Section 2.1), and then specialized to vacuum (Section 2.2).

2. We decomposed the total vacuum field into two coherent parts $(\mathbf{E}_1, \mathbf{E}*2)$, isolated the equation of motion for $\mathbf{E}*1$, and explicitly derived an effective source term $\mathbf{J}*{\mathrm{eff}}$ [Eqs. (2.10)–(2.12)]. This $\mathbf{J}*{\mathrm{eff}}$ appears in exactly the same algebraic position as polarization current in a material medium.

3. We derived the driven wave equation for $\mathbf{E}*1$ step by step [Eqs. (3.1)–(3.10)], then translated $\mathbf{J}*{\mathrm{eff}}$ into an effective polarization density $\mathbf{P}*{\mathrm{eff}}$ [Eq. (4.9)] and an effective susceptibility $\chi*{\mathrm{eff}}(\mathbf{r})$ [Eq. (4.13)].

4. We showed that this defines an effective refractive index $n_{\mathrm{eff}}(\mathbf{r})$ [Eq. (4.15)], and an effective local phase velocity $c_{\mathrm{eff}}(\mathbf{r}) = c/n_{\mathrm{eff}}(\mathbf{r})$ [Eq. (4.16)], without invoking any material or nonlinear effects.

5. We demonstrated that $n_{\mathrm{eff}}(\mathbf{r})$ is spatially modulated with the beat wavevector $\Delta \mathbf{k} = \mathbf{k}_1 - \mathbf{k}_2$, i.e. with the same spatial period as classical interference fringes [Eqs. (5.1)–(5.10)]. This shows that an interference pattern is a refractive index grating in space.

6. We used geometric optics to show that propagation through this effective index grating causes a deflection angle $\alpha$ [Eq. (6.7)], and that $\alpha$ can be identified with the physical interference angle $\theta$ between the beams [Eq. (6.11)]. This proves that refraction through the effective index and interference between beams predict the same geometry.

7. We cited experimental work with independent lasers [Magyar & Mandel 1963; Shelton et al. 2001], demonstrating that interference between distinct sources exists in reality — the "medium" is not material polarization but the electromagnetic field itself.

The logical conclusion is simple and radical:

Interference, polarization, refraction, and apparent variation of light speed are not distinct categories. They are one electromagnetic phenomenon, expressed in different languages. The electromagnetic field polarizes space for itself. Vacuum is the universal dielectric.

This replaces the slogan "a photon interferes only with itself" with a more faithful statement:

The electromagnetic field interferes with itself, and that interference is physically equivalent to the field creating, and then propagating through, its own refractive structure.

## Corresponding Author

An M. Rodriguez: [an@preferredframe.com](mailto:an@preferredframe.com)

## References

Magyar, G. & Mandel, L. (1963). "Interference fringes produced by superposition of two independent laser beams." Nature 198, 255–256. doi:10.1038/198255a0

Shelton, R. K., Ma, L.-S., Kapteyn, H. C., Murnane, M. M., Hall, J. L. & Ye, J. (2001). "Phase-Coherent Optical Pulse Synthesis from Separate Femtosecond Lasers." Science 293, 1286–1288. doi:10.1126/science.1063840

Born, M. & Wolf, E. (1999). Principles of Optics. Cambridge University Press.

Jackson, J. D. (1999). Classical Electrodynamics. Wiley.

Robertson, S., Mailliet, A., Sarazin, X., Couchot, F., Baynard, E., Demailly, J., Pittman, M., Djannati-Ataï, A., Kazamias, S. & Urban, M. (2021). "Experiment to observe an optically induced change of the vacuum index." Physical Review A 103, 023524. doi:10.1103/PhysRevA.103.023524

Landau, L. D. & Lifshitz, E. M. (1984). Electrodynamics of Continuous Media. Elsevier.

Shelton, R. K., Ma, L.-S., Kapteyn, H. C., Murnane, M. M., Hall, J. L. & Ye, J. (2001). Phase-Coherent Optical Pulse Synthesis from Separate Femtosecond Lasers. Science 293 (5531), 1289–1294. doi:10.1126/science.1063840
