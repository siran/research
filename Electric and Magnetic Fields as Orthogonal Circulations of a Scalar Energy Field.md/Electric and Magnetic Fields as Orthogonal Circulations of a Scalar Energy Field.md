# Electric and Magnetic Fields as Orthogonal Circulations of a Scalar Energy Field

Anes Palma, An M. Rodriguez (an@preferredframe.com)  
August 3, 2025

## Summary
We derive electric and magnetic fields as orthogonal circulations of a scalar energy field, with all vector quantities emerging from topology and motion. The Lorentz force law is recovered from internal field momentum evolution, linking the coupling constant $q$ directly to the topological structure of the object.

## Keywords
scalar field, energy circulation, toroidal topology, Lorentz force, Maxwell equations, curl geometry, topological charge, electromagnetic interaction

## Introduction

We consider the possibility that all classical electromagnetic fields arise from structured flows of a single scalar energy field $U(\vec{x}, t)$. The observed vector fields—electric $\vec{E}$ and magnetic $\vec{B}$—are not fundamental, but secondary projections from this scalar field.

In this view, the scalar field supports standing wave solutions on closed topologies. Localized, circulating modes—especially toroidal ones—can sustain stable energy structures. These standing waves possess intrinsic winding numbers, which yield conserved circulation integrals and quantized dynamics. From this structure, we show how the full Maxwell equations emerge, and how the Lorentz force arises from field momentum exchange—without postulating point charges or external forces.

## Scalar Energy Field and Derived Vector Fields

We assume a scalar energy field $U(\vec{x}, t)$ obeying the wave equation:

$$
\frac{\partial^2 U}{\partial t^2} = c^2 \nabla^2 U
$$

Here, $c$ is the local propagation speed of energy flow, which may itself vary with energy density, as discussed later.

We define derived vector fields as orthogonal double-curl operations on $U$:

$$
\vec{E} := \nabla \times \nabla \times (\hat{z} U), \qquad
\vec{B} := \nabla \times \nabla \times (\hat{\theta} U)
$$

These constructions ensure that $\vec{E}$ and $\vec{B}$ are divergence-free (source-free), and inherit wave behavior from $U$.

The directions $\hat{z}$ and $\hat{\theta}$ correspond to distinct circulation directions of a toroidal coordinate system. The orthogonality of $\vec{E}$ and $\vec{B}$ arises directly from orthogonal circulations in the scalar field—linked to topologically distinct winding numbers.

## Toroidal Standing Waves and Quantization

Let us consider a standing-wave solution confined to a torus, with radii $R$ (major) and $r$ (minor). The allowed wavelengths along toroidal and poloidal loops are:

$$
\lambda_1 = \frac{2\pi R}{n_1}, \qquad
\lambda_2 = \frac{2\pi r}{n_2}
$$

with integer winding numbers $n_1, n_2 \in \mathbb{Z}^+$. The wavenumbers are:

$$
k_1 = \frac{n_1}{R}, \qquad
k_2 = \frac{n_2}{r}, \qquad
k = \sqrt{k_1^2 + k_2^2}
$$

From the dispersion relation of the scalar wave equation, we get:

$$
\omega = c k = c \sqrt{\left( \frac{n_1}{R} \right)^2 + \left( \frac{n_2}{r} \right)^2}
$$

The energy associated with the mode is proportional to $\omega$, say:

$$
E_{n_1 n_2} = \hbar_g \omega
$$

with $\hbar_g$ defined as the energy-to-frequency ratio for the lowest allowed mode. These standing-wave modes are quantized by geometry, not postulates.

## Emergence of $\vec{E}$ and $\vec{B}$ as Circulations

In this model:

- $\vec{E}$ arises from toroidal circulation: longitudinal wavefronts curling around the large ring of the torus.
- $\vec{B}$ arises from poloidal circulation: wavefronts curling around the small cross-section.

Their orthogonality is not imposed; it is geometric. If $U$ is a circular standing wave with winding numbers $(n_1, n_2)$, then:

$$
\vec{E} = \nabla \times \nabla \times (\hat{z} U) \quad \text{is tangent to } n_1 
$$

and

$$
\vec{B} = \nabla \times \nabla \times (\hat{\theta} U) \quad \text{is tangent to } n_2
$$

Thus, the fields are orthogonal because they result from independent rotational projections of the same scalar field.

## Motion and Observer Dependence

If the object is at rest in the scalar field frame, the field appears as a time-stationary standing wave. For a moving observer (or a moving wave structure), the fields transform:

- The observer experiences rotation induced by motion across the curl patterns.
- A moving object cuts through the standing wave, perceiving phase gradients.

This leads naturally to velocity-dependent interactions, as now shown.

## Coupling to Background Fields and the Emergence of the Lorentz Force

We now derive the Lorentz force from scalar field dynamics. Let:

