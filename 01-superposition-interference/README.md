# Superposition & Interference
Seeing all of these experiments about quantum superposition and wave-interference (e.g., double-slit experiment) made me feel inclined to try some experimentation of my own, and what better way than coding?

## Question
How do superposition and interference affect a quantum system?

## Methodology
I used Google Cirq to simulate a quantum circuit while mainly working with the Hadamard (H) gate. Other gates, such as the Pauli-X (X) gate and the Pauli-Z (Z) gate, were used in tandem with the H gate. See the [glossary](/glossary.md) for the definition of a gate.

## General Circuit Structure
`8: ———[Gates]———M("m1")———`

## Experiment One
- Gates: H, then X
- Hypothesis: The results will approach a 50/50 split as the number of shots (see [glossary](/glossary.md)) increases
- Data:
    - 10 Shots: 0 = 4 and 1 = 6
    - 1000 Shots: 0 = 504 and 1 = 496
    - 100000 Shots: 0 = 50129 and 1 = 49871
- Conclusion: The split is roughly 50/50

## Experiment Two
- Gates: H, then X, then H
- Hypothesis: Only 1 will be measured in every shot
- Data: 
    - 10 Shots: 0 = 10 and 1 = 0
    - 1000 Shots: 0 = 1000 and 1 = 0
    - 100000 Shots: 0 = 100000 and 1 = 0
- Conclusion: Only 0 was measured in every shot **(I was wrong!)**

## Experiment Three
- Gates: H, then Z, then H
- Hypothesis: Only 0 will be measured in every shot
- Data:
    - 10 Shots: 0 = 0 and 1 = 10
    - 1000 Shots: 0 = 0 and 1 = 1000
    - 100000 Shots: 0 = 0 and 1 = 100000
- Conclusion: Only 1 was measured in every shot **(I was wrong!)**

## Summary of Results
| Experiment | Gates | Hypothesis | Result (100,000 shots) | Hypothesis correct? |
|------------|-------|------------|------------------------|---------------------|
| One   | H, X    | Roughly 50/50 as shots increase | 0 = 50129, 1 = 49871 | Yes |
| Two   | H, X, H | Only 1 measured                 | 0 = 100000, 1 = 0    | No  |
| Three | H, Z, H | Only 0 measured                 | 0 = 0, 1 = 100000    | No  |

## Applying Concepts + Explanation of Experiment Results
If you want more technical definitions of the jargon I'm using, please refer to the glossary!

To simplify the rest of this document, I will be using the following, non-standard terms:
- Outcomes: results you can measure, which are the 0 and 1 basis states (see [glossary](/glossary.md))
- Parts: the two pieces that come from a first H gate, each with an amplitude
- Routes: what each part sends to each outcome at a second H gate

To explain my findings, I will first try to explain the functionality of the gates:
- An H gate "splits" input into two parts with equal amplitudes (see [glossary](/glossary.md)); in other words, the qubit enters superposition (see [glossary](/glossary.md))
- An X gate swaps the amplitudes of the parts
- A Z gate flips the sign of the second part's amplitude

### For Experiment Two
In the second experiment, after the qubit (see [glossary](/glossary.md)) passes through the first H gate, its ground state (0) has been split into two parts with equal amplitudes. When those parts enter the X gate, their amplitudes swap, but remain the same since they were already equal! The second H gate in this scenario acts as the first one's inverse, "reversing" the split and thus "reverting" the qubit back to its ground state. That's why the only possible outcome is the 0 outcome.

### For Experiment Three
For clarity, let's look back at the circuit!
- The first H gate splits the qubit into two parts with equal amplitudes (0: +1/√2, 1: +1/√2)
- The Z gate flips the sign of second part's amplitude (now −1/√2), indicative of its relative phase (see [glossary](/glossary.md))
- The second H gate causes interference (see [glossary](/glossary.md)), allowing the Z gate to change the probabilities

When the Z gate flips the sign of the second part's amplitude, it sets up for what the second H gate will do, which redistributes each part (including their amplitudes) to both outcomes, these pieces being the routes.

| Outcomes  | From Part 1 (+1/√2) | From Part 2 (−1/√2) | Total |
|-----------|---------------------|---------------------|-------|
| Outcome 0 | +1/2                | −1/2                | 0     |
| Outcome 1 | +1/2                | +1/2                | 1     |

Each cell is the part’s amplitude times H’s factor, which is +1/√2 for every route except the one from part 2 into outcome 1, where it’s −1/√2 because it applies both a negative and positive factor.
- For outcome 0, the routes cancel out, and the total amplitude is 0
- For outcome 1, the routes add up, and the total amplitude is 1

An outcome's total amplitude affects its probability as per the Born rule (see [glossary](/glossary.md)). Therefore, the 0 outcome's total amplitude being 0 makes it an impossible outcome, leaving only outcome 1 to be measured.

TL;DR: The two routes into outcome 0 cancel completely, so only outcome 1 can be measured (see [glossary](/glossary.md) for superposition principle).