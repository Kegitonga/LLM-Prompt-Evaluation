"""evaluate.py - simple prompt evaluation runner (simulated)
Produces JSON outputs with prompt, response, and simple heuristics.
"""
import json
from datetime import datetime

def fake_llm(prompt):
    # Placeholder: replace with real LLM API call
    return f"Simulated response to: {prompt}"

def evaluate(prompts):
    results = []
    for p in prompts:
        resp = fake_llm(p)
        score = len(resp) % 10  # fake heuristic
        results.append({
            'prompt': p,
            'response': resp,
            'score': score,
            'timestamp': datetime.utcnow().isoformat()
        })
    return results

if __name__ == '__main__':
    sample = [
        'Explain logistic regression in 3 bullets.',
        'Create a JSON list of 3 African capitals.'
    ]
    out = evaluate(sample)
    print(json.dumps(out, indent=2))
