from db_init import engine, employee_basic_info_table

with engine.connect() as conn:
    query = employee_basic_info_table.select().where(employee_basic_info_table.c.gid == 'Z0048HFZ')
    query1 = employee_basic_info_table.select(name).where(employee_basic_info_table.c.gid == 'Z0048HFZ')
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)
