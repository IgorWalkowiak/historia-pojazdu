from vehicle_data import VehicleDataFetcher
from date_gen import DateGenerator
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.prompt import Prompt, IntPrompt
from rich.align import Align
import time

def find_first_registration_date(registration_number: str, vin_number: str, year_to_check: int) -> str | None:
    fetcher = VehicleDataFetcher()
    for first_registration_date in DateGenerator(year_to_check):
        response = fetcher.get_vehicle_data(
            registration_number=registration_number,
            vin_number=vin_number,
            first_registration_date=first_registration_date,
        )
        print(f"Found on {response.status_code}, {response.text}")


def run_console_ui() -> None:
    console = Console()

    console.print(
        Panel(
            Align.center("[bold]Wyszukiwanie daty pierwszej rejestracji[/]"),
            border_style="cyan",
            title="Historia Pojazdu"
        )
    )

    registration_number = Prompt.ask("Podaj numer rejestracyjny (np. PKS66111)").strip().upper()
    vin_number = Prompt.ask("Podaj numer VIN (np. VF1RJB00265666700)").strip().upper()
    year_to_check = IntPrompt.ask("Podaj rok do sprawdzenia (np. 2020)")

    console.print("Prosze czekać")

    date_generator = DateGenerator(year_to_check)
    total_days = (date_generator.end_date - date_generator.start_date).days + 1

    fetcher = VehicleDataFetcher()
    found_date: str | None = None

    progress_columns = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    ]

    with Progress(*progress_columns, expand=True) as progress:
        task_id = progress.add_task(f"Sprawdzanie {year_to_check}...", total=total_days)
        for current_date in date_generator:
            progress.update(task_id, description=f"Sprawdzanie {current_date}")
            try:
                response = fetcher.get_vehicle_data(
                    registration_number=registration_number,
                    vin_number=vin_number,
                    first_registration_date=current_date,
                )
                if response.status_code == 429:
                    print(f"Error: {response.status_code}, {response.text}")
                    time.sleep(10)
                    response = fetcher.get_vehicle_data(
                        registration_number=registration_number,
                        vin_number=vin_number,
                        first_registration_date=current_date,
                    )
                if response.status_code == 200:
                    found_date = current_date
                    break
                
                if response.status_code != 404 :
                    console.print(
                        Panel(
                            f"Problem z połączeniem [{response.status_code}], {response.text}",
                            title="Error",
                            border_style="red",
                        )
                    )
                    break
                time.sleep(3)
            except Exception as e:                    
                console.print(
                        Panel(
                            f"Nieznany błąd: {str(e)}",
                            title="Error",
                            border_style="red",
                        )
                    )
                pass
            finally:
                progress.advance(task_id)
    if found_date:
        console.print(
            Panel(
                f"[bold green]Znaleziono datę pierwszej rejestracji:[/] [white]{found_date}[/]",
                title="Sukces",
                border_style="green",
            )
        )
    else:
        console.print(
            Panel(
                "[bold red]Nie znaleziono daty w podanym roku[/]",
                title="Brak wyniku",
                border_style="red",
            )
        )

if __name__ == "__main__":
    run_console_ui()
    #find_first_registration_date("PKS66438", "VF1RJB00265666724", 2020)

    
