from django.conf import settings

from kernel.models.roles.faculty_member import (
    AbstractFacultyMember,

    FacultyMember,
)
from kernel.models.roles.maintainer import (
    AbstractMaintainer,

    Maintainer,
)
from kernel.models.roles.student import (
    AbstractStudent,

    Student,
)

# Add the names of roles to the list maintained in settings
settings.ROLES.extend([
    'Student',
    'FacultyMember',
    'Maintainer',
])
