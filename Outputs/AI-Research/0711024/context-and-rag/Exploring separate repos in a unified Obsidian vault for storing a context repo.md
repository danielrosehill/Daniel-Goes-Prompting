# Prompt

Here's a model for storing context that I'd like you to explore with me. Let's say that the context "repo" is going to be an Obsidian vault. At the base of the vault I'd like to have two folders: personal and work. The idea here is that we're going to be buildling two context repos: one for LLM work for our job and the other for our personal life. Each folder is going to be versioned as a separate repo: that's to say that the "Personal" folder will be its own repo and the "Work" folder will be its own repo. What do you think of this system?

# Output

Your proposed model for storing context within an Obsidian vault by separating personal and work contexts into distinct folders is a solid approach. Here are some advantages and considerations of this system:

### Advantages

1. **Clear Separation**:
   - Having dedicated folders for personal and work contexts allows for clear organization. This makes it easy to find and manage relevant documents without sifting through unrelated content.

2. **Version Control**:
   - By treating each folder as its own repository, you can leverage version control systems like Git to track changes, revert to previous states, and manage different versions of context documents independently. This is especially useful if you need to collaborate or keep a history of changes.

3. **Customizability**:
   - You can customize the structure, naming conventions, and templates for each context repository based on the specific needs of your personal life versus your work. This allows for flexibility in how you capture and organize context.

4. **Improved Focus**:
   - With the separation of contexts, you can maintain focus on the relevant aspects of your life without distractions. For instance, when working on a project, you only access your work context, and similarly for personal reflections.

5. **Easy Access to Version History**:
   - With Git or another version control system, you can easily track changes over time and access previous versions of your context documents. This is helpful for reviewing how your thoughts or projects have evolved.

### Considerations

1. **Initial Setup Complexity**:
   - Setting up the folder structure and initializing them as separate repositories requires some initial effort. You’ll need to ensure that each folder is properly configured for version control.

2. **Maintaining Synchronization**:
   - If there are overlaps or connections between personal and work contexts, you may need a system for referencing or linking documents between the two folders. This could be achieved through linking notes in Obsidian, but it requires mindful organization.

3. **Management Overhead**:
   - You will need to manage two separate repositories, which could involve additional overhead in terms of committing changes, pulling updates, and ensuring consistency across both contexts. Automation scripts can help alleviate some of this burden.

4. **Backup Strategy**:
   - With separate repositories, ensure you have a backup strategy for both. This could involve regular pushes to a remote repository or automated backups of your local repositories.

5. **Documentation for Each Context**:
   - As you develop each context repository, consider creating documentation (e.g., a README.md) that outlines the structure, purpose, and content of each folder. This can be helpful for future reference or for onboarding others if you choose to share the context.

### Implementation Steps

1. **Create the Obsidian Vault**: Set up a new Obsidian vault to serve as your context repository.
2. **Define Folder Structure**:
   ```
   /ContextRepo
   ├── /Personal
   └── /Work
   ```
3. **Initialize Git Repositories**:
   - Navigate to each folder and initialize them as separate Git repositories:
     ```bash
     cd /ContextRepo/Personal
     git init
     git add .
     git commit -m "Initial commit for personal context"
     
     cd /ContextRepo/Work
     git init
     git add .
     git commit -m "Initial commit for work context"
     ```
4. **Set Up Version Control**:
   - Create remote repositories on platforms like GitHub, GitLab, or Bitbucket and link the local repositories for backup and collaboration.
5. **Organize Context Documents**: Develop a consistent structure and naming conventions for markdown files in each context folder.
6. **Regular Updates**: Establish a routine for updating and reviewing both repositories.

### Summary
Overall, your system for separating personal and work contexts within an Obsidian vault while leveraging version control is well-thought-out and provides a robust framework for managing your context. This approach encourages organization, clarity, and effective tracking of changes, making it easier to manage both aspects of your life.

If you want to explore any specific part of this implementation further or have additional ideas, feel free to ask!