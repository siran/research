# Defining Topological Charge in a Source-Free Maxwell Universe

Anes Palma, An M. Rodriguez (an@preferredframe.com)  
August 2025

## Abstract

We explore the concept of "topological charge" in a universe governed solely by source-free Maxwell equations. Without invoking mass, particles, or source terms, we show that quantized circulation of electromagnetic fields in bounded configurations—particularly toroidal standing waves—leads to stable, conserved quantities analogous to electric charge. These topological charges arise from the global structure and coherence of the fields, especially the integral properties of their curls. We analyze the nature of these quantities, derive their conservation laws, and show how they lead to interactions, inertia, and quantization within a classical field ontology. This formulation offers a geometric, source-free foundation for understanding charge as a consequence of topological field structure rather than point-like sources.

## Introduction

The standard Maxwell equations in vacuum describe the behavior of electric and magnetic fields in the absence of charges and currents. These are:

$$
\nabla \cdot \vec{E} = 0, \qquad
\nabla \cdot \vec{B} = 0, \qquad
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \qquad
\nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
$$

These equations form a self-consistent system supporting propagating waves at the speed

$$
c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}.
$$

In this framework, there are no explicit sources. Nevertheless, structured field configurations such as toroidal standing waves exhibit behaviors analogous to particles with charge: they are localized, stable, interact at a distance, and exhibit inertia. In this paper, we formalize the notion of topological charge as a quantized, conserved quantity arising purely from the geometry and coherence of source-free electromagnetic fields.

## Standing Waves and Toroidal Confinement

To examine how field structures can be confined and stabilized, we consider electromagnetic fields forming standing waves on a toroidal manifold. Let $R$ and $r$ be the major and minor radii of the torus. The geometry has two independent angular directions:

- The toroidal direction (around the large circle), parameterized by a winding number $n_1$
- The poloidal direction (around the small circle), parameterized by $n_2$

For a stable, periodic standing wave, the wavelengths must fit integer multiples in each direction. The allowed wavelengths are:

$$
\lambda_1 = \frac{2\pi R}{n_1}, \qquad
\lambda_2 = \frac{2\pi r}{n_2}
$$

The spatial wavenumbers are:

$$
k_1 = \frac{n_1}{R}, \qquad
k_2 = \frac{n_2}{r}, \qquad
k^2 = k_1^2 + k_2^2
$$

The angular frequency is related by the dispersion relation:

$$
\omega = c \sqrt{k_1^2 + k_2^2}
$$

The corresponding energy of the mode is:

$$
E_{n_1 n_2} = \hbar_g \omega = \hbar_g c \sqrt{k_1^2 + k_2^2}
$$

where $\hbar_g$ is an emergent constant defined by the lowest mode:

$$
\hbar_g = \frac{E_{11}}{\omega_{11}}
$$

These toroidal modes are characterized by their winding numbers $(n_1, n_2) \in \mathbb{Z}^2$, which cannot change continuously. This is the origin of topological quantization.

## Circulation and Curl-Based Modes

In classical electromagnetism, the curl of a field indicates local rotation. For a vector field $\vec{F}$, the circulation around a closed loop $C$ is:

$$
\oint_C \vec{F} \cdot d\vec{\ell}
= \iint_S (\nabla \times \vec{F}) \cdot d\vec{S}
$$

This integral depends only on the curl of the field over the surface bounded by $C$. In regions where $\nabla \cdot \vec{F} = 0$ and $\vec{F}$ is continuous, the circulation is conserved under smooth deformations of $C$.

In a toroidal field configuration, the electric and magnetic fields are constructed from curls:

$$
\vec{E} = \nabla \times \vec{A}_E, \qquad
\vec{B} = \nabla \times \vec{A}_B
$$

where $\vec{A}_E$ and $\vec{A}_B$ are vector potentials. Because the field lines form closed loops on the torus, the integral of the curl over these loops is quantized:

$$
\oint \vec{E} \cdot d\vec{\ell} = 2\pi n_1 E_0, \qquad
\oint \vec{B} \cdot d\vec{\ell} = 2\pi n_2 B_0
$$

for some constants $E_0, B_0$ set by the amplitude of the fundamental mode. These quantized circulations are preserved as long as the field configuration remains continuous and confined.

We define the topological charge $Q$ as a pair of integers:

$$
Q = (n_1, n_2)
$$

corresponding to the winding numbers of the electric and magnetic fields. These charges are topologically invariant: they cannot change unless the field is discontinuous or escapes the torus.

## Helicity and Field Knottedness

Helicity is a scalar measure of the linkage or knottedness of field lines. For a magnetic field $\vec{B}$ with vector potential $\vec{A}$ (such that $\vec{B} = \nabla \times \vec{A}$), the helicity is defined as:

$$
\mathcal{H} = \int \vec{A} \cdot \vec{B} \, d^3x
$$

This quantity is gauge-invariant under appropriate boundary conditions and is conserved in source-free Maxwell dynamics. In toroidal configurations, helicity is directly related to the product of the winding numbers:

$$
\mathcal{H} \propto n_1 n_2
$$

A nonzero helicity implies a nontrivial topological structure in the field: the field lines are linked or twisted in a way that cannot be undone by smooth deformations. This reinforces the interpretation of $Q = (n_1, n_2)$ as a topological invariant.

## Conservation of Topological Charge

We now show that topological charge is conserved under Maxwell dynamics. The relevant conservation law is the evolution of the field momentum:

$$
\vec{g} = \varepsilon_0 \vec{E} \times \vec{B}
$$

The momentum density evolves according to:

$$
\frac{\partial \vec{g}}{\partial t} + \nabla \cdot \mathbf{T} = 0
$$

