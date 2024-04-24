from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._staff = []
        self._opening_time = "9:00"

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def get_opening_time(self):
        return self._opening_time

    def set_opening_time(self, time):
        self._opening_time = time

    def add_staff(self, staff):
        self._staff.append(staff)

    def transfer_staff_member(self, staff, transfer_branch):
        if staff not in self._staff:
            return False

        self._staff.remove(staff)
        transfer_branch.add_staff(staff)
        return True

    def close_branch(self, transfer_branch):
        for staff in self._staff:
            self.transfer_staff_member(staff, transfer_branch)