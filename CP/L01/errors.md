---
type: cp
---
# Errors

## Rounding Error

Occurs when there is non-zero remainder in a division

$$
\frac{5}{3}= 1 ~\text{r} ~ 2
$$

The computer might thing 5/3 = 1

With [[numbers.md|reals]], rounding is unavoidable, since they are rounded to the nearest representable value $\dfrac{Z}{2^N}$.


## Initial Condition errors

Error in defining the starting point in a calculation. $U(t_0)$ may diverge from intended solution, in particular for chaotic system

## Propagation error

Errors seen at the next step of the the calculation, **in absence of other errors**. The cumulative effect at each step of the calculation is the **inhereted error**

### Error stability
As we do calculation, there will be errors at each step. Stability depends on the types of equation and methods used. If the propagation error
- $\uparrow,$  the calcualtion is unstable
- $\downarrow,$ or constant, the calculation is stable.

> **Example** 
> - stable $x ^{\prime} = 1+ 0.5x$. error $\downarrow$ 
> - unstable $x ^{\prime} = 1+2x$. error $\uparrow$ 

# Truncation Error

Inaccuracy due to removing terms in an infinite series. Most built in functions are approximated via truncated Taylor series such that error is comparable to [[machine accuracy]]