import time
import logging
from agent import PCAgent

# Configure logging for service
logging.basicConfig(
    filename='jarvis_agent.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def run_service():
    """
    Main entry point for the agent as a background process.
    """
    logging.info("Starting Jarvis PC Agent Service wrapper...")
    agent = PCAgent()
    
    try:
        agent.run()
    except Exception as e:
        logging.error(f"Agent service encountered an error: {e}")
    finally:
        logging.info("Jarvis PC Agent Service stopped.")

if __name__ == "__main__":
    run_service()
