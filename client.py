"""Shapley Value Coalitional Game Attribution Engine.
100% Python Standard Library.
"""

import itertools

class ShapleyAttribution:
    """Computes exact Shapley values satisfying efficiency, symmetry, and dummy player axioms."""
    @staticmethod
    def compute_shapley_values(players, value_function):
        shapley = {p: 0.0 for p in players}
        perms = list(itertools.permutations(players))
        num_perms = len(perms)
        
        for perm in perms:
            coalition = set()
            for p in perm:
                v_before = value_function(coalition)
                coalition.add(p)
                v_after = value_function(coalition)
                shapley[p] += (v_after - v_before)
                
        for p in players:
            shapley[p] = round(shapley[p] / num_perms, 5)
            
        return shapley
