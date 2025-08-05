# Explaining Conservation Laws in a Maxwell Universe Ontology

By Anes Palma, An Rodriguez (an@preferredframe.com)  
Aug 2025  

## Abstract  
We derive the fundamental conservation laws of linear and angular momentum in a universe governed solely by source-free Maxwell equations. In this ontology, all matter consists of self-confined, structured electromagnetic fields. Without invoking particles, masses, or mechanical axioms, we demonstrate how momentum and angular momentum emerge directly from Maxwell dynamics. We show how their conservation arises under symmetry and closure conditions, and how deviations result from stress redistribution. This paper provides a complete mechanical foundation for conservation laws in a purely electromagnetic universe.

## Summary  
All classical mechanical behavior—including inertia, motion, and conservation laws—is shown to emerge rigorously from source-free Maxwell field dynamics alone.

## Keywords  
Maxwell equations; electromagnetic ontology; momentum conservation; angular momentum; stress tensor; inertia; field mechanics; emergent motion; pure electromagnetism

## Introduction  
Conservation laws form the backbone of classical mechanics, usually derived from Newtonian axioms or, more generally, from Noether’s theorem. In a universe whose only ontology is the electromagnetic field obeying source-free Maxwell equations, there are no particles or auxiliary mechanical postulates. All physical entities are structured field configurations, such as standing waves or localized toroidal modes.

Two recent results motivate the present study:

* **Hydrogen spectrum from Maxwell fields.**  We showed that the Rydberg energy ladder of the hydrogen atom emerges when the atom is modeled as a self-confined toroidal standing wave of the electromagnetic field [5].  
* **Schrödinger equation from Maxwell fields.**  We demonstrated that a narrow-band analytic projection of a source-free Maxwell mode obeys the Schrödinger equation with effective $\hbar$ and $m$ fixed by field geometry [3].

Together these results suggest that *all* matter may be electromagnetic configuration. The principal aim here is to close another conceptual gap: to explain how such configurations—whose internal updates propagate at light speed—nevertheless behave like everyday objects with subluminal center-of-energy speeds and the full suite of Newtonian conservation laws.

We proceed by identifying the field-theoretic quantities that play the roles of energy, linear momentum, and angular momentum, and by deriving their balance laws directly from Maxwell’s equations and appropriate boundary conditions.

## Maxwell Equations in Vacuum  
We use SI units and the source-free equations  

$$
\nabla\!\cdot\!\vec{E}=0,\qquad
\nabla\!\cdot\!\vec{B}=0,\qquad
\nabla\!\times\!\vec{E}=-\frac{\partial\vec{B}}{\partial t},\qquad
\nabla\!\times\!\vec{B}=\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}.
$$  

These four equations supply all dynamics; every “object’’ is an electromagnetic field packet, and every “force’’ is electromagnetic.

## Energy and Momentum in Fields  
Electromagnetic energy density  

$$
u=\tfrac12\bigl(\epsilon_0|\vec{E}|^{2}+{\textstyle\frac1{\mu_0}}|\vec{B}|^{2}\bigr).
$$  

Poynting vector  

$$
\vec{S}=\frac1{\mu_0}\,\vec{E}\times\vec{B}.
$$  

Momentum density  

$$
\vec{g}=\frac1{c^{2}}\vec{S}=\epsilon_0\,\vec{E}\times\vec{B}.
$$  

Total linear momentum in volume $V$  

$$
\vec{P}=\int_V\vec{g}\,d^{3}x
        =\epsilon_0\!\int_V\!\vec{E}\times\vec{B}\,d^{3}x .
$$  

## Time Evolution of Field Momentum  
Differentiating $\vec{g}$ and inserting Maxwell relations gives  

$$
\frac{\partial\vec{g}}{\partial t}
=\frac1{\mu_0}\!\left[(\nabla\!\times\!\vec{B})\times\vec{B}
                     -\vec{E}\times(\nabla\!\times\!\vec{E})\right].
$$  

Using vector identities one obtains the local balance  

$$
\frac{\partial\vec{g}}{\partial t}+\nabla\!\cdot\!\mathbf{T}=0 ,
$$  

with symmetric stress tensor  

$$
T_{ij}=\epsilon_0\!\left(E_iE_j+c^{2}B_iB_j
             -\tfrac12\delta_{ij}(|\vec{E}|^{2}+c^{2}|\vec{B}|^{2})\right).
