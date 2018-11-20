def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

def evaluate_score (score):
    if score < 0 or score > 100:
        return "invalid score"
    else:
        if score >= 90:
            return "excellent"
        elif score >= 50:
            return "passable"
        elif score < 50:
            return "bad"

main()