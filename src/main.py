from dotenv import load_dotenv
import sys
import warnings
from datetime import datetime
load_dotenv()

from src.crew  import BusinessPlan

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with example inputs.
    """
    inputs = {
        "business_name": "DesignVet",
        "business_idea": "DesignMatch is a platform that connects freelance designers with startup founders for on-demand design projects",
        "pricing_mode": "We charge 5% per design work delivered and also vet freelancers",
    }
    
    try:
        BusinessPlan().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "business_name": "DesignVet",
        "business_idea": "DesignMatch is a platform that connects freelance designers with startup founders for on-demand design projects",
        "pricing_mode": "We charge 5% per design work delivered and also vet freelancers",
    }
    try:
        BusinessPlan().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BusinessPlan().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return results.
    """
    inputs = {
        "business_name": "DesignVet",
        "business_idea": "DesignMatch is a platform that connects freelance designers with startup founders for on-demand design projects",
        "pricing_mode": "We charge 5% per design work delivered and also vet freelancers",
    }
    
    try:
        BusinessPlan().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()