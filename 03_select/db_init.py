import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:kinposh@8.136.221.2/study', echo=True)

meta_data = sqlalchemy.MetaData()

employee_basic_info_table = sqlalchemy.Table(
    "employee_basic_info", meta_data,
    sqlalchemy.Column("id"),
    sqlalchemy.Column("gid"),
    sqlalchemy.Column("name"),
    sqlalchemy.Column("mobile"),
    sqlalchemy.Column("location"),
    sqlalchemy.Column("org_code"),
    sqlalchemy.Column("org_id"),
    sqlalchemy.Column("country"),
    sqlalchemy.Column("are"),
    sqlalchemy.Column("company"),
    sqlalchemy.Column("company_unit"),
    sqlalchemy.Column("cost_center"),
    sqlalchemy.Column("report_to"),
    sqlalchemy.Column("level"),
    sqlalchemy.Column("image"),
    sqlalchemy.Column("employee_id"),
    sqlalchemy.Column("rate"),
    sqlalchemy.Column("state"),
    sqlalchemy.Column("create_time"),
    sqlalchemy.Column("modify_time"),
    sqlalchemy.Column("work_position"),
    sqlalchemy.Column("is_enable"),
    sqlalchemy.Column("gender"),
    sqlalchemy.Column("email"),
    sqlalchemy.Column("is_leave"),
    sqlalchemy.Column("work_time_is_fy"),
    sqlalchemy.Column("avaible_day"),
    sqlalchemy.Column("is_auto_approve"),
    sqlalchemy.Column("auto_approve_start_time"),
    sqlalchemy.Column("de_language"),
    sqlalchemy.Column("modify_by"),
    sqlalchemy.Column("level_suffix")
)


