# Prompt

I see. So let me describe the primitive system that I'm using currently. Rather than using a proper RAG system, I'm crating a library of contextual "snippets". I'll give you an example: I created what I call a "context document" which has my computer's hardware. This way I can ask GPT a question like "how much RAM could I add to my computer?" without needing to repeat the spec each time. I achieve this by dropping a markdown file into the conversation to provide the context alongside my prompt. Does this kind of system have a formal name?

# Output

The system you're using could be described as a form of "manual context management" or "manual context injection." In a way, you're creating your own version of what Retrieval-Augmented Generation (RAG) systems automate. However, because you're manually organizing and dropping in context documents (like markdown files) into conversations, it differs from more sophisticated systems that retrieve context dynamically from a large database.

What you're doing doesn't have a widely recognized formal name, but it fits under concepts like:

- **Contextual memory management**: You're manually managing a set of memory or context "snippets" that provide background information to your assistant.
- **Manual context-based retrieval**: You're manually injecting relevant context (like your computer specs) when needed, which is similar to how RAG systems automatically pull context based on embeddings.

In essence, it's like a simpler, more hands-on approach to what modern AI systems are trying to automate with embeddings and retrieval systems. But it's clever because it achieves a similar goal: reducing repetition by having a pre-built memory of information ready to provide context!