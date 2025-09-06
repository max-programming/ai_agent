import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

load_dotenv()

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or override files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    if len(sys.argv) < 2:
        print("No prompt provided")
        sys.exit(1)

    is_verbose = False

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        is_verbose = True

    prompt = sys.argv[1]

    max_iters = 20

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )
    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[available_functions],
    )

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for i in range(0, max_iters):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=config,
        )

        if response is None or response.usage_metadata is None:
            print("No response from the model")
            return

        if is_verbose:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, is_verbose)
                messages.append(function_call_result)
                # if function_call_result.parts[0].function_response is None:
                #     raise Exception("Function call result is None")
                # else:
                #     print(
                #         f"-> {function_call_result.parts[0].function_response.response}"
                #     )

        else:
            print(response.text)
            return


main()