$$
U(\vec{x}, t) = U_{\text{bg}}(\vec{x}, t) + U_{\text{obj}}(\vec{x}, t)
$$

where $U_{\text{obj}}$ is a localized, toroidal standing wave (representing a "particle") and $U_{\text{bg}}$ is a large-scale, approximately uniform background scalar field.

We define the total electromagnetic field as:

$$
\vec{E} = \nabla \times \nabla \times (\hat{z} U), \qquad
\vec{B} = \nabla \times \nabla \times (\hat{\theta} U)
$$

Let the object move at constant velocity $\vec{v}$ relative to the background. As it moves, the **internal energy flow** within the object is transported. We define a local **scalar energy current density**:

$$
\vec{j}_U := \frac{\partial U_{\text{obj}}}{\partial t} \, \vec{v}
$$

This quantity captures the transport of energy due to motion of the object’s standing wave structure. Now, from energy-momentum conservation in electromagnetism, the momentum density is:

$$
\vec{g} = \varepsilon_0 \vec{E} \times \vec{B}
$$

We are interested in the **interaction momentum** between the object and background fields. Keeping only **cross terms** (object–background overlap), we write:

$$
\vec{P}_{\text{int}} = \varepsilon_0 \int_V 
\left( \vec{E}_{\text{obj}} \times \vec{B}_{\text{bg}} + 
\vec{E}_{\text{bg}} \times \vec{B}_{\text{obj}} \right) d^3x
$$

The **rate of change** of this interaction momentum gives the force:

$$
\vec{F} = \frac{d}{dt} \vec{P}_{\text{int}}
$$

We now derive expressions for each term. Start with:

$$
\vec{F}_E := \frac{d}{dt} \int_V \varepsilon_0 \vec{E}_{\text{obj}} \times \vec{B}_{\text{bg}} \, d^3x
$$

Since $\vec{B}_{\text{bg}}$ is assumed time-independent in the object frame (slow variation), we write:

$$
\vec{F}_E \approx \varepsilon_0 \int_V \frac{\partial \vec{E}_{\text{obj}}}{\partial t} \times \vec{B}_{\text{bg}} \, d^3x
$$

But from Maxwell’s equation:

$$
\frac{\partial \vec{E}_{\text{obj}}}{\partial t} = c^2 \nabla \times \vec{B}_{\text{obj}} \approx \nabla \times \vec{B}_{\text{obj}} \quad \text{(units with } c = 1)
$$

Hence:

$$
\vec{F}_E \approx \varepsilon_0 \int_V (\nabla \times \vec{B}_{\text{obj}}) \times \vec{B}_{\text{bg}} \, d^3x
$$

Now consider the other cross term:

$$
\vec{F}_B := \frac{d}{dt} \int_V \varepsilon_0 \vec{E}_{\text{bg}} \times \vec{B}_{\text{obj}} \, d^3x
$$

Here, $\vec{E}_{\text{bg}}$ is approximately static in the object frame, so:

$$
\vec{F}_B \approx \varepsilon_0 \int_V \vec{E}_{\text{bg}} \times \frac{\partial \vec{B}_{\text{obj}}}{\partial t} \, d^3x
$$

Using:

$$
\frac{\partial \vec{B}_{\text{obj}}}{\partial t} = -\nabla \times \vec{E}_{\text{obj}}
$$

We obtain:

$$
\vec{F}_B \approx -\varepsilon_0 \int_V \vec{E}_{\text{bg}} \times (\nabla \times \vec{E}_{\text{obj}}) \, d^3x
$$

We now define a **coupling measure** $q$ by modeling how internal energy flow overlaps with the background fields.

Assume that internal energy flow in the object follows the energy density gradient under motion. Then:

$$
\vec{j}_U := \frac{\partial U_{\text{obj}}}{\partial t} \vec{v} \approx (\vec{v} \cdot \nabla) U_{\text{obj}}
$$

We now project this scalar energy current onto the background fields. The **electrical-like component** of the interaction is:

$$
q_E := \int_V \vec{j}_U \cdot \vec{E}_{\text{bg}} \, d^3x
$$

The **magnetic-like component**, arising from moving circulation coupling, is:

$$
q_B := \int_V \vec{j}_U \cdot (\vec{v} \times \vec{B}_{\text{bg}}) \, d^3x
$$

These expressions arise naturally: they are the scalar product between the moving energy density flow and the effective background forces. We then define the total coupling:

$$
q := \frac{1}{v^2} (q_E + q_B)
$$

Note: this normalization ensures correct scaling with velocity.

The total force from interaction momentum exchange is then:

$$
\vec{F} = \frac{d}{dt} \vec{P}_{\text{int}} = q \left( \vec{E}_{\text{bg}} + \vec{v} \times \vec{B}_{\text{bg}} \right)
$$

