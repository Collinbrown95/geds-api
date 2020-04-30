from ..models.organization import Organization
from ..models.employee import Employee

def get_organization_by_id(organization_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        organization_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Organization.query.filter_by(id=organization_id).first()

def get_employees_in_organization(organization_id):
    ''' Gets all employees who belong to a particular organizational unit. '''
    return [employee.json() for organization in Organization.query.filter_by(org_id=organization_id)]