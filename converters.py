"""This program allows the user to perform conversions between
measurement systems for:

    temperatures
    *** Add your conversion module names here ***

Author: R. Linley
Date: 2019-12-18

Modified by:
Section: 00
Student number: 
"""

import menu
import get_int
import temperatures


def main():
    """Program execution starts here."""

    # Set up main menu and sub-menus.
    main_menu_choices = ["Temperatures"]
    temperatures_menu_choices = ["Celsius to Fahrenheit",
                                 "Fahrenheit to Celsius"]
    # Loop until user wants to quit.
    while True:
        choice = menu.do_menu("Choose a conversion type:",
                              main_menu_choices)
        # Did the user choose "Exit?"
        if choice is None:
            # Yes, then exit.
            break
        if choice == 1:  # User chose temperature conversions.
            # Loop until user wants to return to the main menu.
            while True:
                choice = menu.do_menu("Choose a temperature conversion",
                                      temperatures_menu_choices)
                if choice is None:
                    break
                if choice is 1:  # Celsius to Fahrenheit chosen.
                    cels = get_int.input_int("\nDegrees Celsius: ")
                    print((f"\n{cels} degrees Celsius is "
                           f"{temperatures.cels_to_fahr(cels):.1f} "
                           "degrees Fahrenheit."))
                else:  # Fahrenheit to Celsius chosen.
                    fahr = get_int.input_int("\nDegrees Fahrenheit: ")
                    print((f"\n{fahr} degrees Fahrenheit is "
                           f"{temperatures.fahr_to_cels(fahr):.1f} "
                           "degrees Celsius."))


main()
