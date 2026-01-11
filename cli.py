import typer
from compare.engine import compare_options

app = typer.Typer()

@app.command()
def compare(option1: str, option2: str, criteria: str):
    criteria_list = [c.strip() for c in criteria.split(",")]
    result = compare_options(option1, option2, criteria_list)
    print(result)

if __name__ == "__main__":
    app()
