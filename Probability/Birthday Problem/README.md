# Birthday Problem

This mini-project explores the classic **Birthday Problem**:

> How many people need to be in a room before there is at least a 50% probability that at least two people share a birthday?

The result shows that the probability **first exceeds 50%**  when there are **23 people** in the room.

---

## Method

The calculation uses the complement rule:

```
P(at least 2 people share a birthday) = 1 - P(no one shares a birthday)
P(no shared birthdays) = 365! / ((365 - n)! × 365ⁿ)

Where n is the number of people
365 being the number of days in a year and therefore number of possible birthday (ignoring leap years)
The script calculates the probability from 1 to a chosen value of n then plots the probability curve
```

## Features
```
- Calculates the probaility that at atleast two people share a birthday
- Finds the minimum value of n where the probabilty exceeds 50%
- Plots the probability against the number of people
- The 50% line is hihglighted
- The first crossing point over 50% is also marked on the graph for clarity
```

## Output
```
- Minimum number of people required is: 23
  - When n is 22, the Probability of more than two people are sharing a birthday: 0.4756953076625501
  - When n is 23, the Probability of more than two people are sharing a birthday: 0.5072972343239854
  - When n is 24, the Probability of more than two people are sharing a birthday: 0.5383442579145288
 ```

## How to Run
```
- Install matplotlib (requirement for the plotting function)
- Run the script
```

# Notes:
```
Project was created as part of my probability and mathematical modelling practice. It reinforced:
- Complementary probability
- Factorial based counting
- Translating maths into code
- Plotting and interpreting probabilty curves
```
