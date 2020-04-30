from flask import request
from flask_restx import Resource

from ..utils.dto import OrganizationDto
from ..services.employee_service import (get_employee_by_id,
                                         get_all_employees)

from ..models.organization import Organization as OrganizationModel

api = OrganizationDto.api
_organization = OrganizationDto.organization

@api.route("",
           doc={
               "description": "Organization/Business Unit within a Department<br>",
           })

@api.route("/<org_id>",
           doc={
               "description": "Single employee.<br>"
           })
@api.response(401, "Employee not found.")
class Organization(Resource):
    @api.doc("Single organization", description="Gets a single organization by its org_id.", params={"employee_id": "The integer id assigned to the organization in the database."})
    @api.marshal_with(_organization, 200)
    def get(self, employee_id):
        if get_employee_by_id(employee_id):
            return get_employee_by_id(employee_id).json()
        return abort(401, "Employee not found.")

    
