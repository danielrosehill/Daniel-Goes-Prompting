# Prompt

Great. Now the Python script to build out that structure using the same model we did before?

# Output

Here’s a Python script that will create a folder structure and generate markdown files based on the 100 personal context repository ideas provided. Each markdown file will be named according to its corresponding idea, and you can customize the content as needed.

```python
import os

# Define the base directory where the personal context repo will be created
base_directory = "Personal_Context_Repo"

# Define the folder structure and corresponding file names
personal_context_ideas = {
    "Personal Information": [
        "Full name and nicknames",
        "Date of birth",
        "Contact information (email, phone, address)",
        "Emergency contacts",
        "Important health information (allergies, medications)",
        "Personal identification numbers (e.g., Social Security, ID numbers)",
        "Personal mission statement",
        "Life goals and aspirations",
        "Favorite quotes and mottos",
        "Personal values and beliefs"
    ],
    "Education": [
        "Schools attended (high school, college, etc.)",
        "Degrees earned and majors",
        "Certifications and licenses",
        "Significant projects or papers completed",
        "Honors and awards received",
        "Extracurricular activities",
        "Key learning experiences",
        "Skills acquired during education",
        "Mentors and their impact on your education",
        "Resources or books that influenced your learning"
    ],
    "Work Experience": [
        "Job history (companies, roles, dates)",
        "Key achievements in each job",
        "Skills developed through work experience",
        "Professional references",
        "Notable projects worked on",
        "Lessons learned from challenges faced at work",
        "Career aspirations and goals",
        "Networking contacts and relationships",
        "Industry-specific knowledge or insights",
        "Feedback received from colleagues or supervisors"
    ],
    "Hobbies and Interests": [
        "Hobbies and how you got into them",
        "Skills or techniques learned in hobbies",
        "Favorite books, movies, and music",
        "Travel experiences and places visited",
        "Volunteer experiences and contributions",
        "Sports or physical activities you enjoy",
        "Creative projects (art, writing, etc.) and accomplishments",
        "Classes or workshops attended for personal interests",
        "Favorite recipes or cooking techniques",
        "Lists of items you want to collect or try"
    ],
    "Health and Wellness": [
        "Personal fitness goals and routines",
        "Nutrition and diet preferences",
        "Mental health practices (meditation, mindfulness)",
        "Medical history and important health records",
        "Exercise routines and schedules",
        "Strategies for stress management",
        "Sleep habits and routines",
        "Support networks for health and wellness",
        "Health-related resources or guides",
        "Progress tracking for health goals"
    ],
    "Finances": [
        "Budgeting strategies and tools used",
        "Income sources and financial goals",
        "Investment strategies and portfolios",
        "Savings plans for short-term and long-term goals",
        "Debt management strategies",
        "Insurance policies and coverage details",
        "Tax-related documents and information",
        "Financial milestones achieved",
        "Major purchases and their impact on finances",
        "Lessons learned from financial mistakes"
    ],
    "Personal Development": [
        "Books or articles read for personal growth",
        "Courses taken for self-improvement",
        "Skills you want to develop or learn",
        "Personal projects and their outcomes",
        "Reflections on past experiences and growth",
        "Time management strategies that work for you",
        "Methods for goal setting and tracking progress",
        "Challenges you want to overcome",
        "Feedback received on personal development efforts",
        "Strategies for effective communication"
    ],
    "Relationships": [
        "Key relationships and their significance",
        "Communication styles of family and friends",
        "Important life events with loved ones",
        "Strategies for conflict resolution",
        "Family traditions and their meanings",
        "Reflections on your role in relationships",
        "Networking strategies for building friendships",
        "Significant mentors and their influence",
        "Social activities you enjoy with others",
        "Reflections on personal values in relationships"
    ],
    "Future Planning": [
        "Vision for your ideal life",
        "Short-term and long-term goals",
        "Bucket list items you want to achieve",
        "Plans for personal development in the coming years",
        "Desired career trajectory and milestones",
        "Locations you want to travel to",
        "Skills you want to master",
        "Projects you want to undertake",
        "Legacy you wish to leave behind",
        "Strategies for achieving your life goals"
    ],
    "Miscellaneous": [
        "Technology tools or apps you find useful",
        "Important documents and where they are stored",
        "Personal projects you’re currently working on",
        "Quotes or phrases that inspire you",
        "Advice you would give to your younger self",
        "Important life lessons learned",
        "Fun facts about yourself",
        "Rituals or routines that bring you joy",
        "Items you want to declutter or organize",
        "Future aspirations for your personal life"
    ]
}

# Create the base directory
os.makedirs(base_directory, exist_ok=True)

# Create the folder structure and markdown files
for category, ideas in personal_context_ideas.items():
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
            
print(f"Personal context repository structure created at '{base_directory}'.")
```

### Instructions to Run the Script:
1. Copy the script into a Python environment (e.g., Jupyter Notebook, or a `.py` file).
2. Make sure you have Python installed on your system.
3. Run the script. It will create a directory named **Personal_Context_Repo** containing all the specified categories and markdown files.

### Output:
This will create a structured folder within **Personal_Context_Repo** with markdown files for each personal context idea, ready for you to fill in with your content.

Feel free to modify the script to add any additional features or customize it further based on your specific needs! Let me know if you need any help with that!