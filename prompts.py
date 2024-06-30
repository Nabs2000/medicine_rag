from llama_index.core.prompts import PromptTemplate


instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. ONLY USE THE TOOLS PROVIDED TO YOU.
    5. PRINT ONLY THE EXPRESSION.
    6. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `medicines`.
    This is the result of `print(medicines.head())`:
    {medicines_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about statistics and details about a medicine. """
