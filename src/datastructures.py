class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {"id": 1, "first_name": "John", "last_name": self.last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": self.last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": self.last_name, "age": 5, "lucky_numbers": [1]}
        ]
        self._next_id = 4  # Initial next id after predefined members

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        required_fields = ['first_name', 'age', 'lucky_numbers']
        for field in required_fields:
            if field not in member:
                return ValueError(f"Missing required field: {field}")

        # Generate a unique ID if not already provided
        if 'id' not in member:
            member['id'] = self._generate_id()
        else:
            # Ensure the provided ID is unique
            if any(m['id'] == member['id'] for m in self._members):
                return ValueError("ID already exists.")

        # Set the last name to the family's last name
        member['last_name'] = self.last_name

        # Append the member to the list
        self._members.append(member)
        return True

    def delete_member(self, id):
        initial_count = len(self._members)
        self._members = [member for member in self._members if member['id'] != id]
        if len(self._members) < initial_count:
            return True  # Member was deleted
        return False  # No member with the given id was found

    def get_member(self, id):
        return next((member for member in self._members if member['id'] == id), None)

    def get_all_members(self):
        return self._members
