from clv.models import CLV

# Example usage:
if __name__ == "__main__":
    # Replace with your desired value for t
    t = 40
    clv_calculator = CLV(t)

    clv = clv_calculator.calculate_clv()
    print(f"CLV: ${clv:.2f}")