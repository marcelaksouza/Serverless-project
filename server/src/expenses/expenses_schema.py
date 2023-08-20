from server.utils.db import Initialize_db
ddb = Initialize_db()

def create_users_table(ddb):
    print("expenses table")
    
    all_tables = [table.name for table in ddb.tables.all()]
    # print(all_tables)

    if "Expenses" not in all_tables:
        # create a table
        response = ddb.create_table(TableName='Expenses',
                            AttributeDefinitions=[
                                {
                                    'AttributeName': 'ExpenseId',
                                    'AttributeType': 'S'
                                }
                            ],
                            KeySchema=[
                                {
                                    'AttributeName': 'ExpenseId',
                                    'KeyType': 'HASH'
                                }
                            ],
                            ProvisionedThroughput= {
                                'ReadCapacityUnits': 10,
                                'WriteCapacityUnits': 10
                            }
                            )
        print('Successfully created Table')
    else:
        print('Table already in exist in DB')
    
    return response