from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    quantity = Col('Quantity')
    description = Col('Description')
    date_added = Col('Date Created')
