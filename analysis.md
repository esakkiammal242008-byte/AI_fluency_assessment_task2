# Agentic AI: Reasoning and Acting

## Day 2 Task — Comparing Direct Prompting, Chain-of-Thought, and ReAct

---

## 1. Introduction

This project compares three approaches for solving AI problems:

1. Direct Prompting
2. Chain-of-Thought (CoT)
3. ReAct (Reasoning and Acting)

The experiment uses a **College Course Registration & Fee Assistant** scenario.

The purpose is to understand how the three approaches differ in reasoning depth, tool usage, reliability, transparency, speed/cost, and consistency.

---

# 2. Scenario

The scenario is based on college course registration and fee calculation.

The available courses and fees are:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

The scenario contains both calculation/reasoning questions and a question that requires external information through tools.

---

# 3. Direct Prompting

## Definition

Direct Prompting asks the model to answer a question directly using the information provided in the prompt.

It does not explicitly use external tools.

In this project, Direct Prompting was tested using three questions involving fee calculation, computer-lab capacity, and logical ordering.

### Example Question

Three courses cost ₹12,000, ₹18,000, and ₹15,000. A 15% scholarship is applied to the total fee, and the remaining amount is divided into 4 equal instalments.

### Result

Total fee:

₹12,000 + ₹18,000 + ₹15,000 = ₹45,000

Scholarship:

15% of ₹45,000 = ₹6,750

Remaining fee:

₹45,000 − ₹6,750 = ₹38,250

Each instalment:

₹38,250 ÷ 4 = **₹9,562.50**

The Direct Prompting approach produced the correct answer.

### Advantages

* Simple to implement.
* Fast for straightforward questions.
* Does not require tool integration.
* Suitable when the required information is already available in the prompt.

### Limitations

* Cannot independently retrieve unknown external information.
* Less suitable when a problem requires interaction with external tools or data.
* Complex multi-step tasks can be more difficult to verify.

---

# 4. Chain-of-Thought (CoT)

## Definition

Chain-of-Thought prompting asks the model to reason through a problem step by step before giving the final answer.

In this experiment, the model was explicitly instructed to solve the questions carefully and show the important calculation or logical steps.

## Example

For the course-fee question:

1. Calculate the total course fee.
2. Calculate the 15% scholarship.
3. Subtract the scholarship from the total.
4. Divide the remaining amount by four.

Final answer:

**₹9,562.50 per instalment**

The CoT approach also correctly solved the computer-lab and logical-ordering questions.

### Advantages

* Provides more detailed reasoning.
* Makes intermediate calculations easier to inspect.
* Useful for multi-step mathematical and logical problems.
* Can make errors easier to identify.

### Limitations

* Takes more output tokens than a direct answer.
* Can be slower than a short direct response.
* Does not automatically provide access to external information or tools.
* Detailed reasoning does not guarantee correctness.

---

# 5. ReAct

## Definition

ReAct combines reasoning with actions performed through external tools.

The general pattern used in this project is:

**Thought → Action → Observation → Thought → Action → Observation → Final Answer**

The ReAct experiment used two tools:

* `get_course_fee()` — retrieves the fee of a course.
* `calculator()` — performs calculations.

## ReAct Question

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

## ReAct Execution

### Step 1

**Thought:** I need the fee of CS101.

**Action:**
`get_course_fee("CS101")`

**Observation:**
₹12,000

### Step 2

**Thought:** I need the fee of AI202.

**Action:**
`get_course_fee("AI202")`

**Observation:**
₹18,000

### Step 3

**Thought:** I need the fee of DS303.

**Action:**
`get_course_fee("DS303")`

**Observation:**
₹15,000

### Step 4

Calculate the first option:

```text
(12000 + 18000) × 0.90
= 27000
```

**Observation:** ₹27,000

### Step 5

Calculate the second option:

```text
(12000 + 18000 + 15000) × 0.75
= 33750
```

**Observation:** ₹33,750

### Step 6

