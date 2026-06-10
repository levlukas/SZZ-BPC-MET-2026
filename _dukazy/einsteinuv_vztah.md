# "Odvozeni" Einsteinova vztahu
Nerigorozni odvozeni kompenzace difuze a driftu (pro diry):
- Fickuv zakon difuze: $J = - q D \nabla p$ 
- Drift: $J = qpv_d = qp\mu_p E$

Pro teple diry priblizne plati Boltzmannova distr.

$$ p \propto \exp\left( - \frac{q \phi}{kT} \right), $$

takze $\nabla p(\phi) = \text{konst.}\cdot \nabla \phi$ a $- \nabla \phi = E$. Odtud z derivace $p$ (gradient): 

$$ \nabla p = \nabla \exp\left( - \frac{q \phi}{kT} \right) = p\frac{-q\nabla\phi}{kT} = \frac{qpE}{kT}. $$

Po uprave rovnovahy obou $J$:
$$ J_{difuze} = J_{drift} $$
$$ qp\mu E = q D \nabla p $$
$$ qp\mu E = qD\frac{qpE}{kT} $$
$$ \mu  = \frac{qD}{kT} $$
To je Einsteinuv vztah $\frac{D}{\mu} = \frac{kT}{q}$ 
