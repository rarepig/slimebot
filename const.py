from json import load

with open('secret.json', 'r') as file:
    secret = load(file)
    
def _get(json: dict, path: str):
    path = path.split('.')
    
    while path:
        json = json.get(path.pop(0))
        
        if json is None:
            return
        
    return json

def get_secret(path):
    return _get(secret, path)