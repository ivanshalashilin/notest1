---
type: cp
---

# Natural Units

Making variables O(1) so that it is centered on the range of [[numbers.md|real numbers]], so you're less likely to go out of range. The natural units give you a scale for the sort of range to solve the DE between.


> **Example** - decay equation.
> Consider a decay equation with a source term such that $\frac{d u}{d t}+\alpha u=g$.
> We have 3 fixed values: $\alpha$ $g$ and $u(0)$. In the case when $g=0$, we get the standard decay equation,
> $$
> \frac{d u}{d t}=-\alpha u \quad \rightarrow u(t)=u(0) e^{-\alpha t}
> $$
> The solution $\Rightarrow ~ \alpha = \dfrac{1}{\text{Lifetime}}$, so $\alpha$ is a measure of the timescale of the solution. In this case we want to iterate between $t \sim  O\left(\dfrac{1}{\alpha}\right) \rightarrow  O\left(\dfrac{10}{\alpha}\right)$. This is a problem, because we are not in the $O(1)$ range that is the range of the most accurate [[numbers.md|real numbers]].
> For this, define *dimensionless time* : $\hat{t} = \alpha t$. The values are all scaled up, so now are range is 
> Another way would be to scale $t$, such that $\hat{t} = \alpha t$. This means $t \sim  O\left(1\right) \rightarrow  O\left(10\right)$.
> 
> Assuming now $g \neq 0$, that physcially corresponds to a source term. We eventually reach a steady state where $\dfrac{du}{d\hat{t}}=0$, at this point $u(\infty) = \dfrac{g}{\alpha}$. We therefore define another scaling, $\hat u = \dfrac{u}{u(\infty)}=\dfrac{\alpha u}{g}$, which has the same effect as with $\hat t$.
> 
> This also permits us to generalise to different $\alpha$ and $g$.


> When doing a plot of results:
> - scale back into the natural units (move away from centre range), OR
> - state in the axes that the units are scaled 
>{.is-warning}
