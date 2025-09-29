import re
# import ast
import os


path=os.getcwd()+"/output/result.dot"
class Cleaner :
    def __init__(self,path=None):
        pass
    def clean_dot_result():
        with open(path, 'r') as f:
            content = f.read()
        #  Remove ANSI escape codes (e.g., \x1b[33m, etc.)
        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        cleaned = ansi_escape.sub('', content)

        #  Extract the DOT content inside the triple quotes
        match = re.search(r'("""\[)(.*)(\]""")', cleaned, re.DOTALL)
        if match:
            dot_raw = match.group(2)

            # Remove surrounding quotes if present
            if dot_raw.strip().startswith('"') and dot_raw.strip().endswith('"'):
                dot_raw = dot_raw.strip()[1:-1]

            # Unescape `\n` and `\"`, and save as clean DOT file
            dot_str = dot_raw.encode('utf-8').decode('unicode_escape')  # Handles \n, \", etc.

            with open('cleaned_result.dot', 'w') as out:
                out.write(dot_str)

            print("✅ Clean DOT file written to cleaned_result.dot")

        else:
            print("❌ Could not find DOT graph content in the expected format.")

    @staticmethod
    def clean_content(content):
        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        cleaned = ansi_escape.sub('',content)
         #  Extract the DOT content inside the triple quotes
        match = re.search(r'("""\[)(.*)(\]""")', cleaned, re.DOTALL)
        if match:
            dot_raw = match.group(2)
            # Remove surrounding quotes if present
            if dot_raw.strip().startswith('"') and dot_raw.strip().endswith('"'):
                dot_raw = dot_raw.strip()[1:-1]
            # Unescape `\n` and `\"`, and save as clean DOT file
            dot_str = dot_raw.encode('utf-8').decode('unicode_escape')  # Handles \n, \", etc.
            # with open('cleaned_result.dot', 'w') as out:
            #     out.write(dot_str)
            return dot_str
        else:
            print("❌ Could not find DOT graph content in the expected format.")





# def clean(content):
#     ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
#     cleaned = ansi_escape.sub('',content)
#      #  Extract the DOT content inside the triple quotes
#     match = re.search(r'("""\[)(.*)(\]""")', cleaned, re.DOTALL)
#     if match:
#         dot_raw = match.group(2)
#         # Remove surrounding quotes if present
#         if dot_raw.strip().startswith('"') and dot_raw.strip().endswith('"'):
#             dot_raw = dot_raw.strip()[1:-1]
#         # Unescape `\n` and `\"`, and save as clean DOT file
#         dot_str = dot_raw.encode('utf-8').decode('unicode_escape')  # Handles \n, \", etc.
#         # with open('cleaned_result.dot', 'w') as out:
#         #     out.write(dot_str)
#         return dot_str
#     else:
#         print("❌ Could not find DOT graph content in the expected format.")

