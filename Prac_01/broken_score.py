def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("invalid score")
    else:
        if score >= 90:
            print("excellent")
        elif score >= 50:
            print("passable")
        elif score < 50:
            print("bad")

main()