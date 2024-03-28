import requests
import env


class GptCompleter:
    def __init__(self, system_prompt: str) -> None:
        self._system_prompt = system_prompt

    def complete(self, prompt: str) -> str:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            json={
                "model": "gpt-4-0125-preview",
                "max_tokens": 4000,
                "temperature": 0,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "messages": [
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": prompt},
                ],
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {env.OPENAI_API_KEY}",
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
