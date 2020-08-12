Title: The Repertoire Method and the radix-based solution to the Josephus Problem
Date: 2020-07-31
Category: computer science

This post summarizes how one uses the repertoire method (as presented in Concrete Mathematics by Graham, Knuth and Patashnik). First we look at the repertoire method without the need for a radix-based solution and afterwards we discuss the solution given in the book for Exercise 16.

# General method

Suppose we are given the recursion

$
\begin{aligned}
T(0) &= \alpha \\
T(n) &= \beta n^2 + \gamma n + \delta + T(n-1).
\end{aligned}
$

Starting the recursion, we find that $T(n)$ is of the form $T(n) = \alpha A(n) + \beta B(n) + \gamma C(n) + \delta C(n)$ and we can use the repertoire method.

There a two ways to proceed: One is to guess values for the parameters and to find fitting functions for $A(n),B(n), C(n), D(n)$, the other one is to guess functions and to find fitting values for $\alpha,\beta,\gamma,\delta$. We proceed by guessing functions.

## Function guessing

The idea here is to guess functions of which a linear combination results in a closed form solution to the recurrence given above. We start by guessing that

$\begin{aligned}T(n) &= 1.\end{aligned}$

It follows that

$\begin{aligned}T(0) = \alpha = 1\end{aligned}$

and

$\begin{aligned}T(n) &= \beta n^2+\gamma n + \delta + T(n-1) \\
1 &= \beta n^2+\gamma n + \delta + 1.\end{aligned}$

By comparing the coefficients for all $n$ we see that $\beta=\gamma=\delta=0$. Hence, $A(n) = 1$.

From setting $T(n) = n$, we find that $(\alpha,\beta,\gamma,\delta) = (0,0,0,1)$. Hence, $D(n) = n$.

Setting $T(n) = n^2$ gives us $(\alpha,\beta,\gamma,\delta) = (0,0,2,-1)$. Hence,

$\begin{aligned}
n^2 &= 2C(n) - D(n) \\
    &= 2C(n) - n \\
C(n) &= \frac{n^2+n}{2}.
\end{aligned}
$

Finally, we set $T(n) = n^3$ and get $(\alpha,\beta,\gamma,\delta) = (0,3,-3,1)$. Hence,

$\begin{aligned}
n^3 &= 3 B(n) - 3 C(n) + D(n) \\
B(n) &= \frac 1 3 n^3 + \frac 1 2 n^2 + \frac 1 6 n,
\end{aligned}
$

solving our recurrence. Comparing the result with [this video](https://www.youtube.com/watch?v=8WbpRwYcEf0) we set $(\alpha,\beta,\gamma,\delta) = (7,2,0,7)$. This gives

$\begin{aligned}
T(n) &= 7 A(n)+ 2 B(n) + 0 C(n) + 7 D(n) \\
&= 7 + 2 \left( \frac 1 3 n^3 + \frac 1 2 n^2 + \frac 1 6 n\right) + 7 n \\
&= 7 + \frac 2 3 n^3 + n^2 + \frac{22}{3} n
\end{aligned}
$

as in the video.

# Radix-based solution

On page 16 the book states that a recurrence of the form

$\begin{aligned}
f(j) &= \alpha, \qquad\qquad\;\text{for } 1 \leq j < d; \\
f(dn + j) &= cf(n) + \beta_j \quad \text{for } 0 \leq j < d \text{ and } n \geq 1
\end{aligned}
$

has the radix-changing solution

$
f((b_m b_{m-1}\dots b_1 b_0)_d) = (\alpha_{b_m}\beta_{b_{m-1}}\beta_{b_{m-2}}\dots\beta_{b_1}\beta_{b_0})_c.
$

## Parameter guessing

Armed with this knowledge we can now solve exercies 1.16:

__1.16__ Use the repertoire method to solve the general four-parameter recurrence

$\begin{aligned}
g(1) &= \alpha \\
g(2n+j) &= 3g(n) + \gamma n + \beta_j, \quad \text{for } j = 0,1 \text{ and } n \geq 1.
\end{aligned}
$

_Hint:_ Try the function $g(n) = n$.

Let's start by using the hint given in the exercise. Using the same approach as before, setting $g(n) = n$ implies

$\begin{aligned}
g(1) &= 1 = \alpha \\
2n &= 3n + \gamma n + \beta_0 \\
2n + 1 &= 3n + \gamma n + \beta_1.
\end{aligned}
$

The values $(1,0,1,-1)$ for the parameters $(\alpha,\beta_0,\beta_1,\gamma)$ satisfy these equations for all n.

Thus $n = A(n) + C(n) - D(n)$.

Now, if we, by an educated guess, let $(\alpha,\beta_0,\beta_1,\gamma)$ be $(1,0,1,0)$ we get

$\begin{aligned}
g(1) &= 1 \\
g(2n) &= 3g(n) \\
g(2n+1) &= 3g(n) + 1.
\end{aligned}
$

This looks exactly like the recurrence to which we already know the solution and gives us $A(n), B(n)$ and $C(n)$.

Combining both results we find the closed form.