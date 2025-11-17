from dataclasses import dataclass

@dataclass
class InputData:
    eenmalige_inleg: float
    maandelijkse_inleg: float
    looptijd: int
    winst_percentage: float

    def validatie(self) -> None:
        if self.eenmalige_inleg < 0:
            raise ValueError("Eenmalige inleg mag niet negatief zijn.")
        if self.maandelijkse_inleg < 0:
            raise ValueError("Maandelijkse inleg mag niet negatief zijn.")
        if self.looptijd <= 0:
            raise ValueError("Looptijd moet groter zijn dan 0.")
        if self.winst_percentage <= 0 or self.winst_percentage > 100:
            raise ValueError("Winstpercentage moet groter zijn dan 0 en kleiner of gelijk dan 100")


def bereken_saldo(eenmalige_inleg: float, maandelijkse_inleg:float, looptijd: float, winst_percentage: float) -> None:
    data = InputData(eenmalige_inleg, maandelijkse_inleg, looptijd, winst_percentage)
    data.validatie()

    marge = 1 + winst_percentage / 100
    jaarlijkse_inleg = maandelijkse_inleg * 12
    saldo = eenmalige_inleg
    totale_inleg = eenmalige_inleg + (jaarlijkse_inleg * float(looptijd))

    for _ in range(looptijd):
        saldo = (saldo + jaarlijkse_inleg) * marge

    winst = saldo - totale_inleg
    return saldo, totale_inleg, winst


def main():
    while True:
        print("Voer onderstaande informatie in.\n")

        try:
            eenmalige_inleg = float(input("Eenmalige inleg (€): "))
            maandelijkse_inleg = float(input("Maandelijkse inleg (€): "))
            looptijd = int(input("Looptijd (jaren): "))
            winst_percentage = float(input("Gemiddelde winst per jaar (%): "))

            saldo, totale_inleg, winst = bereken_saldo(
                eenmalige_inleg,
                maandelijkse_inleg,
                looptijd,
                winst_percentage
            )

            print("\n-------------------------------\n")
            print(f"Totale inleg: €{totale_inleg:2.2f}")
            print(f"Saldo: €{saldo:2.2f}")
            print(f"Winst: €{winst:2.2f}")

        except ValueError as e:
            print(f"\nError: {e}.")

        # Vraag of de gebruiker opnieuw wil
        opnieuw = input("\nWil je opnieuw? (j/n): ").strip().lower()
        if opnieuw != "j":
            break


if __name__ == "__main__":
    main()





