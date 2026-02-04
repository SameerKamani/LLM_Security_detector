import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def analyze_specs(user_specs):
    """
    Part 2: Analyzes GenAI app specifications and maps potential 
    vulnerabilities to OWASP Top 10 for LLMs and MITRE ATLAS.
    """
    
    # Initialize the Groq client
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # System prompt to enforce the specific frameworks required by the assignment
    system_prompt = (
        "You are an AI Red Team lead and Threat Modeler. "
        "Analyze the following GenAI/Agentic application specifications for potential security vulnerabilities. "
        "Your output MUST be structured as follows:\n\n"
        "1. **OWASP Top 10 for LLM Apps Mapping**: Identify which of the top 10 risks apply (e.g., LLM01: Prompt Injection, LLM02: Insecure Output Handling).\n"
        "2. **MITRE ATLAS Perspective**: Map potential attack tactics (e.g., Reconnaissance, Initial Access, ML Model Abuse).\n"
        "3. **Actionable Recommendations**: Provide specific security controls or architectural changes to mitigate these risks.\n\n"
        "Be specific to the provided use case. Avoid generic security advice."
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": f"Analyze these GenAI app specs:\n\n{user_specs}",
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.3, # Low temperature for structured, framework-aligned responses
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"