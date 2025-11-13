# Feature: Add Get_Current_Weather Tool

## Description
This feature introduces a new tool, `get_current_weather`, to the agent. This tool will provide current weather information for a specified location. Initially, it will return a hard-coded response, with the intention of integrating with an external weather API in a future iteration.

## Acceptance Criteria
*   The tool function must be named `get_current_weather`.
*   The tool must accept a single string argument named `location`.
*   The tool must return a JSON string with two keys: `temperature` (integer) and `conditions` (string).
*   For this task, the tool must return the hard-coded JSON string: `{"temperature": 72, "conditions": "sunny"}`.
*   The new tool function must be added to `my-react-agent/app/tools.py`.
*   The `get_current_weather` tool must be imported and added to the agent's tool list in `my-react-agent/app/agent.py`.
*   A new unit test, `test_get_current_weather`, must be added to `my-react-agent/app/tools_test.py` to verify the hard-coded return value.