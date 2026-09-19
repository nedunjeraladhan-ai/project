# Chatbot configuration
CHATBOT_TITLE = 'StudyMate AI'
DOMAIN = 'Education & Study'

SYSTEM_PROMPT = """You are a helpful specialist for the configured domain. Give accurate, practical, easy-to-understand answers. Stay strictly within the configured domain."""
BEHAVIOR = "Helpful, concise, beginner-friendly, domain-only."

WELCOME_MESSAGE = "Hello! I am StudyMate AI. Ask me anything related to Education & Study."

PRIMARY_COLOR = '#7c3aed'
DARK_COLOR = '#172554'
SOFT_COLOR = '#ede9fe'

GEMINI_MODEL = "gemini-3.1-flash-lite"
GEMINI_API_KEY = ""  # Optional fallback. Prefer .env.
PORT = 5000
