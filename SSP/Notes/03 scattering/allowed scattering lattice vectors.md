---
type: ssp
---


# allowed scattering lattice vectors ($\vec{G}$)

Consider a plane wave propagating and being scattered by the lattice

![](2022-10-11-15-19-10.png)

We define the origin of the lattice at $O$ and the vector $\vec{R}$ between the planes. The incoming and outgoing waves are characterised by $\vec{k}_\text{in}$ and $\vec{k}_\text{out}$.


Since the bottom ray has travelled a longer the bottom ray, there is a phase difference between them, $\Delta \varphi=\dfrac{2 \pi}{\lambda}\left(d+d^{\prime}\right)$.


The diffracted ray now has a phase, such that at $\vec{R}$ 

$$
\left\{\begin{array}{l}
\text { in: } e^{i \vec{k}_{\text {in}} \cdot \vec{R}+i \varphi} \\
\text { out }: e^{i \vec{k}_{\text {out}} \cdot \vec{R}+i\varphi+i \Delta \varphi}
\end{array}\right.
$$

We find the distance $d$ and $d ^{\prime}$ Using $\vec{k}_\text{in}$ and $\vec{k}_\text{out}$, by finding the projection onto the ray path,

$$
d=\frac{\vec{k}_{\text {in }} \cdot \vec{R}}{|\vec{k}_{\text {in }}|} \quad d=-\frac{\vec{k}_{\text {out}} \cdot \vec{R}}{\left|\vec{k}_\text {out}\right|}.
$$

Subbing this into $\Delta \varphi$

$$
\Delta \varphi =( \vec{k}_\text { in }-\vec{k}_ \text { out }) \cdot \vec{R} = -\vec{q}\cdot \vec{R}
$$

Where we have used the fact that $\left|\vec{k}_\text {in}\right|=\left|\vec{k}_\text {out}\right| = \dfrac{2\pi}{\lambda}$. This gives us a closed form for the phase change in terms of the lattice vector $\vec{q}$. We require $\Delta \phi = 2\pi m$ for constructive interference ($e^{- i\vec{q}\cdot \vec{R}} = 1$). This gives use the defining property of lattice vectors 

> The defining property of scattered reciprocal lattice vectors $\vec{G}$ is that for lattice sites $\vec{R}$,
> $$
> e^{i \mathbf{G} \cdot \mathbf{R}}=1 \quad \text { for all lattice points } \mathbf{R} \text {in the real-space lattice.}
> $$
>{.is-warning}


For constructive interference, we require (see [[elastic scattering]]) $\exp{i \vec{k}\cdot \vec{r}} = 1$, which means that $\vec{q}$ must be a reciprocal lattice vector


## Equivalence to Bragg's law
Consider the previous derivation for [[elastic scattering.md| Laue condition]], that $2 \vec{k}_{\text {in }} \cdot \vec{G}+\vec{G}^2 = 0$. If we expand out the dot product,

$$
2|\vec{k}_\text{in}||\vec{G}| \sin \theta+|\vec{G}|^2=0
$$

Cancelling one of the $|\vec{G}|$, and using the definitions $\left|\vec{k}_\text {in}\right| = \dfrac{2\pi}{\lambda}$ and $\left|\vec{G}\right| = m\dfrac{2\pi}{a}$, we get

$$
2 \cdot \frac{2 \pi}{\lambda} \sin \theta+m \frac{2 \pi}{d}=0, ~ 2d \sin \theta = m \lambda
$$

where we dropped the - sign because $m$ is *any* integer.


## methods to see diffraction
- **Laue method**: fix $\theta$ and vary $\lambda$ (obselete)
- **Rotating Crystal**: fix $\lambda$ and vary $\theta$
- **Powder Method**: vary crystal planes. Pulvarise it so lots of planes point in one direction. This essentially lets the crystal be at any angle, so we can map the entire Ewald sphere.