Compare the two options:

```text
33750 − 27000 = 6750
```

**Observation:** ₹6,750

### Final Result

**Option 1 is cheaper by ₹6,750.**

---

# 6. Comparison

| Criteria               | Direct Prompting              | Chain-of-Thought                | ReAct                                  |
| ---------------------- | ----------------------------- | ------------------------------- | -------------------------------------- |
| Reasoning depth        | Low to moderate               | Higher                          | High with actions                      |
| Tool usage             | No                            | No                              | Yes                                    |
| Multi-step reliability | Suitable for simple tasks     | Better for reasoning tasks      | Suitable when tools/data are required  |
| Transparency           | Short explanation             | Shows important reasoning steps | Shows Thought/Action/Observation trace |
| Speed/Cost             | Generally fastest             | More tokens/output              | Higher due to multiple tool calls      |
| Consistency            | High at temperature 0         | High at temperature 0           | Depends on tool execution and model    |
| External information   | Not available unless supplied | Not available unless supplied   | Can retrieve information through tools |

---

# 7. Self-Consistency Experiment

Self-consistency was tested using the course-fee instalment problem.

The same Chain-of-Thought question was run **5 times with temperature = 0.8**.

The expected mathematical answer was:

**₹9,562.50**

All five runs produced the same mathematical answer.

The script's simple answer-normalization step counted the canonical formatted answer as **4/5**, because one response used a different textual formatting even though its mathematical answer was the same.

Therefore, the experiment shows that the model was mathematically consistent across the five runs, while exact textual formatting varied.

## Temperature 0 Check

The same question was then run with:

**Temperature = 0**

The model produced the same correct mathematical answer.

Temperature 0 therefore produced a deterministic-style response for this experiment, subject to the model/API implementation.

---

# 8. Capabilities and Limitations

## Direct Prompting

Direct Prompting is useful when:

* The problem is simple.
* All required information is already provided.
* A short answer is sufficient.

Its main limitation is the lack of external tool access.

## Chain-of-Thought

CoT is useful when:

* The problem requires multiple reasoning steps.
* Intermediate calculations are useful.
* The user needs a more detailed solution.

Its limitation is that reasoning alone does not provide external information.

## ReAct

ReAct is useful when:

* The task requires external information.
* Calculations need reliable tool execution.
* Multiple actions are required.
* The process needs an observable tool-use trace.

Its limitations include additional tool calls, greater complexity, and potentially higher execution cost and latency.

---

# 9. Reliability

For the selected experiments:

* Direct Prompting produced correct answers for the tested questions.
* Chain-of-Thought produced correct answers for the tested questions.
* ReAct successfully retrieved all three course fees and performed the required calculations.
* Self-consistency produced the same mathematical answer across all five runs.

However, these results apply only to the selected scenario and test runs. They do not prove that one approach will always be more reliable for every problem.

---

# 10. Suitability of Each Approach

### Direct Prompting

Best suited for simple questions where the required information is already available.

### Chain-of-Thought

Best suited for problems requiring several reasoning or calculation steps.

### ReAct

Best suited for tasks that combine reasoning with external information retrieval, calculations, or other tool interactions.

---

# 11. Conclusion

The experiment demonstrates that the three approaches serve different purposes.

**Direct Prompting** provides a simple and efficient way to answer questions when the necessary information is already available.

**Chain-of-Thought** is useful for problems that require multiple reasoning steps and makes important intermediate steps easier to inspect.

**ReAct** extends reasoning by allowing the system to interact with tools. In the college course-registration scenario, the ReAct implementation retrieved course fees, performed calculations, compared the results, and generated the final answer.

Therefore, the appropriate approach depends on the task requirements:

* Use **Direct Prompting** for straightforward questions.
* Use **CoT** for multi-step reasoning and calculations.
* Use **ReAct** when reasoning needs to be combined with external information or tool use.

The self-consistency experiment also showed that repeated sampling can be used to examine answer consistency, while temperature affects variation between model responses.
