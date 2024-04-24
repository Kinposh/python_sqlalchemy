from db_init import engine, employee_basic_info_table

with engine.connect() as conn:
    query = employee_basic_info_table.select().where(employee_basic_info_table.c.gid == 'Z0048HFZ')

    result_set = conn.execute(query)

    for row in result_set:
        print(row)



