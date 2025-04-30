import random

def dynamic_chatbot():
    """A slightly more dynamic elementary chatbot."""

    greetings = ["Hello there!", "Hi!", "Greetings!", "Welcome!"]
    farewells = ["Goodbye!", "Have a great day!", "See you later!", "Farewell!"]
    affirmations = ["You're welcome!", "No problem!", "Glad I could help!", "Sure thing!"]
    default_responses = [
        "I'm not sure I understand. Could you rephrase?",
        "I'm still learning. Can you try asking something else?"
    ]

    print(random.choice(greetings) + " How can I assist you today?")

    while True:
        user_input = input("> ").lower()

        if "hello" in user_input or "hi" in user_input:
            print(random.choice(greetings))
        elif "thank you" in user_input or "thanks" in user_input:
            print(random.choice(affirmations))
        elif "bye" in user_input or "goodbye" in user_input:
            print(random.choice(farewells))
            break
        elif "order status" in user_input:
            print("To check your order status, please provide your order number.")
            order_number = input("Order Number: ")
            # Simulate looking up order status with a dynamic message
            statuses = ["processing", "shipped", "delivered", "on hold"]
            random_status = random.choice(statuses)
            if random_status == "shipped":
                tracking_number_simulated = "TRACK-" + "".join(random.choices("0123456789ABCDEF", k=10))
                print(f"Checking status for order {order_number}... Your order has shipped.. Your tracking number is: {tracking_number_simulated}")
            else:
                print(f"Checking status for order {order_number}... Your order is currently '{random_status}'.")
        elif "track order" in user_input:
            print("Please provide your tracking number.")
            tracking_number = input("Tracking Number: ")
            # Simulate tracking information with a dynamic message
            locations = ["in transit at a local facility", "out for delivery", "arrived at destination", "delayed"]
            random_location = random.choice(locations)
            print(f"Looking up tracking information for {tracking_number}... Your package is currently '{random_location}'.")
        elif "return policy" in user_input:
            print(f"Our return policy allows returns within 15 days of purchase, provided the item is in unused condition.")
        elif "contact us" in user_input:
            contact_methods = ["email", "phone", "live chat"]
            chosen_method = random.choice(contact_methods)
            if chosen_method == "email":
                print(f"You can contact us via {chosen_method} at support@ourcompany.net")
            elif chosen_method == "phone":
                print(f"You can contact us via {chosen_method} at 1-800-9297")
            elif chosen_method == "live chat":
                print(f"You can contact us via {chosen_method} on our website during business hours.")
        elif "help" in user_input:
            print("Here are some things I can help you with:")
            print("- Check order status")
            print("- Track your order")
            print("- Learn about our return policy")
            print("- Find our contact information")
            print("- Say hello or goodbye")
        else:
            print(random.choice(default_responses))

if __name__ == "__main__":
    dynamic_chatbot()