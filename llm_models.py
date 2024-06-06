import subprocess


def list_available_models():
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    model_names = [line.split()[0] for line in lines[1:]]
    models = {}
    for i in range(len(model_names)):
        models[i + 1] = model_names[i]
    return models
