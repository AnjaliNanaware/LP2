def employee_performance_expert_system():
    """A simple rule-based expert system for employee performance evaluation."""

    print("Welcome to the Simple Employee Performance Evaluation System!")
    print("Please answer the following questions about the employee's performance.")

    performance_data = {}

    # Define evaluation criteria and their possible ratings
    criteria = {
        "Productivity": ["Low", "Average", "High"],
        "Quality of Work": ["Needs Improvement", "Satisfactory", "Excellent"],
        "Teamwork": ["Poor", "Fair", "Good", "Excellent"],
        "Problem Solving": ["Reactive", "Proactive", "Exceptional"],
        "Communication": ["Unclear", "Clear", "Effective"],
    }

    # Gather performance data
    for criterion, ratings in criteria.items():
        while True:
            print(f"\nRate the employee's {criterion} ({', '.join(ratings)}):")
            rating = input("> ").strip().title()
            if rating in ratings:
                performance_data[criterion] = rating
                break
            else:
                print("Invalid rating. Please choose from the options provided.")

    # Define rules for overall performance assessment
    rules = [
        {"conditions": {"Productivity": "High", "Quality of Work": "Excellent", "Teamwork": "Excellent", "Problem Solving": "Exceptional", "Communication": "Effective"}, "assessment": "Outstanding Performer"},
        {"conditions": {"Productivity": "High", "Quality of Work": "Excellent", "Teamwork": "Good"}, "assessment": "High Achiever"},
        {"conditions": {"Productivity": "Average", "Quality of Work": "Satisfactory", "Teamwork": "Fair"}, "assessment": "Meets Expectations"},
        {"conditions": {"Productivity": "Low", "Quality of Work": "Needs Improvement"}, "assessment": "Needs Improvement"},
        # Add more rules as needed
    ]

    # Evaluate performance based on the rules
    overall_assessment = "Further Review Required"  # Default assessment
    for rule in rules:
        match = True
        for criterion, expected_rating in rule["conditions"].items():
            if performance_data.get(criterion) != expected_rating:
                match = False
                break
        if match:
            overall_assessment = rule["assessment"]
            break

    print("\n--- Performance Evaluation ---")
    for criterion, rating in performance_data.items():
        print(f"{criterion}: {rating}")
    print(f"\nOverall Performance Assessment: {overall_assessment}")

if __name__ == "__main__":
    employee_performance_expert_system()