$$  

## Global Momentum Conservation  
Integrating over $V$  

$$
\frac{d\vec{P}}{dt}=-\!\int_{\partial V}\mathbf{T}\cdot d\vec{A}.
$$  

Momentum is conserved when the flux through $\partial V$ vanishes:  

$$
\int_{\partial V}\mathbf{T}\cdot d\vec{A}=0 .
$$  

For a self-confined configuration whose external fields cancel at the boundary, this equality holds and $\vec{P}$ stays constant.

## Center of Energy and Inertial Motion  
Total energy and center of energy  

$$
U=\int_V u\,d^{3}x,\qquad
\vec{R}(t)=\frac1U\int_V\vec{r}\,u\,d^{3}x .
$$  

Because $\vec{P}=U\,d\vec{R}/dt$, a constant $\vec{P}$ implies constant $d\vec{R}/dt$. Inertia is therefore an *outcome* of field momentum, not an added postulate.

## Angular Momentum of Fields  
Angular-momentum density and total angular momentum  

$$
\vec{\ell}=\vec{r}\times\vec{g},\qquad
\vec{L}=\int_V\vec{\ell}\,d^{3}x
      =\epsilon_0\!\int_V\!\vec{r}\times(\vec{E}\times\vec{B})\,d^{3}x .
$$  

Their balance law  

$$
\frac{d\vec{L}}{dt}=-\!\int_{\partial V}\vec{r}\times(\mathbf{T}\cdot d\vec{A})
$$  

shows $\vec{L}$ is conserved when the total torque crossing $\partial V$ is zero:  

$$
\int_{\partial V}\vec{r}\times(\mathbf{T}\cdot d\vec{A})=0 .
$$  

For a self-confined, reflection-symmetric configuration—such as a toroidal standing wave—this condition is met and $\vec{L}$ remains constant.

## Rotational Inertia and the Wheel Analogy  
A familiar wheel spins because its matter carries angular momentum.  
In a Maxwell universe the analogue is a bounded electromagnetic structure whose fields carry non-zero  

$$
\vec{L}=\epsilon_0\!\int_V\!\vec{r}\times(\vec{E}\times\vec{B})\,d^{3}x .
$$  

**Effective moment of inertia**  
Let $\omega$ be the uniform phase-rotation rate about some axis. For a time-stationary configuration  

$$
\vec{L}=I_{\text{eff}}\,\vec{\omega},\qquad
I_{\text{eff}}=\frac1{\omega^{2}}
               \,\epsilon_0\!\int_V\!|\vec{E}\times\vec{B}|_{\perp}\,d^{3}x ,
$$  

where $|\,\cdot\,|_{\perp}$ picks the component perpendicular to the axis.

**Persistence of rotation**  
Source-free Maxwell dynamics is lossless, so $\partial_t\vec{L}=0$ whenever the boundary torque vanishes. An electromagnetic “wheel’’ therefore spins indefinitely; an external torque is required to change $\vec{L}$.

## Mechanical Behavior Without Mass  
In a Maxwell universe every “object’’ is a packet of electromagnetic energy. These packets—dipoles, toroids, or more intricate knots—exhibit the hallmarks of mass: they resist sudden acceleration yet can move far below the speed of light. We trace these behaviours directly to Maxwell’s equations; no explicit mass parameter is introduced.

### Definition of Push  
A **push** is a transient external field $(\vec{E}_{\text{ext}},\vec{B}_{\text{ext}})$ that overlaps a localized object for $t\in[t_0,t_1]$:

$$
\vec{E}_{\text{tot}}=\vec{E}+\vec{E}_{\text{ext}},\qquad
\vec{B}_{\text{tot}}=\vec{B}+\vec{B}_{\text{ext}} .
$$  

The momentum density becomes $\vec{g}_{\text{tot}}=\epsilon_0\vec{E}_{\text{tot}}\times\vec{B}_{\text{tot}}$, altering the object’s momentum.

### Definition of Deformation  
A **deformation** is the local change in field amplitude, phase, or shape produced by the non-uniform overlap. Maxwell’s local balance  

$$
\frac{\partial\vec{g}}{\partial t}=-\nabla\!\cdot\!\mathbf{T}
$$  

forces redistribution of energy and momentum inside $V$:

