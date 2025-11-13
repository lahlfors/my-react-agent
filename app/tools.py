# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json


def get_current_weather(location: str) -> str:
    """
    Returns the current weather for a given location.

    Args:
        location: The location for which to get the weather.

    Returns:
        A JSON string with the temperature and conditions.
    """
    # This is a placeholder implementation.
    # In a real-world scenario, this would call a weather API.
    _ = location
    return json.dumps({"temperature": 72, "conditions": "sunny"})
