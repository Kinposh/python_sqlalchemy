from db_init import engine, employee_basic_info_table
from sqlalchemy.sql import and_, or_

with engine.connect() as conn:
    # query = employee_basic_info_table.select().\
    #     where(employee_basic_info_table.c.org_code == 'RC-CN DI S-RE SE&TSS TSS TEST-T1').\
    #     where(employee_basic_info_table.c.level == 'E2')

    query = employee_basic_info_table.select().\
        where(
            and_(
                employee_basic_info_table.c.org_code == 'RC-CN DI S-RE SE&TSS TSS TEST-T1',
                employee_basic_info_table.c.level == 'E2'
                )
            )

    # query = employee_basic_info_table.select().where(
    #     or_(
    #         employee_basic_info_table.c.gid == 'Z0048HFZ',
    #         and_(
    #             employee_basic_info_table.c.org_code == 'RC-CN DI S-RE SE&TSS TSS TEST-T1',
    #             employee_basic_info_table.c.level == 'E6'
    #             )
    #         )
    # )

    result_set = conn.execute(query)

    for row in result_set:
        print(row.gid, row.name)


