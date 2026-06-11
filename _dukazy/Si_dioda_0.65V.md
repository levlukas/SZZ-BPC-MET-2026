# Hodnota 0.65 V pro Si diodu

Ne konstanta, ale dusledek exponencialni VA charakteristiky (Shockley):

$$
I = I_S\left(e^{\frac{qV}{kT}}-1\right).
$$

Pri 300 K:

$$
\frac{kT}{q}\approx26\ \mathrm{mV},
\qquad
V=\frac{kT}{q}\ln\frac{I}{I_S}.
$$

Pro typicke $I_S$ a proudy v radu mA:

$$
V \approx 0.6{-}0.7\ \mathrm{V}.
$$

# Proudove mechanismy PN prechodu

- Drift (vliv elektrickeho pole):

$$
J_{\mathrm{drift}} = qn\mu E.
$$

- Difuze (gradient koncentrace):

$$
J_{\mathrm{dif}} = -qD\nabla n.
$$

Rovnovaha:

$$
J_{\mathrm{drift}} + J_{\mathrm{dif}} = 0.
$$

Propustna polarizace $\rightarrow$ snizeni potencialove bariery $\rightarrow$
prevaha difuze majoritnich nosicu $\rightarrow$
exponencialni rust proudu (Shockleyho rovnice).