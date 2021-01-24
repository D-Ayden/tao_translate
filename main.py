from typing import List, Any

import PySimpleGUI as sg

from translate_gui.frame import layout, run_gui


def main(layout: List[List[Any]] = layout) -> None:
    window = sg.Window("道译", layout)

    while True:
        result = run_gui(window)
        if result == "EXIT":
            break

    window.close()


main()