* the most strongly overlapped region gains energy and momentum;  
* neighbouring regions adjust via internal stresses that propagate at $c$;  
* these strain-like adjustments keep $d\vec{R}/dt$ well below $c$, in line with everyday motion.

### Redistribution of Energy and Momentum  
With  

$$
U_0,\vec{P}_0\quad\text{and}\quad U_1,\vec{P}_1
$$  

values before and after the push, the impulse

$$
\Delta\vec{P}=\vec{P}_1-\vec{P}_0
$$  

is absorbed by internal phase and shape shifts, not by point-masses.

### Emergence of Persistent Motion  
After relaxation the object moves with  

$$
\frac{d\vec{R}}{dt}=\frac{\vec{P}_1}{U_1},
$$  

continuing until another interaction occurs—there is no intrinsic damping in vacuum.

### Boundary of a Field Object  
Choose $V$ as the smallest region where  

1. energy, momentum, and stress integrals converge;  
2. $u$ outside $V$ falls below a fixed threshold $\varepsilon$;  
3. $\vec{S}$ is tangential or zero on $\partial V$.  

This surface cleanly separates the dynamical interior from its surroundings.

### Summary  
A push redistributes momentum; the object then moves at a constant velocity set by its new $\vec{P}$. Inertia is an internal, purely electromagnetic phenomenon.

## Emergence of $F = ma$  
Define  

$$
m_{\text{eff}}=\frac{U}{c^{2}},\qquad U=\int_V u\,d^{3}x,
$$  

so that $\vec{P}=m_{\text{eff}}\vec{v}$ with $\vec{v}=d\vec{R}/dt$. Differentiating and using the boundary flux gives  

$$
\boxed{\;\vec{F}_{\text{ext}}=m_{\text{eff}}\vec{a}\;}
$$  

where $\vec{a}=d\vec{v}/dt$. Newton’s second law is therefore an identity that links stress-tensor flux to the rate of change of field momentum.

## Example: Dipole in a Gradient  
Consider a dipole-like object along $z$, lobes at $\pm d$. Entering a background energy density  

$$
u_{\text{bg}}(z)=u_0+\alpha z
$$  

adds a position-dependent stress. The net internal field force  

$$
\vec{F}_{\text{eff}}=\int_V\nabla\!\cdot\!\mathbf{T}_{\text{bg}}\,d^{3}x
                  \approx\Bigl(\tfrac{dT_{zz}}{dz}\Bigr)\,V_{\text{eff}}\hat{z},
$$  

so the dipole drifts with  

$$
\frac{d\vec{R}}{dt}=\frac{\vec{P}_{\text{field}}}{U},\qquad
\frac{d\vec{P}_{\text{field}}}{dt}\approx
        \Bigl(\tfrac{dT_{zz}}{dz}\Bigr)V_{\text{eff}}\hat{z}.
$$  

Motion arises purely from spatial variation of the background stress tensor.

## Conclusion  
* Linear momentum, angular momentum and energy are field integrals; their balances follow from $\partial_t\vec{g}+\nabla\!\cdot\!\mathbf{T}=0$ and Poynting’s theorem.  
* A confined field object moves at constant velocity when $\vec{P}$ is constant and spins at constant angular rate when $\vec{L}$ is constant—outcomes, not assumptions, of Maxwell dynamics.  
* The familiar law $\vec{F}=m\vec{a}$ is recovered with $m=U/c^{2}$; forces are the surface fluxes of the Maxwell stress tensor.  
* Departures from uniform motion occur only when external gradients inject or remove momentum or torque through $\mathbf{T}$.

Classical mechanics—translation, rotation, and Newton’s second law—thus follows rigorously from source-free electromagnetic dynamics, with no need for particles, intrinsic mass, or curved space-time.

## References  
1. Jackson, J. D., *Classical Electrodynamics*, 3rd ed., Wiley, 1999.  
2. Landau, L. D., Lifshitz, E. M., *The Classical Theory of Fields*, Pergamon Press, 1971.  
3. Rodriguez, A. M., Palma, A., *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*, 2025.  
4. Griffiths, D. J., *Introduction to Electrodynamics*, 4th ed., Pearson, 2013.  
5. Rodriguez, A. M., Palma, A., *Hydrogen Atom Quantization from Purely Classical Maxwell Electromagnetic Fields*, 2025.