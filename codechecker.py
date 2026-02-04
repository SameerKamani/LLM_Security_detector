import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env (formerly secrets.txt)
load_dotenv()

def analyze_code(user_code):
    """
    Part 1: Takes a code snippet, identifies security vulnerabilities, 
    and provides recommended fixes using the Groq API.
    """
    
    # Initialize the Groq client
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # The System Prompt is crucial for focusing on SECURITY vs general refactoring
    system_prompt = (
        "You are an expert Security Researcher. Your task is to analyze the provided code "
        "specifically for security vulnerabilities (e.g., OWASP Top 10, SQL injection, XSS, "
        "insecure defaults, or buffer overflows). \n\n"
        "1. Identify the specific vulnerability.\n"
        "2. Explain the risk.\n"
        "3. Provide a SECURE version of the code.\n"
        "Do not suggest general style improvements or refactoring unless it directly impacts security."
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
                    "content": f"Analyze this code for security issues:\n\n{user_code}",
                }
            ],
            model="llama-3.3-70b-versatile", # High-intelligence model for reasoning
            temperature=0.2, # Lower temperature for more consistent, factual analysis
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"