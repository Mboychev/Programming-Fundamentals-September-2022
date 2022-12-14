"""Create a class Weapon. The __init__ method should receive a number of bullets (integer).
Create an attribute called bullets to store that number. The class should also have the following methods:
•	shoot()
o	If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
o	If there are no bullets left, return: "no bullets left"
•	__repr__()
o	Returns "Remaining bullets: {amount_of_bullets}"
o	You can read more about the method here: link
###################################EXAMPLES#######################################
Input:
4 5 3
1
1
0
Output: 14

Input:
5 10 6 3 5
2
4
1
1
3
0
0
Output: 51
"""


class Weapon:

    def __init__(self, bullets: int):

        self.bullets = int(bullets)

    def shoot(self):
        if self.bullets != 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

