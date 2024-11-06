#!/usr/bin/env python3
import random
import re
import typer


def main(
    #CLI options 
    lenght: int = typer.Option(8, "--lenght", "-l" ,help= "Lenght of the password" ),
    version: bool = typer.Option(False, "--version", "-v", help="Get the current version"),
    n: int = typer.Option(1, "--number", "-n" ,help= "Number of password to generate" )):

    #CLI --help documentation 
    '''
    Random password generator
    '''

    if version:
        typer.echo("Current version: 1.7v")
        raise typer.Exit()

    for i  in range(n):
        generatedPassword = makePassword(lenght)
        typer.secho(f"Output: {format(generatedPassword)}")

def makePassword(len):
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%#&=?0123456789')

    while True:
        password = ''
        for i in range(0, int(len)):
            password += random.choice(chars)

        if validatePassword(password):
            break
        else:
            format(password)
    return password

def validatePassword(password):
    trueCondition = ('^.*(?=.{'+str(len(password))+',})(?=.*\\d)(?=.*[a-z])'
                        '(?=.*[A-Z])(?=.*[!£$%&#=?]).*$')
    return re.findall(trueCondition, password)

if __name__ == '__main__':
    typer.run(main)