where $\mathbf{T}$ is the Maxwell stress tensor:

$$
T_{ij} = \varepsilon_0 \left( E_i E_j + c^2 B_i B_j - \frac{1}{2} \delta_{ij} \left( |\vec{E}|^2 + c^2 |\vec{B}|^2 \right) \right)
$$

Integrating over a volume $V$ bounded by a surface $\partial V$, the total field momentum evolves as:

$$
\frac{d}{dt} \int_V \vec{g} \, d^3x = - \int_{\partial V} \mathbf{T} \cdot d\vec{A}
$$

If the fields are confined (i.e., vanish on the boundary), then the right-hand side is zero and the total momentum is conserved. Since the topological charge is defined via integrals over loops inside $V$, and the field topology does not change under continuous Maxwell evolution, the charge $Q$ is also conserved.

## Emergence of Charge-like Behavior

The topological charge $Q$ manifests physically in several ways:

1. **Long-range interaction**: Toroidal modes with nonzero $Q$ interact via standing-wave modes between them. The allowed energy of these modes scales as $1/r$, and differentiation yields a $-1/r^2$ force between field structures. This mimics Coulomb attraction.

2. **Inertia**: The internal circulation of momentum inside the toroidal field leads to resistance to acceleration. The object exhibits effective mass:

$$
m_{\text{eff}} = \frac{U}{c^2}, \qquad
U = \int u \, d^3x
$$

3. **Quantization**: The allowed values of $Q$ are discrete, imposing quantization on energy levels, sizes, and allowed states—similar to the energy spectrum of the hydrogen atom.

4. **Persistence**: These configurations are topologically stable. A toroidal mode with $Q \ne 0$ cannot decay continuously into the vacuum.

This reinterprets "charge" as a manifestation of topological circulation, rather than the divergence of a field. In conventional terms, electric charge satisfies:

$$
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}
$$

In the source-free framework, $\rho = 0$ everywhere, yet stable field objects with nontrivial $Q$ behave as if they carry effective "charge".

### Energy–Energy Attraction and Variable Propagation Speed

The standing-wave derivation gives a $1/r^2$ force between two toroidal charges because each shared normal mode carries an energy  
$W_m(r) \propto 1/r$. Differentiating yields  
$F = -\partial_r W \propto -1/r^2$.

In our separate analysis of variable vacuum parameters, we showed that a **local increase in electromagnetic energy density** $u$ multiplies both  
$\varepsilon_0$ and $\mu_0$ by the same factor $f(p)$, where $p$ stands for energy density:

$$
\varepsilon(x) = \varepsilon_0 f(p), \qquad
\mu(x) = \mu_0 f(p)
$$

The local wave speed becomes:

$$
c_{\text{eff}}(x) = \frac{1}{\sqrt{\mu(x)\varepsilon(x)}} =
\frac{c}{f(p)}
$$

A spatial gradient of $f(p)$—hence of energy density—acts as an **effective refractive-index gradient**. Light (and any confined field structure) drifts toward higher-$f$ regions just as rays bend toward higher optical index in geometrical optics. Writing  
$f(p) = 1 + \delta f$ with $\delta f \ll 1$, the effective potential for a slowly varying envelope is:

$$
V(\mathbf{x}) = \hbar_g \, \omega_{11} \, \delta f(\mathbf{x})
$$

So a gradient in $u$ produces a force  
$\vec{F}_{\text{eff}} = -\nabla V$.

Putting the pieces together:

- **Topological charge** fixes the integer windings $(n_1, n_2)$ and therefore the baseline energy density inside a torus.
- Higher windings raise $u$ and thus the local $f(p)$, reducing $c_{\text{eff}}$ inside the core.
- Two distant tori therefore see each other as regions of elevated $f(p)$; the resulting index gradient reproduces the same $-1/r^2$ pull derived from the standing-wave argument, but now framed as **energy attracting energy**.
- Because inertial mass in this ontology is simply $m_{\text{eff}} = U / c^2$, the interaction couples proportional to “mass” as well—mirroring the equivalence of mass and energy without invoking separate gravitational or electric charges.

Hence the Coulomb-like force and the energy–energy attraction are two views of the same underlying mechanism: variations in field energy density modify the local propagation speed and generate a stress-tensor gradient that pulls coherent structures together.


## Conclusion

In a source-free Maxwell universe, electromagnetic fields can organize into confined, coherent structures with nontrivial topology. These structures are characterized by winding numbers $(n_1, n_2)$, which remain invariant under smooth field evolution. We interpret these integers as topological charges.

These charges correspond to quantized circulation of the electric and magnetic fields. They generate conserved quantities such as energy, momentum, angular momentum, and helicity. Field configurations with nonzero topological charge interact, resist acceleration, and form discrete energy levels—exhibiting all the classical properties of particles with charge.

This formulation provides a purely geometric and field-theoretic origin for charge, independent of point particles or source terms. It shows that Maxwell’s equations, when combined with global topology and boundary coherence, are sufficient to generate the rich structure of matter and interaction from fields alone.

## References

1. Rodriguez A. M., Palma A., Hydrogen Atom Quantization from Purely Classical Maxwell Electromagnetic Fields, 2025  
2. Palma A., Rodriguez A. M., Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics, 2025  
3. Palma A., Rodriguez A. M., Emergent -1/L² Interaction Force in a Pure Maxwell Universe, 2025  
4. Palma A., Rodriguez A. M., Explaining Conservation Laws in a Maxwell Universe Ontology, 2025  
5. Jackson J. D., Classical Electrodynamics, 3rd ed., Wiley, 1999
