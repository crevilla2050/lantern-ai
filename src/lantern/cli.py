import typer
from rich.console import Console

app = typer.Typer(
    name="lantern",
    help="An AI-powered terminal companion for developers and system administrators.",
)

console = Console()


@app.command()
def version():
    """Show Lantern version."""
    from lantern import __version__

    console.print(f"Lantern AI {__version__}")


@app.command()
def ask(question: str):
    """Ask Lantern a question."""
    console.print(f"[cyan]Question:[/cyan] {question}")
    console.print("[yellow]Provider integration coming soon.[/yellow]")


def main():
    app()


if __name__ == "__main__":
    main()