import os
import glob
import datetime
import json

# Define the base directory of your repository as a relative path
repo_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

# Define the directories to count markdown files
directories = {
    "Outputs": os.path.join(repo_base, "Outputs"),
    "Prompts": os.path.join(repo_base, "Prompts"),
    "Context": os.path.join(repo_base, "Context"),
}

# Path to store the memory file
memory_file_path = os.path.join(repo_base, "Scripts", "memory.json")

# Function to load previous counts from memory
def load_previous_counts():
    if os.path.exists(memory_file_path):
        with open(memory_file_path, 'r') as f:
            return json.load(f)
    return {key: 0 for key in directories.keys()}

# Function to save current counts to memory
def save_current_counts(current_counts):
    with open(memory_file_path, 'w') as f:
        json.dump(current_counts, f)

# Function to count markdown files recursively
def count_markdown_files():
    current_counts = {}
    previous_counts = load_previous_counts()

    for key, directory in directories.items():
        # Initialize count for the current directory
        current_counts[key] = 0
        
        # Recursively count markdown files in the current directory
        for root, _, files in os.walk(directory):
            markdown_files = [file for file in files if file.endswith('.md')]
            current_counts[key] += len(markdown_files)

    # Prepare report content
    report_lines = []
    report_lines.append(f"# Output\n")
    report_lines.append(f"Number in vault: {current_counts['Outputs']}\n")
    report_lines.append(f"Additions since last run: {current_counts['Outputs'] - previous_counts['Outputs']}\n")
    
    report_lines.append(f"# Prompts\n")
    report_lines.append(f"Number in vault: {current_counts['Prompts']}\n")
    report_lines.append(f"Additions since last run: {current_counts['Prompts'] - previous_counts['Prompts']}\n")
    
    report_lines.append(f"# Contextual Documents\n")
    report_lines.append(f"Number in vault: {current_counts['Context']}\n")
    report_lines.append(f"Additions since last run: {current_counts['Context'] - previous_counts['Context']}\n")

    # Save the report with the current date
    report_date = datetime.datetime.now().strftime("%d%m%y")
    report_filename = os.path.join(repo_base, "Analytics", f"{report_date}-vault-report.md")
    
    with open(report_filename, 'w') as report_file:
        report_file.write('\n'.join(report_lines))

    # Save the current counts for the next run
    save_current_counts(current_counts)

# Run the function
count_markdown_files()