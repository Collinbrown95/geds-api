from flask import request
from flask_restx import Resource

from ..utils.dto import DepartmentDto
from ..services.department_service import (get_department_by_id)

from ..models.department import Department as DepartmentModel

api = DepartmentDto.api
_department = DepartmentDto.department

@api.route("",
           doc={
               "description": "Department/Business Unit within a Department<br>",
           })

@api.route("/<dept_id>",
           doc={
               "description": "Single employee.<br>"
           })
@api.response(401, "Employee not found.")
class Department(Resource):
    @api.doc("Single department", description="Gets a single department by its dept_id.", params={"dept_id": "The integer id assigned to the department in the database."})
    @api.marshal_with(_department, 200)
    def get(self, dept_id):
        if get_department_by_id(dept_id):
            return get_department_by_id(dept_id).json()
        return abort(401, "Department not found.")

    
