"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import csv
import reflex as rx

def reader_csv():
        fixure = ''
        with open('./fifa_workdcup_fixture.csv', newline='') as f:
            data = csv.reader(f, delimiter=",")
            fixure = list(data)        
        return fixure

     
        
def index() -> rx.Component:
 return rx.container(
        rx.vstack(
                rx.text("Fixture FIFA World Cup Qatar 2022**"),
                
                rx.data_table(
                    data=reader_csv()[1:len(reader_csv())],
                    columns=reader_csv()[0],
                    pagination=True,
                    sort=True,
                    search=True,
                    resizable=True,
                ),
                rx.text("**Info extraída de 'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'"), 
        )
)        
           

app = rx.App()
app.add_page(index)
