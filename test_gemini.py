
from config import generate_with_retry

try:
    print("Testing Gemini API...")
    result = generate_with_retry(
        "Reply with only: Gemini connection successful"
    )
    print("SUCCESS:", result)

except Exception as error:
    print("FAILED:", error)
