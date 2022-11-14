
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
                "id": self._generateId(),
                "first_name": "Jose",
                "last_name": self.last_name,
                "age": 7,
                "lucky_numbers": [7, 13, 22] },

            {
                "id": self._generateId(),
                "first_name": "Hellen",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [10, 14, 3] },

            {
                "id": self._generateId(),
                "first_name": "Mikela",
                "last_name": self.last_name,
                "age": 12,
                "lucky_numbers": [1] }]

    
   