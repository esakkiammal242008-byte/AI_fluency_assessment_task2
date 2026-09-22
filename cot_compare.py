from config import client, MODEL


QUESTIONS = [
    "Three courses cost ₹12,000, ₹18,000, and ₹15,000. "
    "A 15% scholarship is applied to the total fee, and the remaining "
    "amount is divided into 4 equal instalments. "
    "What is the amount of each instalment?",

    "A computer lab has 18 computers. In the morning, each computer is "
    "used by 2 students, and in the afternoon, each computer is used by "
    "3 students. How many student sittings are available in one day?",

    "Ravi is taller than Kumar, Kumar is taller than Arun, and Priya "
    "is shorter than Arun. Who is the tallest and who is the shortest?"
]


def ask_model(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def direct_prompt(question):
    prompt = f"""
Answer the following question directly.

Give only the final answer with a short explanation.

Question:
{question}
"""

    return ask_model(prompt)


def chain_of_thought(question):
    prompt = f"""
Solve the following question carefully.

Reason through the problem step by step.
Show the important calculation or logical steps.
At the end, write the final answer clearly.

Question:
{question}
"""

    return ask_model(prompt)


if __name__ == "__main__":

    print("=" * 70)
    print("DIRECT PROMPTING vs CHAIN-OF-THOUGHT")
    print("=" * 70)

    for i, question in enumerate(QUESTIONS, start=1):

        print(f"\n\nQUESTION {i}")
        print("-" * 70)
        print(question)

        print("\n[DIRECT PROMPTING]")
        direct_answer = direct_prompt(question)
        print(direct_answer)

        print("\n[CHAIN-OF-THOUGHT]")
        cot_answer = chain_of_thought(question)
        print(cot_answer)