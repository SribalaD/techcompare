from compare.presets import PRESET_DATA
from compare.textgen import generate_output

def compare_options(option1, option2, criteria):
    data1 = PRESET_DATA.get(option1.lower(), {})
    data2 = PRESET_DATA.get(option2.lower(), {})

    results = {"option1": option1, "option2": option2, "criteria": []}

    for c in criteria:
        score1 = data1.get(c, 2)
        score2 = data2.get(c, 2)

        results["criteria"].append({
            "name": c,
            "scores": {
                option1: score1,
                option2: score2,
            }
        })

    return generate_output(results)

