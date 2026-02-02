reast Cancer Dataset (Binary Classification)

More features ≠ better models.

In this project, I used a Genetic Algorithm (GA) to automatically select the most informative feature subset for a Decision Tree classifier, instead of training on all features blindly.

The objective was to maximize performance while minimizing feature redundancy.

This work treats feature selection as an optimization problem, not a greedy preprocessing step — which is especially important for Decision Trees, as they are highly sensitive to irrelevant features.

✔️ GA-selected features lead to cleaner splits, reduced tree depth, and better generalization.



🔍Feature selection is essential because it:

Reduces overfitting by removing noisy and redundant features

Improves accuracy, recall, and generalization

Produces faster, smaller, and more interpretable models



🧬 How the Genetic Algorithm Is Implemented



1️⃣ Chromosome Representation

Binary vector where each bit represents a feature

(1 = selected, 0 = ignored), ensuring at least one feature is always selected.

2️⃣ Initial Population

Randomly generated feature masks to ensure diversity.

Optionally fixed to allow fair comparison across experiments.

3️⃣ Fitness (Objective) Function

Multi-objective fitness:

0.6 × Accuracy − 0.1 × Feature Ratio + 0.3 × Recall

This balances performance, penalizes large feature sets, and prioritizes recall — a critical metric for medical datasets.

4️⃣ Selection Strategies

Tournament Selection: favors strong individuals while maintaining diversity

Roulette Wheel: selection probability proportional to fitness

Rank-Based Selection: relies on relative ranking, not raw fitness values

5️⃣ Crossover Techniques

Single-point crossover: swaps feature segments

Two-point crossover: exchanges middle segments

Uniform crossover: randomly mixes features from both parents

These strategies enable effective exploration of new feature interactions.

6️⃣ Mutation Strategy

Population-level mutation probability

Gene-level bit flipping

Prevents premature convergence and preserves population diversity.

7️⃣ Elitism

The best global feature subset is preserved every generation, ensuring no loss of the best solution found so far and guaranteeing stable convergence.



🏆 Best GA Configuration (From Experiments)

Tournament selection + Uniform crossover + Moderate mutation + Elitism

→ Stable convergence, compact feature sets, and improved Decision Tree performance.



🎯 Convergence & Evaluation

GA stops when fitness stabilizes across generations, ensuring a balance between exploration and exploitation.

The GA successfully discovered feature interactions that traditional filter methods often miss.
