# PersonWeightedAccessibilty
Accessibility Code (Python)

Calculating the accessibility is a way to measure the number of opportunities reachable in a specific time threshold. A person-weighted accessibility measure is the number of opportunities (jobs) at destinations reachable to the population at each origin. This index allows comparing the system-wide accessibility by a transit mode (Levinson et al., 2016). 

The cumulative opportunities of block $i$ is represented in Equation 1.

\begin{equation}
    \label{Equation 1}
    A_{i,T} = \sum_{j=1}^{J} P_j f(C_{ij})
\end{equation}


where $C_{ij}$ is the generalized travel cost from region $i$ to region $j$, and $f(C_{ij})$ is the impedance function which: 

\begin{equation}
    f(C_{ij}) = \begin{cases}
            1 & if \; C_{ij} \le T\\
            0 & otherwise
            \end{cases}
\end{equation*}


Person-weighted accessibility could be formulated as the Equation 2. 

\begin{equation}
    \label{Equation 2}
    A_{pw,T} = \frac{\sum_{i=1}^{I} A_{i,T} P_i}{\sum_{i=1}^{I} P_i}
\end{equation}

where $A_i$ is the opportunities of block $i$ to every other blocks reachable in time $T$, and $P_i$ is the population within region $i$. 

References:
Levinson, D. M., Giacomin, D., & Badsey-Ellis, A. (2016). Accessibility and the choice of network investments in the London Underground. Journal of Transport and Land Use, 9(1), 131-150.
