from collections import Counter

from config import client, MODEL


QUESTION = """
Three courses cost ₹12,000, ₹18,000, and ₹15,000.
A 15% scholarship is applied to the total fee, and the remaining
amount is divided into 4 equal instalments.
What is the amount of each instalment?
"""

RUNS = 5
TEMPERATURE = 0.8


def ask_cot(temperature):
    prompt = f"""
Solve this problem carefully.

Reason through the calculation step by step.
At the end, write a clear final answer.

Question:
{QUESTION}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("=" * 70)
    print("SELF-CONSISTENCY TEST")
    print("=" * 70)

    print("\nQuestion:")
    print(QUESTION)

    answers = []

    for i in range(1, RUNS + 1):

        print(f"\n--- RUN {i} ---")

        answer = ask_cot(TEMPERATURE)

        print(answer)

        answers.append(answer)

    # Extract the final numerical answer approximately
    normalized = []

    for answer in answers:
        if "9,562.50" in answer or "9562.50" in answer:
            normalized.append("₹9,562.50")
        else:
            normalized.append(answer)

    counts = Counter(normalized)

    print("\n" + "=" * 70)
    print("SELF-CONSISTENCY RESULT")
    print("=" * 70)

    print("\nAnswer counts:")

    for answer, count in counts.items():
        print(f"{answer}: {count}/{RUNS}")

    majority_answer, majority_count = counts.most_common(1)[0]

    print("\nMajority answer:", majority_answer)
    print("Majority count:", f"{majority_count}/{RUNS}")

    print("\n--- TEMPERATURE 0 CHECK ---")

    zero_answer = ask_cot(0)

    print(zero_answer)

    print("\nTemperature 0 produces a deterministic-style response for")
    print("the same prompt, subject to the model/API implementation.")