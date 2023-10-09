import typer
from invoke import run

set_env = 'source scripts/env.sh && dev_env_lib'
app = typer.Typer()

@app.command()
def build():
    cmd = 'rm -rf dist && poetry build'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)

@app.command()
def wipe_env():
    cmd = f'''
    sver
    pip freeze | cut -d "@" -f1 | xargs pip uninstall -y
    # wipeenv
    '''
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)


@app.command()
def build_publish():
    cmd = 'rm -rf dist && poetry publish --build'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.shell)

@app.command()
def build_install():
    cmd = 'rm -rf dist && poetry build && pip install dist/*.whl --force-reinstall'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)

@app.command()
def reset_env():
    '''dont use virtualenvwrapper'''
    cmd = '''
    poetry install
    poetry shell
    '''
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.shell)


@app.command()
def run_gql():
    cmd = f'{set_env} && strawberry server app'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)


if __name__ == "__main__":
    app()

