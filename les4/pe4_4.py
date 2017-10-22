def new_password():
    old_password = input('Voer oud wachtwoord in: ')
    new_password = input('Voer een nieuw wachtwoord in: ')
    if new_password >= str(6):
        print('Uw wachtwoord voldoet aan de eis dat het meer dan 6 tekens bevat!')
        if new_password != old_password:
            print('Uw nieuwe wachtwoord is ingesteld!')
    else:
        print('Uw nieuwe wachtwoord voldoet niet aan de eisen!')

new_password()