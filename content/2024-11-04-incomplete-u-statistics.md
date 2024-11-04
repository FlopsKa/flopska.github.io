Title: Notes on the limiting distribution of incomplete U-statistics
Date: 2024-11-04
Tags: statistics; notes

<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css"
      crossorigin="anonymous">

The main results on the limiting distributions of incomplete U-statistics were developed in Blom (1976)[^blom1976incomplete] and Janson (1984)[^janson1984incomplete]; Lee (1990)[^lee1990ustats] gives a summary. However, for my taste, the proofs in Janson (1984) are somewhat hard to read. Lee (1990) improves upon those but has some inaccuracies---the main one being that $\theta$ is missing---, which we will address below. Nevertheless, his stated result seems correct.

## Notations

Let $N=\binom{n}{k}$, $h : \R^k \to \R$ a symmetric measurable function, and
$$
\begin{align}
U_n = N^{-1}\sum_{(n,k)}h(S),
\end{align}
$$
where the index $(n,k)$ denotes summation over all $N$ permutations of $m$ elements of a sample $\left(X_i\right)_{i=1}^n \sim P^n$, that is $S=\left(X_{i_1},\ldots,X_{i_m}\right)$ (we hide the dependence on the summation's index). $U_n$ estimates the parameter $\theta(P) =: \theta =\E h\left(X_1,\ldots,X_k\right)$, that is, $\E U_n = \theta$. Define, for $c=1,\ldots,k$, $h_c(x_1,\ldots,x_c) = \E h\left(x_1,\ldots,x_c,X_{c+1},\ldots,X_k\right)$, $\sigma_c^2 = \Var(h_c)$, and $\sigma_0^2=0$. $h$ is $d$-degenerate if $0=\sigma_1^2=\cdots =\sigma_d^2<\sigma_{d+1}^2$.
We call a statistic of the form
$$U_n' =m^{-1}\sum_{S\in\mathcal D}h(S),$$
where $\mathcal D$ is some (suitably chosen) subset of the $(n,k)$ sets in (1) with cardinality $m$ an *incomplete U-statistic*.

In this post, we will consider $m$ randomly chosen (with replacement) subsets of $(n,k)$. Letting $(Z_S)_{i=1}^{N}\sim\mathrm{Mult}(m;\frac1N,\ldots,\frac1N)$, we can write this incomplete U-statistic as
$$
\begin{align}
U_{n,m}' = m^{-1}\sum_{(n,k)}Z_Sh(S).
\end{align}
$$.


## Limit distribution of sampling with replacement

The following is Theorem 1(ii) (p. 200; Lee, 1990), which is a restatement of Corollary 1 (Janson, 1984).

__Theorem 1.__ Let $U_n$ and $U_{n,m}'$ be as in (1) and (2), respectively, with $h$ of degeneracy $d$. Define $\alpha = \lim_{n,m\to\infty}n^{d+1}m^{-1}$, and assume all necessary variances exist. If $0<\alpha<\infty$ then
$$m^{1/2}(U_{n,m}'-\theta) \to^d\alpha^{1/2}X+\sigma_kY,$$
where $X$ has distribution such that $n^{(d+1)/2}(U_n-\theta) \to^dX$, $Y\sim\mathcal N(0,1)$, and $X$ and $Y$ are independent.

The following proof is as in Lee (1990) with minor corrections.

_Proof._ Recall that pointwise convergence of characteristic functions (c.f.s) implies distributional ("$\to^d$") convergence.

Let $\phi_{n,m}$ be the c.f. of $m^{1/2}(U_{n,m}'-\theta)$ and $\phi$ the limiting c.f. of $n^{(d+1)/2}(U_n-\theta)$. We will show that $\phi_{n,m}(t) \to \phi(t)e^{-t^2\sigma_k^2/2}$ for $n,m\to\infty$; the latter factor is the c.f. of $\sigma_kY$. One has that
$$\begin{align*}
\phi_{n,m}(t) &= \E\exp\left(it\;m^{1/2}\left(U_{n,m}'-\theta\right)\right) \\
&\stackrel{(a)}{=} \E\exp\left(it\;m^{-1/2}\sum Z_S\left(h(S)-\theta\right)\right) \\
&= \E\E\left[\exp\left(it\;m^{-1/2}\sum Z_S\left(h(S)-\theta\right)\right)\Big|X_1,\ldots,X_n\right] \\
&\stackrel{(b)}{=} \E\exp\left(it\;m^{1/2}(U_n-\theta)\right)\times \\
&\quad \times \E\E\left[it\;m^{-1/2}\left(\sum Z_S(h(S)-\theta)-m(U_n-\theta)\right)\Big|X_1,\ldots,X_n\right] \\
&\stackrel{(c)}{=} \E\exp\left(it\;m^{1/2}(U_n-\theta)\right)\times \\
&\quad \times \E\E\left[it\;m^{-1/2}\sum \left(Z_S-\frac mN\right)\left(h(S)-\theta\right)\Big|X_1,\ldots,X_n\right] \\
\end{align*}$$
The details are as follows. In (a), we use that $m^{-1}\sum Z_S=1$ and reorder. $\pm m(U_n-\theta)$ and independence yields (b). (c) is by (1).

By Lemma A (p. 201; Lee, 1990) the conditional expectation converges in distribution to $\mathcal N(0,\sigma_k^2)$ for $m,n\to\infty$. One has that
$$\begin{align*}
\lim_{n,m\to\infty}\phi_{n,m}(t) &= \lim_{n\to\infty}\E\exp\left(it\;m^{1/2}(U_n-\theta)\right)e^{-t^2\sigma_k^2/2} \\
&=  \lim_{n\to\infty}\E\exp\left(it\;m^{1/2}n^{-(d+1)/2}n^{(d+1)/2}(U_n-\theta)\right)e^{-t^2\sigma_k^2/2} \\
&= \phi\left(\alpha^{-1/2}\right)e^{-t^2\sigma_k^2/2},
\end{align*}$$
where we used the assumptions in the last equality. The result is the c.f. of a random variable with the stated limit, concluding the proof.

## References

[^blom1976incomplete]: Blom, G. (1976). Some properties of incomplete U-statistics. Biometrika, 63(3), 573-580.
[^janson1984incomplete]: Janson, S. (1984). The asymptotic distributions of incomplete U-statistics. Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete, 66(4), 495-505.
[^lee1990ustats]: Lee, A. J. $U$-statistics. Theory and practice. Statistics: Textbooks and Monographs, 110. Marcel Dekker, Inc., New York, 1990.
