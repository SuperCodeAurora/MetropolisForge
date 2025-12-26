from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container

class MetropolisForgeApp(App):
    """The main TUI Application class."""

    CSS_PATH = "../../assets/metropolis.css"
    BINDINGS = [("q", "quit", "Quit Forge")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Container(
            Static("🏗️ MetropolisForge System Online", id="welcome-msg"),
            Button("Initialize City", variant="primary", id="init-btn"),
            id="main-container"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler for button presses."""
        if event.button.id == "init-btn":
            self.exit("Initialization Protocol Complete. (This is a placeholder)")

if __name__ == "__main__":
    app = MetropolisForgeApp()
    app.run()
