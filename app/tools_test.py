# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law-or-agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from app.tools import get_current_weather


def test_get_current_weather() -> None:
    """
    Tests that the get_current_weather function returns the correct hard-coded value.
    """
    assert get_current_weather("some location") == json.dumps(
        {"temperature": 72, "conditions": "sunny"}
    )
