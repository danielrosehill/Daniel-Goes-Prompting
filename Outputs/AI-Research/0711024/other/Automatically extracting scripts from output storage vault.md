# Prompt

Within my Obsidian vault I have a lot of generated code snippets. I'm saving some of these outputs into a new vault that I'm sharing on Github. For every script that you generate, I'd like to copy it into a separate folder in my vault called /Scripts. Can you suggest a way to do this programatically? That is to say: I'd like to find a way to glob over my vault. Every time the program sees that there is a script there it should automatically copy it into the Scripts folder. It would need to be able to automatically detect the language and automatically detect where the script starts and ends and where the natural language around it starts and ends. Thinking this out, it's not such a simple task. Any existing programs for this or ideas for how to do it?

# Output

Extracting code snippets from markdown files in your Obsidian vault and organizing them into a separate `/Scripts` folder is a more complex task, but it can certainly be achieved programmatically with Python. Below, I’ll outline a potential approach and provide a sample script to get you started.

### Approach:

1. **File Traversal**: Use Python's `os` and `glob` libraries to traverse your Obsidian vault and find all markdown files.
2. **Detect Code Blocks**: Use regular expressions (regex) to identify code blocks within the markdown files. You can detect the start and end of code snippets based on the common markdown format for code blocks (e.g., triple backticks).
3. **Determine Language**: If specified, the language is typically indicated right after the opening backticks (e.g., ```python). You can extract this information for classification.
4. **Copy to Scripts Folder**: For each detected code block, copy the code into the `/Scripts` folder, creating a new file named according to the original file and a timestamp or incremental number to avoid name collisions.

### Sample Python Script:
Here’s a Python script to demonstrate this process:

```python
import os
import re
import glob
import shutil

# Define the base directory of your Obsidian vault and the target Scripts directory
vault_directory = "/path/to/your/obsidian/vault"
scripts_directory = os.path.join(vault_directory, "Scripts")

# Create the Scripts directory if it doesn't exist
os.makedirs(scripts_directory, exist_ok=True)

# Regex pattern to detect code blocks (with optional language)
code_block_pattern = re.compile(r'```(\w+)?\n(.*?)\n```', re.DOTALL)

# Traverse markdown files in the vault
for markdown_file in glob.glob(os.path.join(vault_directory, "*.md")):
    with open(markdown_file, 'r') as file:
        content = file.read()
    
    # Find all code blocks in the file
    matches = code_block_pattern.findall(content)
    
    for index, (language, code) in enumerate(matches):
        # Generate a filename for the script
        # You can customize the naming scheme as needed
        script_filename = f"{os.path.basename(markdown_file).replace('.md', '')}_script_{index + 1}.{language if language else 'txt'}"
        script_filepath = os.path.join(scripts_directory, script_filename)
        
        # Write the extracted code to a new file in the Scripts directory
        with open(script_filepath, 'w') as script_file:
            script_file.write(code.strip())

print(f"Scripts copied to '{scripts_directory}'.")
```

### Instructions to Run the Script:
1. **Adjust Paths**: Replace `/path/to/your/obsidian/vault` with the actual path to your Obsidian vault.
2. **Run the Script**: Save the script as a `.py` file and run it in your Python environment.

### Considerations:
- **Code Block Detection**: The regex captures language identifiers, and the code between the triple backticks. Adjust the regex if your markdown uses different formatting.
- **Error Handling**: You might want to add error handling to account for cases where the files can't be read or written.
- **File Naming**: Customize how the script generates filenames for the scripts based on your preferences to avoid overwriting existing files.
- **File Types**: This script assumes you're only working with `.md` files. Modify the `glob` pattern if your vault contains other formats.

### Existing Programs:
While there may not be off-the-shelf solutions that meet all your requirements, some markdown processing tools like **Pandoc** can help in parsing and converting markdown. However, they might not provide the specific extraction functionality you're looking for. For your needs, a custom script as outlined above will likely be the most flexible and effective solution.

Let me know if you need further modifications or assistance with the script!
# Input

Nice work. I think almost all the scripts would be Bash, Python, or Javascript. As a starter, could you update your script so that it covers those three languages at least?

# Output

Here’s the updated Python script that specifically handles code blocks in Bash, Python, and JavaScript. The script will create separate files for each detected code block, with appropriate file extensions based on the language.

### Updated Python Script:

```python
import os
import re
import glob

# Define the base directory of your Obsidian vault and the target Scripts directory
vault_directory = "/path/to/your/obsidian/vault"  # Update this path
scripts_directory = os.path.join(vault_directory, "Scripts")

# Create the Scripts directory if it doesn't exist
os.makedirs(scripts_directory, exist_ok=True)

# Regex pattern to detect code blocks (with optional language)
code_block_pattern = re.compile(r'```(bash|python|javascript)?\n(.*?)\n```', re.DOTALL)

# Traverse markdown files in the vault
for markdown_file in glob.glob(os.path.join(vault_directory, "*.md")):
    with open(markdown_file, 'r') as file:
        content = file.read()
    
    # Find all code blocks in the file
    matches = code_block_pattern.findall(content)
    
    for index, (language, code) in enumerate(matches):
        # Determine the file extension based on the language
        if language == 'bash':
            file_extension = 'sh'
        elif language == 'python':
            file_extension = 'py'
        elif language == 'javascript':
            file_extension = 'js'
        else:
            file_extension = 'txt'  # Fallback if no language is detected
        
        # Generate a filename for the script
        script_filename = f"{os.path.basename(markdown_file).replace('.md', '')}_script_{index + 1}.{file_extension}"
        script_filepath = os.path.join(scripts_directory, script_filename)
        
        # Write the extracted code to a new file in the Scripts directory
        with open(script_filepath, 'w') as script_file:
            script_file.write(code.strip())

print(f"Scripts copied to '{scripts_directory}'.")
```

### Key Changes:
- **Language Filtering**: The regex pattern now specifically captures code blocks marked as `bash`, `python`, or `javascript`.
- **File Extensions**: The script assigns appropriate file extensions (`.sh`, `.py`, or `.js`) based on the detected language.

### Instructions to Run the Script:
1. **Update the Path**: Replace `/path/to/your/obsidian/vault` with the actual path to your Obsidian vault.
2. **Run the Script**: Save the script as a `.py` file and run it in your Python environment.

This script will extract code snippets from your markdown files that are in Bash, Python, or JavaScript and save them to the `/Scripts` folder with the corresponding file extensions. Let me know if you need further modifications or additional features!

# Input

One more change. Sometimes I ask GPT to output to raw markdown, but I wouldn't want to include those. Could you explicitly exclude raw markdown in the program?

# Output

Here’s the updated Python script that explicitly excludes raw markdown outputs when copying code snippets to the `/Scripts` folder. To implement this, we'll modify the regex to avoid matching raw markdown blocks.

### Updated Python Script:

```python
import os
import re
import glob

# Define the base directory of your Obsidian vault and the target Scripts directory
vault_directory = "/path/to/your/obsidian/vault"  # Update this path
scripts_directory = os.path.join(vault_directory, "Scripts")

# Create the Scripts directory if it doesn't exist
os.makedirs(scripts_directory, exist_ok=True)

# Regex pattern to detect code blocks (with optional language)
# This will exclude raw markdown blocks by checking for specific formats
code_block_pattern = re.compile(r'```(bash|python|javascript)\n(.*?)\n```', re.DOTALL)

# Traverse markdown files in the vault
for markdown_file in glob.glob(os.path.join(vault_directory, "*.md")):
    with open(markdown_file, 'r') as file:
        content = file.read()
    
    # Find all code blocks in the file
    matches = code_block_pattern.findall(content)
    
    for index, (language, code) in enumerate(matches):
        # Determine the file extension based on the language
        if language == 'bash':
            file_extension = 'sh'
        elif language == 'python':
            file_extension = 'py'
        elif language == 'javascript':
            file_extension = 'js'
        else:
            file_extension = 'txt'  # Fallback if no language is detected
        
        # Generate a filename for the script
        script_filename = f"{os.path.basename(markdown_file).replace('.md', '')}_script_{index + 1}.{file_extension}"
        script_filepath = os.path.join(scripts_directory, script_filename)
        
        # Write the extracted code to a new file in the Scripts directory
        with open(script_filepath, 'w') as script_file:
            script_file.write(code.strip())

print(f"Scripts copied to '{scripts_directory}'.")
```

### Key Change:
- **Excluding Raw Markdown**: The regex pattern has been adjusted to only capture code blocks with specified languages (`bash`, `python`, or `javascript`). This will effectively exclude raw markdown blocks, which do not specify a language and are generally not wrapped with the specific language indicator.

### Instructions to Run the Script:
1. **Update the Path**: Replace `/path/to/your/obsidian/vault` with the actual path to your Obsidian vault.
2. **Run the Script**: Save the script as a `.py` file and execute it in your Python environment.

With this version, only the relevant code snippets will be copied to your `/Scripts` folder, ensuring that raw markdown outputs are excluded. Let me know if you have any further modifications or questions!



