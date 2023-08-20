def add_seeds(ddb):
    #List tables
    
    all_tables = [table.name for table in ddb.tables.all()]
    # print(all_tables)

    if "Expenses" not in all_tables:
        # create a table
        ddb.create_table(TableName='Expenses',
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
        print('Successfully created Expenses Table')
    else:
        print('Table already in exist in DB')

    input = {'ExpenseId': '1', 'Date': '2022-04-22', 'Value': 100, 'Description':'House', 'Category':'House', 'Sub-Category':'Rent', 'UserID':'1'}

    table = ddb.Table('Expenses')
    #3 - Insert Data
    table.put_item(Item=input)
    print('Seeds were successfully added')

    #4 - Scan Table - Show items in DB
    # scanResponse = table.scan(TableName='Expenses')
    # items = scanResponse['Items']
    # for item in items:
    #     print(item)
