---
type: cp
---

# Algebraic Equations

> **Definition** - Algebraic Equations
> equations that do not involve derivatives  
> With 1 variable They can *all* be written in the form 
> $$
> f(x) = 0
> $$
> With $N$ unkowns, we need $N$ equations. Define the vector of variables $x_i = \vec x$,so 
> $$
> f_i(\vec x) =0, ~ \vec f( \vec x)=0 
> $$
>{.is-info}

> eventually, these all reduce to root finding problems 
>{.is-warning}



# linear equations



## $N=1$
No higher powers than $x^1$ (i.e. $f(x)$ could be a polynomial). Generally, $f(x) = Ax-b = 0$. this is trivial to solve. 

$Ax = b, ~ x = \frac{b}{A}= b A^{-1}$,


## $N>1$

We simply have a matrix equation to solve $A \vec{x}=\vec{b}$. To solve for $\vec{x}$, we need to invert $A$, such that $\vec{x}=A^{-1} \vec{b}$. That means algebraic equtions boil down to:
- explicitly finding the inverse $A^{-1}$, OR
- solve for $\vec{x}$ [[Direct Methods.md|directly]] (usually faster)

> **Example** - finding $A^{-1}$ using vectors.
> 
> Suppose that there are 2 equations for $A$ ($A$ not necessarily 2x2)?, such that 
> 
> $$
> A \vec{x}_1=\vec{b} \quad A \vec{x}_2=\vec{c}
> $$
> 
> We can combine these equations to form a matrix of the $\vec{x}_i$ on the LHS and a matrix of $\vec{b}$ and $\vec{c}$ on the RHS, so 
> $$
> A\left(\vec{x}_1 \vec{x}_2\right)=(\vec{b} ~\vec{c})
> $$
> With $N$ ND vectors this generalises to 
> $$
> A\left(\vec{x}_1 \vec{x}_2 \ldots \vec{x}_N\right)=AX=\left(\vec{b}_1 \vec{b}_2 \ldots \vec{b}_N\right)
> $$
> 
> To find $A^{-1}$, we can simply set $\left(\vec{b}_1 \vec{b}_2 \ldots \vec{b}_N\right) = \mathbb{I}$. that means by defintion, 
> 
> $$
> A \cdot X=\mathbb{I}=A\cdot A^{-1}
> $$
> 
> So by constructing $X$, we obtain $A^{-1}$ ! 
> 
> We effectively have $N^2$ equations, so we can find every element of $A$ hence $A^{-1}$.
> 
> Of course this is (at least) $N$ times slower than just finding $\vec x$ as you need to find each of the $N$ columns, compared to just solving one of the $A \vec{x}_i=\vec{b}_i$.
> 


### eigenvalues (come back tomorrow)