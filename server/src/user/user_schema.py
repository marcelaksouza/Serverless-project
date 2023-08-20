from server.utils.db import Initialize_db
ddb = Initialize_db()

def create_users_table(ddb):
    print("user table")
    
    all_tables = [table.name for table in ddb.tables.all()]

    if "Users" not in all_tables:
        # create a table
        response = ddb.create_table(TableName='Users',
                            AttributeDefinitions=[
                                {
                                    'AttributeName': 'userId',
                                    'AttributeType': 'S'
                                },
                                {
                                    'AttributeName': 'userName',
                                    'AttributeType': 'S'
                                },
                                {
                                    'AttributeName': 'password',
                                    'AttributeType': 'S'
                                },
                                {
                                    'AttributeName': 'isActive',
                                    'AttributeType': 'BOOL'
                                }
                            ],
                            KeySchema=[
                                {
                                    'AttributeName': 'UserId',
                                    'KeyType': 'HASH'
                                }
                            ],
                            ProvisionedThroughput= {
                                'ReadCapacityUnits': 10,
                                'WriteCapacityUnits': 10
                            }
                            )
        print('Successfully created Users table')
    else:
        print('User table already in exist in DB')
    
    return response