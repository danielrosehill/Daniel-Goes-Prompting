# Prompt

Let's carry on with the context system idea. What about creating a personal LLM agent whose sole purpose was generating these context documents. I'd like it to have two "settings": creating personal context and work context. It would operate by simply asking the user questions on a random topic and from that it would generate a context document - which we've said could be markdown initially. Could you draft the config for such an agent?

# Output

Creating a personal LLM agent dedicated to generating context documents is an exciting idea! Below is a draft configuration for such an agent, including its core functionalities, settings, and the overall flow of interaction with the user. 

### Agent Configuration Draft

#### 1. **Agent Overview**
- **Name**: Context Generator Agent (CGA)
- **Purpose**: To generate personalized context documents based on user inputs, tailored for both personal and work-related contexts.
- **Output Format**: Markdown files (.md).

#### 2. **Settings**
- **Mode**: 
  - **Personal Context Mode**: Generates context documents related to personal life, interests, and goals.
  - **Work Context Mode**: Focuses on professional life, job-related information, and projects.
  
#### 3. **Functionality**
- **Question Generation**: The agent will randomly select topics related to personal or work contexts and ask the user questions to gather information.
- **Data Collection**: Based on user responses, the agent will compile relevant information into a structured context document.
- **Markdown Formatting**: The generated context documents will follow a predefined markdown structure for consistency and ease of use.

#### 4. **User Interaction Flow**
1. **Greeting and Mode Selection**:
   - The agent introduces itself and asks the user to select a mode (Personal or Work).
   - Example Prompt: "Hello! I’m your Context Generator Agent. Would you like to create a personal context document or a work context document?"

2. **Random Topic Selection**:
   - The agent randomly selects a topic related to the chosen mode.
   - Example Topics:
     - **Personal Context**: Hobbies, life goals, significant events, favorite books, or travel experiences.
     - **Work Context**: Job roles, projects, skills, achievements, or industry trends.

3. **Questioning**:
   - The agent poses open-ended questions based on the selected topic.
   - Example Question: "What hobbies are you passionate about, and why do they matter to you?"

4. **User Responses**:
   - The user provides detailed responses to the questions.
   - The agent should encourage elaboration for richer content.

5. **Document Generation**:
   - The agent compiles user responses and generates a structured markdown document.
   - Example Document Structure:
     ```markdown
     # Context Document: [Title based on Topic]

     ## Summary
     - Brief summary based on user input.

     ## Details
     - **Topic**: [Selected Topic]
     - **Responses**:
       - [User Response 1]
       - [User Response 2]
       - [User Response 3]
     
     ## Reflections
     - [Any additional insights or conclusions]
     ```

6. **Review and Save**:
   - The agent presents the generated document to the user for review.
   - Example Prompt: "Here’s the context document I created based on your responses. Would you like to make any changes or should I save it?"

7. **Saving the Document**:
   - If the user approves, the agent saves the document in a predefined folder (e.g., `/Context`) with a timestamped filename.
   - Example Filename: `ddmmyy-personal-context.md` or `ddmmyy-work-context.md`.

8. **Repeat or Exit**:
   - The agent can ask if the user would like to create another context document or exit.
   - Example Prompt: "Would you like to create another context document or finish for now?"

#### 5. **Technical Implementation Considerations**
- **LLM Integration**: Choose an LLM (like GPT-4 or a fine-tuned version) that can handle context generation based on prompts.
- **Natural Language Understanding**: Ensure the agent can understand and process user responses effectively.
- **Storage Mechanism**: Implement a system for saving documents in markdown format and managing file paths.

#### 6. **User Experience Enhancements**
- **Customization**: Allow users to define their own topics of interest for more personalized interactions.
- **Feedback Loop**: Implement a mechanism for users to provide feedback on generated documents to improve the agent’s performance over time.

### Summary
This configuration outlines the key functionalities and user interaction flow for a personal LLM agent dedicated to generating context documents. By incorporating random topic questioning and user responses, the agent can create meaningful and structured markdown files that capture both personal and work-related contexts effectively.

If you need further details or modifications to this configuration, let me know!