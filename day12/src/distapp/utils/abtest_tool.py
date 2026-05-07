from statsig import StatsigEvent, statsig, StatsigUser, statsig_event

def abtest_tool():
    # Initialize Statsig with your server secret key
    statsig.initialize("secret-uOj2IK6AXOoOgplkFEVAx97gmDTff0ammwjQePsWxLS")
    for i in range(501,510):
        user = StatsigUser(user_id=f"user{i}", email="aimltraining2026@gmail.com")

        event = StatsigEvent(
            user=user,
            event_name="python_test_event"
        )

        print("Sending event...")

        statsig.log_event(event)
        
        
        # Check if the user is in the experiment
        in_experiment = statsig.check_gate(user, "experiment_name")
        if in_experiment:
            print(f"User {i} is in the experiment")
        else:
            print(f"User {i} is not in the experiment")
    #flush the events to ensure they are sent to Statsig
    statsig.flush()
    #shutdown the Statsig client to clean up resources
    statsig.shutdown()

if __name__ == "__main__":
    abtest_tool()
