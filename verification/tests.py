"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 4], [2, 6], [8, 10], [12, 19]],
            "answer": [[1, 6], [8, 10], [12, 19]]
        },
        {
            "input": [[1, 12], [2, 3], [4, 7]],
            "answer": [[1, 12]]
        }
    ],
    "Extra": [
        {
            "input": [[1, 4], [12, 19]],
            "answer": [[1, 4], [12, 19]]
        },
        {
            "input": [[2, 6], [6, 10], [10, 19]],
            "answer": [[2, 19]]
        }
    ]
}