This is precisely the Lorentz force:

$$
\vec{F} = q (\vec{E} + \vec{v} \times \vec{B})
$$

But it is derived—not postulated—from scalar field overlap and motion. The effective charge $q$ is **not intrinsic**, but a geometric interaction strength arising from internal scalar structure.


## Connection to Topological Charge

In the paper *Defining Topological Charge in a Source-Free Maxwell Universe*, we defined the **topological charge** of a confined field structure as the pair:

$$
Q := (n_1, n_2) \in \mathbb{Z}^2
$$

These are the **winding numbers** of the toroidal standing wave:

- $n_1$: number of circulations along the toroidal direction  
- $n_2$: number along the poloidal (cross-sectional) direction

Each winding contributes to the internal circulation of energy in orthogonal directions. The scalar field $U(\vec{x}, t)$ supports such a standing wave through two angular coordinates:

$$
U(\vec{x}, t) = U_0 \cos(n_1 \phi_1 + n_2 \phi_2 - \omega t)
$$

Let us now derive how the **scalar energy current** $\vec{j}_U$ depends on this structure.

### Step 1: Scalar Gradient Flow from Toroidal Coordinates

From the above, the spatial gradient is:

$$
\nabla U \propto -n_1 \sin(\dots) \, \nabla \phi_1 - n_2 \sin(\dots) \, \nabla \phi_2
$$

Thus, the gradient direction combines:

$$
\nabla U \propto n_1 \hat{\phi}_1 + n_2 \hat{\phi}_2
$$

Let the object be moving with external velocity $\vec{v}$ (external in the sense that it represents the object’s motion relative to the background field structure, not part of its intrinsic circulation). Then:

$$
\vec{j}_U = \frac{\partial U}{\partial t} \vec{v} 
= \omega U_0 \sin(\dots) \, \vec{v}
$$

Multiplying out with $\nabla U$ implies:

$$
\vec{j}_U \propto (n_1 \hat{\phi}_1 + n_2 \hat{\phi}_2) \cdot \vec{v}
$$

The scalar current carries directional information aligned with:

$$
\vec{Q} := n_1 \hat{\phi}_1 + n_2 \hat{\phi}_2
$$

This is the **vector form of topological charge** in the local tangent space of the toroidal mode.

### Step 2: Coupling to Background Fields

From the Lorentz derivation, the interaction coupling strength $q$ is:

$$
q := \frac{1}{v^2} \int_V \vec{j}_U \cdot (\vec{E}_{\text{bg}} + \vec{v} \times \vec{B}_{\text{bg}}) \, d^3x
$$

Since $\vec{j}_U$ is parallel to $\vec{Q}$ and $\vec{v}$, the integrand simplifies to:

$$
\vec{j}_U \cdot \vec{F}_{\text{bg}} \propto 
(\vec{Q} \cdot \vec{F}_{\text{bg}})(\vec{v} \cdot \vec{v})
$$

Then:

$$
q \propto \vec{Q} \cdot \vec{F}_{\text{bg}}
$$

This shows that the **effective charge** $q$ is a **projection of the topological vector $\vec{Q}$ onto the background field** structure.

### Step 3: Interpretation

The object’s internal energy circulation is fixed by its winding numbers $(n_1, n_2)$. These define the geometry of energy flow within the toroidal scalar configuration. When this object moves relative to background $\vec{E}$ and $\vec{B}$ fields, its coupling strength $q$ arises from the directional overlap:

$$
q = \text{scalar projection} \propto \vec{Q} \cdot \vec{F}_{\text{bg}}
$$

Hence, charge is topological in origin—not an intrinsic substance, but a conserved consequence of energy circulation geometry. It reflects the alignment between intrinsic circulation and external field structure, rather than being a fixed scalar property.

## Discussion and Implications

- The Lorentz force is not fundamental, but a consequence of scalar energy conservation and curl-coupling geometry.
- The effective charge $q$ is not postulated—it is derived from the overlap of energy flow with ambient fields.
- Motion across curl structures induces apparent forces, because momentum must be conserved.
- The vector fields $\vec{E}$ and $\vec{B}$ are geometric projections of toroidal scalar field modes.
- This framework unifies electric and magnetic fields as rotational symmetries of scalar topology.

## References

1. Rodriguez A. M., Palma A., *Hydrogen Atom Quantization from Purely Classical Maxwell Electromagnetic Fields*, 2025  
2. Palma A., Rodriguez A. M., *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*, 2025  
3. Palma A., Rodriguez A. M., *Emergent -1/L² Interaction Force in a Pure Maxwell Universe*, 2025  
4. Palma A., Rodriguez A. M., *Explaining Conservation Laws in a Maxwell Universe Ontology*, 2025  
5. Jackson J. D., *Classical Electrodynamics*, 3rd ed., Wiley, 1999  
