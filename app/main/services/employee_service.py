from ..models.employee import Employee

def get_employee_by_id(user_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        user_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Employee.query.filter_by(employee_id=user_id).first()

def get_employees_in_organization(organization_id):
    ''' Gets all employees who belong to a particular organizational unit. '''
    return [employee.json() for employee in Employee.query.filter_by(org_id=organization_id)]