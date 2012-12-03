report_types = {
    1: T("Violence"),
    2: T("No Service"),
    3: T("Corruption")
}



tablename = "feedback_report"
table = db.define_table(tablename,
                    Field("title",
                          label=T("Title of Report")),
                    Field("description",
                          label=T("Description of Report")),
	            Field("type", "integer",
                      requires=IS_IN_SET(report_types),
                      label=T("Type")),
		    s3db.pr_person_id(label=T("Name of Person")),
		    s3db.project_project_id(label=T("Name of Project")),
                    Field("reportingtime", "datetime",
                          label=T("Date & Time")),
                    *s3.meta_fields()
                    )


LIST_REPORT =  T("All Reports")
s3.crud_strings[tablename] = Storage(
    title_create = T("Add New Report"),
    title_list = LIST_REPORT,
    title_update = T("Edit Report"),
    title_search = T("Search Report"),
    subtitle_create = T("New Report"),
    subtitle_list = T("Report"),
    label_list_button = LIST_REPORT,
    label_create_button = T("Add New Report"),
    label_delete_button = T("Delete Report"),
    msg_record_created = T("Report Added"),
    msg_record_modified = T("Report Modified"),
    msg_record_deleted = T("Report Deleted"),
    msg_list_empty = T("No Report Exists!")) 



