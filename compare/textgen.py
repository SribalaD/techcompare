from rich.table import Table
from rich.console import Console

console = Console()

def generate_output(data):
    table = Table(title="Comparison")

    opt1 = data["option1"]
    opt2 = data["option2"]

    table.add_column("Criterion")
    table.add_column(opt1)
    table.add_column(opt2)

    for c in data["criteria"]:
        table.add_row(
            c["name"],
            str(c["scores"][opt1]),
            str(c["scores"][opt2])
        )

    console.print(table)

    score1 = sum([c["scores"][opt1] for c in data["criteria"]])
    score2 = sum([c["scores"][opt2] for c in data["criteria"]])

    summary = "\nRecommendation:\n"

    if score1 > score2:
        summary += f"Use {opt1} — better based on criteria."
    elif score2 > score1:
        summary += f"Use {opt2} — better based on criteria."
    else:
        summary += "Both are equal — choose based on experience."

    return summary
