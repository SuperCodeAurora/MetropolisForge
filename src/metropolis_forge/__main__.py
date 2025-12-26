import sys
from metropolis_forge.app import MetropolisForgeApp

def main():
    """
    Entry point for the 'forge' command defined in pyproject.toml.
    """
    app = MetropolisForgeApp()
    app.run()

if __name__ == "__main__":
    main()
