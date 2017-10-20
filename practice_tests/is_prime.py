
class Prime_numbers():
    def is_number_prime(target):

        for index in range(2, target):
            if target % index == 0:
                return False
            return True
