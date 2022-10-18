---
type: cp
---


# Taylor Series

Computers can only add subtract, multiply and divide. To calculate something like a sin, we require a taylor series.

The small deviation/shift from the point of expansion ($x-a \rightarrow h$) is the key thing in Taylor series (add why later), so 

$$
f(x+h)=\sum_{i=0}^{\infty} \frac{1}{i !} f^i(x) h^i.
$$

Computing all the infinite terms would take an infinite amount of time. We thus keep terms up to and including some $h^n$ ($n$th order),

$$
f(x+h)=\sum_{i=0}^n \frac{1}{i !} f^i(x) h^i+R_n(x, h)
$$

The remaining infinite terms $R_n(x,h)$ are called the **residual**, leading to a [[errors.md|truncation error]]. In general it is $\propto h^{n+1}$.

$R_n$ cannot be found exactly numerically, but its closed form exists and can be found using the mean value theorem,

$$
R_n(x, h)=\frac{1}{(n+1) !} f^{n+1}(\xi) h^{n+1}.
$$

where $x<\xi<x+h$. 



