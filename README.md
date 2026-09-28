# Shapley Value Cooperative Game Attribution Skill

Axiomatically unique payoff allocation and feature importance engine based on coalitional marginal contribution averaging.

```mermaid
flowchart LR
    Players["Players / Features {1, ..., n}"] --> Permutations["Enumerate All n! Permutations"]
    Permutations --> Marginals["Calculate Marginal Contribution: v(S ∪ {i}) - v(S)"]
    Marginals --> Average["Uniform Expectation over Orders"]
    Average --> Shapley["Exact Shapley Value φ_i"]
```

## Features
- **100% Python Standard Library**: Exact permutation evaluation.
- **Axiomatic Fairness**: Strictly satisfies Efficiency, Symmetry, Additivity, and Null Player axioms.
- **Universal Application**: Powers team profit division, cost sharing, and machine learning feature attribution.
