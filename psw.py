#!/usr/bin/env python3

from pickle import TRUE
import random
import re
from typing import Optional
import typer


def main(
    #CLI options 
    lenght: int = typer.Option(8, "--lenght", "-l" ,help= "Lenght of the password" ),
    version: bool = typer.Option(False, "--version", "-v", help="Get the current version"),
    n: int = typer.Option(1, "--number", "-n" ,help= "Number of passwrod to generate" )):

    #CLI --help documentation 
    '''
    Random password generator
    '''

    if version:
        typer.echo("Current version: 1.7v")
        raise typer.Exit()

    for i  in range(n):
        password_generata = genera_password(lenght)
        typer.secho(f"Output: {format(password_generata)}", fg=typer.colors.GREEN)


def genera_password(lunghezza):
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '!£$%#&=?0123456789')
    while True:
        password = ''
        for i in range(0, int(lunghezza)):
            password += random.choice(caratteri)
        if valida_password(password):
            break
        else:
            format(password)
    return password

def valida_password(password):
    condizione_valida = ('^.*(?=.{'+str(len(password))+',})(?=.*\d)(?=.*[a-z])'
                        '(?=.*[A-Z])(?=.*[!£$%&#=?]).*$')
    return re.findall(condizione_valida, password)


if __name__ == '__main__':
    typer.run(main)