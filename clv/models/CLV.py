from .Data_Processing import *

class CLV():
    """
    Customer Lifetime Value (CLV) calculator using survival analysis and discounting.

    Parameters:
    -----------
    t : int
        Time for which CLV is calculated.

    Attributes:
    -----------
    t : int
        Time for which CLV is calculated.

    Methods:
    --------
    calculate_clv():
        Calculate the Customer Lifetime Value (CLV) based on survival probabilities and discounting.
    """
    def __init__(self, t):
        """
        Initialize the CLV calculator with the specified time 't'.

        Parameters:
        -----------
        t : int
            Time for which CLV is calculated.
        """
        self.t = t

    def calculate_clv(self):
        """
        Calculate the Customer Lifetime Value (CLV) based on survival probabilities and discounting.

        Returns:
        --------
        float:
            The calculated Customer Lifetime Value (CLV).
        """

        # Define the discount rate
        discount_rate = 0.1025  # 10.25% as a decimal

        # Get the monthly margins and probabilities for the customer
        monthly_margin = MM()
        customer_probabilities = p(self.t)

        # Calculate the CLV using the formula
        print(customer_probabilities)
        clv = 0
        for i in range(len(customer_probabilities)):
            clv += (customer_probabilities[i] / ((1 + discount_rate/12) ** (i-1)))

        clv *= monthly_margin

        return clv

# Example usage:
# Replace with your desired value for t
t = 40
clv_calculator = CLV(t)

clv = clv_calculator.calculate_clv()
print(f"CLV: ${clv:.2f}")
