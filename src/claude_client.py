from anthropic import Anthropic, APIStatusError
from src.config import ANTHROPIC_API_KEY


def ask_claude(
    system_prompt: str,
    user_prompt: str,
    model: str = "claude-sonnet-4-5",
    max_tokens: int = 1600
) -> str:
    if not ANTHROPIC_API_KEY:
        return "Claude unavailable: missing ANTHROPIC_API_KEY."

    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    try:
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return message.content[0].text

    except APIStatusError as e:
        return f"Claude unavailable: {str(e)}"

    except Exception as e:
        return f"Claude unavailable: {str(e)}"