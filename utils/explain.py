def generate_explanation(year, km):
    reasons = []

    if year > 2018:
        reasons.append("Newer model increases price")

    if km > 80000:
        reasons.append("High mileage reduces price")

    if year < 2013:
        reasons.append("Older model reduces price")

    return reasons