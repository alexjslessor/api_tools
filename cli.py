import typer
from rich import print as rprint
from invoke import run

app = typer.Typer()

@app.command()
def build():
    cmd = 'rm -rf dist && poetry build'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        rprint(result.stdout)

@app.command()
def build_publish():
    cmd = 'rm -rf dist && poetry publish --build'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        rprint(result.stdout)

@app.command()
def build_install():
    cmd = 'rm -rf dist && poetry build && pip install dist/*.whl --force-reinstall'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        rprint(result.stdout)

if __name__ == "__main__":
    app()

