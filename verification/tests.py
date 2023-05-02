"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['V', 'V', 'V', 'V', 'V', 'V']],
            "answer": 1
        },
        {
            "input": [['V', 'V', 'V', 'V', 'P', 'P']],
            "answer": 2
        },
        {
            "input": [['V', 'V', 'P', 'P', 'P', 'P']],
            "answer": 3
        }
    ],
    "Extra": [
        {
            "input": [['P', 'P', 'P', 'P', 'P', 'P']],
            "answer": -1
        },
    ]
}
