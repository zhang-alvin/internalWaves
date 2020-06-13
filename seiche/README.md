For this case, there is an assumption that there is a standing wave at the surface of the basin. 
The top-boundary condition, however, is not the true surface. 
It is instead, at some depth larger than the wave amplitude below the surface.
This allows us to more accurately prescribe the boundary and initial conditions.
The issue is in the event of mixing, the mixing might propagate up to the boundary which would no longer be an accurate condition.
  
For reference, how the pressure and velocity conditions vary with depth initially

<!--[comment]: <> https://alexanderrodin.com/github-latex-markdown/?math=%24p%3Dp_%7Ba%7D%2B%7B%5Crho_1%7DgA(H-y)%2B2%7B%5Crho_1%7Dg%5Cfrac%7Bcosh(%5Ckappa%20y)%7D%7Bcosh(%5Ckappa%20H)%7Dsin(%5Ckappa%20x)sin(%5Comega%20t)%24
[comment]: <> $p=p_{a}+{\rho_1}gA(H-y)+2{\rho_1}g\frac{cosh(\kappa y)}{cosh(\kappa H)}sin(\kappa x)sin(\omega t)$
[comment]: <> $u=2\omega A \frac{cosh(\kappa y)}{sinh(\kappa H)}sin(\kappa x)sin(\omega t)$ 
[comment]: <> $v=2\omega A \frac{sinh(\kappa y)}{sinh(\kappa H)}sin(\kappa x)cos(\omega t)$
-->


![$p=p_{a}+{\rho_1}gA(H-y)+2{\rho_1}g\frac{cosh(\kappa y)}{cosh(\kappa H)}sin(\kappa x)sin(\omega t)$](https://render.githubusercontent.com/render/math?math=%24p%3Dp_%7Ba%7D%2B%7B%5Crho_1%7DgA(H-y)%2B2%7B%5Crho_1%7Dg%5Cfrac%7Bcosh(%5Ckappa%20y)%7D%7Bcosh(%5Ckappa%20H)%7Dsin(%5Ckappa%20x)sin(%5Comega%20t)%24)

![$u=2\omega A \frac{cosh(\kappa y)}{sinh(\kappa H)}sin(\kappa x)sin(\omega t)$](https://render.githubusercontent.com/render/math?math=%24u%3D2%5Comega%20A%20%5Cfrac%7Bcosh(%5Ckappa%20y)%7D%7Bsinh(%5Ckappa%20H)%7Dsin(%5Ckappa%20x)sin(%5Comega%20t)%24)

![$v=2\omega A \frac{sinh(\kappa y)}{sinh(\kappa H)}sin(\kappa x)cos(\omega t)$](https://render.githubusercontent.com/render/math?math=%24v%3D2%5Comega%20A%20%5Cfrac%7Bsinh(%5Ckappa%20y)%7D%7Bsinh(%5Ckappa%20H)%7Dsin(%5Ckappa%20x)cos(%5Comega%20t)%24)
