#!python.exe
def start_html():
    print("""
    <html>
    <head>

    <style>
        table, th, td {
            border:1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
    </style>
    </head>
    <body>
    """)

def end_html():
    print("""
    </body>
    </html>
    """)
