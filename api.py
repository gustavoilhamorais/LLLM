import requests, json, os


stream = []


def generate(model, prompt):
    stream.append("\n\n")
    stream.append(f"[USER]\n{prompt}\n")
    url = "http://localhost:11434/api/generate"
    data = {"model": model, "prompt": prompt}
    print_joined_stream = lambda stream: print("".join(stream))

    with requests.post(url, json=data, stream=True) as response:
        if response.status_code == 200:
            stream.append("\n[AI]\n")
            for chunk in response.iter_content(chunk_size=None):
                if chunk:
                    stream.append(json.loads(chunk.decode("utf-8"))["response"])
                    os.system("clear")
                    print_joined_stream(stream)
        else:
            print(f"Request failed with status code: {response.status_code}")
