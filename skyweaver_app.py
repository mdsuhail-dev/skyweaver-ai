import anthropic
import json
from pathlib import Path

def generate_sky_poetry(sky_description: str) -> str:
    """
    Transform what you see in the night sky into poetic AI interpretation.
    Uses Claude (via Featherless) to create meaningful narratives.
    """
    client = anthropic.Anthropic(api_key="YOUR_FEATHERLESS_API_KEY")
    
    prompt = f"""You are SkyWeaver - a mystical poet who transforms observations of the night sky into profound, beautiful narratives.

User saw this in the night sky: "{sky_description}"

Create a SHORT, poetic 2-3 sentence interpretation that:
1. Validates what they saw
2. Adds cosmic meaning/mythology
3. Ends with an emotional or thought-provoking statement

Be creative, mystical, but grounded. Keep it under 100 words."""

    message = client.messages.create(
        model="meta-llama/llama-2-70b-chat",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text


def create_demo():
    """Create a demo output"""
    test_observations = [
        "I see a dragon made of stars chasing the moon",
        "There's a eye watching me from the darkness",
        "I see my future written in constellations"
    ]
    
    print("🌙 SkyWeaver.AI - Night Sky Poetry Generator 🌙")
    print("=" * 50)
    
    results = []
    for obs in test_observations:
        print(f"\n📍 You see: {obs}")
        # For demo without API key
        demo_response = f"✨ {obs.upper()} - This cosmic vision speaks of wonder and connection."
        print(f"🎭 SkyWeaver says: {demo_response}\n")
        results.append({
            "observation": obs,
            "interpretation": demo_response
        })
    
    # Save demo output
    with open("demo_output.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("✅ Demo completed! Check demo_output.json")
    return results


if __name__ == "__main__":
    create_demo()
