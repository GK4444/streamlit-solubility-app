import yaml

def convert_requirements_to_yaml(requirements_file):
    with open(requirements_file, 'r') as f:
        requirements = f.read().splitlines()

    dependencies = {}
    for requirement in requirements:
        parts = requirement.split('==')
        if len(parts) == 2:
            package, version = parts
            dependencies[package] = version
        else:
            package = parts[0]
            dependencies[package] = None

    with open('requirements.yaml', 'w') as f:
        yaml.dump({'dependencies': dependencies}, f, default_flow_style=False)

if __name__ == '__main__':
    convert_requirements_to_yaml('requirements.txt')