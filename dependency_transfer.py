import yaml

# Load requirements.txt
with open('requirements.txt', 'r') as f:
    pip_packages = f.read().splitlines()

# Load environment.yml
with open('environment.yml', 'r') as f:
    env = yaml.safe_load(f)

# Add pip packages to environment.yml
if 'dependencies' in env:
    env['dependencies'].append({'pip': pip_packages})
else:
    env['dependencies'] = [{'pip': pip_packages}]

# Write back to environment.yml
with open('environment.yml', 'w') as f:
    yaml.safe_dump(env, f)
