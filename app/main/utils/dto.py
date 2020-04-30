from flask_restx import Namespace, fields


class AuthDto:
    api = Namespace('authorize', description="Authentication related operations")
    client_auth = api.model('auth_details', {
        'client_id': fields.String(required=True, description="The Client ID"),
        'client_secret': fields.String(required=True, description="The Client Secret"),
    })
    auth_resp = api.model('auth_resp', {
        'access_token': fields.String(required=True, description="The access token to be used in the Authentication "
                                                                 "header to validate subsequent requests.<br>Token "
                                                                 "expires in 24 hours")
    })


class ClientDto:
    api = Namespace('client', description="Client related operations")
    client = api.model('client', {
        'id': fields.String(required=True, description="The Client ID"),
        'name': fields.String(required=True, description="The Client name"),
        'secret': fields.String(required=True, description="The Client Secret"),
    })


class EmployeeDto:
    api = Namespace('employee', description="Employee related operations")
    employee = api.model('employee', {
        'employee_id': fields.Integer(required=True, description="The primary key for the employees table"),
        'first_name': fields.String(required=True, description="The employee's first name"),
        'last_name': fields.String(required=True, description="The employee's last name"),
        'job_title_en': fields.String(required=True, description="The employee's job title in English"),
        'job_title_fr': fields.String(required=True, description="The employee's job title in French"),
        'phone_number': fields.String(required=False, description="The employee's phone number"),
        'email': fields.String(required=False, description="The employee's email"),
        'address_en': fields.String(required=False, description="The employee's address in English"),
        'address_fr': fields.String(required=False, description="The employee's address in French"),
        'province_en': fields.String(required=False, description="The employee's province in English"),
        'province_fr': fields.String(required=False, description="The employee's province in French"),
        'city_en': fields.String(required=False, description="The employee's city in English"),
        'city_fr': fields.String(required=False, description="The employee's city in French"),
        'postal_code': fields.String(required=False, description="The employee's postal code"),
        'org_id': fields.String(required=True, description="The id of the organization the employee works in ",
                                                           "(foreign key for organizations table)"),
        'dept_id': fields.String(required=False, description="The id of the department where the employee works ",
                                                           "(foreign key for departments table)"),
    })

class OrganizationDto:
    api = Namespace('organization', description="Organization related operations")
    organization = api.model('organization', {
        'org_id': fields.Integer(required=True, description="The primary key for the organizations table"),
        'org_name_en': fields.String(required=True, description="The organization's name in English"),
        'org_name_fr': fields.String(required=True, description="The organization's name in French"),
        'dept_id': fields.String(required=False, description="The id of the department that the organization is in ",
                                                             "(foreign key for departments table)"),
        'org_chart_path': fields.String(required=True, description="A serialized array (list) containing the traversal ",
            "path to get from the root node of the department to the orgainzation unit. Example [0, 0, 4, 3, 1] specifies ",
            "a series of index positions required to arrive at a node from its department root."),
    })

class DepartmentDto:
    api = Namespace('organization', description="Organization related operations")
    department = api.model('organization', {
        'dept_id': fields.String(required=False, description="The id of the department that the organization is in"),
        'department_en': fields.String(required=True, description="The organization's name in English"),
        'department_fr': fields.String(required=True, description="The organization's name in French"),
        'org_chart_en': fields.String(required=True, description="A serialized json (dict) containing all of the organizations ",
                                                                  "in this department in English"),
        'org_chart_fr': fields.String(required=True, description="A serialized json (dict) containing all of the organizations ",
                                                                  "in this department in French"),
    })