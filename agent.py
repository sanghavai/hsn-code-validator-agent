from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from hsn_lookup_tool import hsn_lookup  # Import your FunctionTool here

# === Agent Setup ===
APP_NAME = "hsn_validator_app"
USER_ID = "user1234"
SESSION_ID = "session_001"
MODEL_ID = "gemini-1.5-flash"

root_agent = Agent(
    model=MODEL_ID,
    name="hsn_validator_agent",
    instruction=(
        "You are an HSN code validation assistant. When given one or more HSN codes "
        "(comma or space separated), use the 'hsn_lookup' tool to check each code's "
        "format validity and existence in the dataset. Return the validation results clearly."
    ),
    tools=[hsn_lookup],
)

# === Session and Runner Setup ===
session_service = InMemorySessionService()
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

# === Query Handler ===
def call_agent(query: str):
    content = types.Content(role="user", parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response:\n", final_response)

# === Example Run ===
if __name__ == "__main__":
    user_input = input("Enter one or more HSN codes (comma or space separated): ")
    call_agent(user_input)
