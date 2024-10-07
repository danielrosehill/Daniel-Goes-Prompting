# Prompt

Great work. Give me a Python script that will automatically populate that folder structure. Each context document can be a markdown file with that as its file name.

# Output

Here’s a Python script that will automatically create a folder structure and generate markdown files based on the 100 context repository ideas provided. Each markdown file will be named according to its corresponding idea, and you can customize the content as needed.

```python
import os

# Define the base directory where the context repo will be created
base_directory = "Job_Context_Repo"

# Define the folder structure and corresponding file names
context_ideas = {
    "Job Description": [
        "Overview of your job role",
        "Key responsibilities",
        "Daily tasks and routines",
        "Short-term goals",
        "Long-term goals",
        "Required skills and qualifications",
        "Key performance indicators (KPIs)",
        "Tools and software you use",
        "Reporting structure (who you report to)",
        "Team members and their roles"
    ],
    "Key Projects": [
        "Overview of major projects",
        "Objectives for each project",
        "Your specific contributions to projects",
        "Challenges faced and solutions implemented",
        "Project timelines and milestones",
        "Project outcomes and impacts",
        "Stakeholders involved in projects",
        "Lessons learned from projects",
        "Best practices identified through projects",
        "Project documentation links"
    ],
    "Company Information": [
        "Company mission and vision statements",
        "Organizational structure",
        "Core values of the company",
        "Major products or services offered",
        "Competitors and market positioning",
        "Recent company news or developments",
        "Company culture and work environment",
        "HR policies that affect your role",
        "Training and development opportunities",
        "Performance review processes"
    ],
    "Industry Insights": [
        "Current trends in your industry",
        "Emerging technologies impacting your field",
        "Key publications and resources (e.g., journals, blogs)",
        "Conferences and events to attend",
        "Networking groups and professional organizations",
        "Regulatory changes affecting your industry",
        "Notable thought leaders in your field",
        "Case studies relevant to your work",
        "Market analysis reports",
        "Future predictions for your industry"
    ],
    "Professional Development": [
        "Relevant certifications and licenses",
        "Workshops or training sessions completed",
        "Courses taken related to your job",
        "Skills you want to develop further",
        "Books or resources you recommend",
        "Mentorship experiences (as a mentor or mentee)",
        "Personal development goals",
        "Feedback received from peers and supervisors",
        "Strategies for time management",
        "Techniques for effective communication"
    ],
    "Work Relationships": [
        "Key collaborators in your role",
        "Communication styles of team members",
        "Conflict resolution strategies used",
        "Feedback mechanisms within the team",
        "Collaboration tools utilized",
        "Networking strategies for building relationships",
        "Insights from team meetings",
        "Celebrations of team successes",
        "Professional challenges with colleagues",
        "Tips for effective teamwork"
    ],
    "Processes and Workflows": [
        "Standard operating procedures (SOPs) for tasks",
        "Checklists for project initiation and completion",
        "Templates used for reports and presentations",
        "Process maps for workflow understanding",
        "Quality assurance practices",
        "Time tracking methods",
        "Tools for project management (e.g., Asana, Trello)",
        "Reporting and documentation requirements",
        "Feedback loops for continuous improvement",
        "Risk management strategies"
    ],
    "Personal Reflections": [
        "Why you chose this job or career path",
        "Your initial expectations versus reality",
        "Key successes in your career",
        "Areas for improvement you’ve identified",
        "Strategies for overcoming challenges",
        "Values that guide your work",
        "Work-life balance practices",
        "Personal achievements you're proud of",
        "Key mentors and their impact on your career",
        "Inspirational quotes that resonate with you"
    ],
    "Miscellaneous": [
        "Common questions asked in job interviews for your role",
        "Examples of successful work presentations",
        "Work-related tools you find indispensable",
        "Case studies of successful projects in your industry",
        "Client or customer feedback you've received",
        "Interesting facts about your company or industry",
        "Articles you've written or contributed to",
        "Podcasts relevant to your profession",
        "Technology tools or apps you recommend",
        "Strategies for staying current in your field"
    ],
    "Future Aspirations": [
        "Career milestones you want to achieve",
        "Potential job roles you're interested in exploring",
        "Skills you want to acquire for future roles",
        "Networks you want to develop",
        "Innovations you hope to see in your industry",
        "Personal projects that could enhance your career",
        "Plans for obtaining further education",
        "Short-term projects to focus on next",
        "Long-term visions for your career",
        "Reflections on what success looks like for you"
    ]
}

# Create the base directory
os.makedirs(base_directory, exist_ok=True)

# Create the folder structure and markdown files
for category, ideas in context_ideas.items():
    # Create a directory for each category
    category_path = os.path.join(base_directory, category)
    os.makedirs(category_path, exist_ok=True)
    
    # Create a markdown file for each idea
    for idea in ideas:
        file_name = f"{idea.replace(' ', '_').replace(':', '').lower()}.md"
        file_path = os.path.join(category_path, file_name)
        
        # Write a basic template to the markdown file
        with open(file_path, 'w') as f:
            f.write(f"# {idea}\n\n<!-- Add your content here -->\n")
            
print(f"Context repository structure created at '{base_directory}'.")
```

### Instructions to Run the Script:
1. Copy the script into a Python environment (e.g., Jupyter Notebook, or a `.py` file).
2. Make sure you have Python installed on your system.
3. Run the script. It will create a directory named **Job_Context_Repo** containing all the specified categories and markdown files.

### Output:
This will create a structured folder within **Job_Context_Repo** with markdown files for each context idea, ready for you to fill in with your content.

Feel free to modify the script to add any additional features or customize it further based on your specific needs! Let me know if you need any help with that!