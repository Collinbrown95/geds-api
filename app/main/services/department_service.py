from ..models.department import Department

def get_department_by_id(user_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        user_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Department.query.filter_by(id=user_id).first()