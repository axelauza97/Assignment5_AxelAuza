import sys


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


try:
    # Get values from form data
    input_string = sys.argv[1]
    threshold = sys.argv[2]

    # Split the input string by commas to get individual values
    inputs = input_string.split(",")

    if len(inputs) < 1:
        print(
            "<html><body><p>Error: At least one input value is required.</p></body></html>"
        )
        raise "Error"

    # Check if all inputs are integers
    if not all(is_integer(val.strip()) for val in inputs):
        print("<html><body><p>Error: All inputs must be integers.</p></body></html>")
        raise "Error"

    # Convert inputs to integers
    numbers = [int(val.strip()) for val in inputs]

    # Validate threshold
    if not is_integer(threshold):
        print("<html><body><p>Error: Threshold must be an integer.</p></body></html>")
        raise "Error"
    threshold = int(threshold)

    # Generate HTML output
    print("<html><head><title>Bitwise Operations Results</title></head><body>")
    print(f"<h2>Inputs: {', '.join(f'{val}' for val in numbers)}</h2>")

    # Bitwise operations
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    print(f"<p>Bitwise AND: {bitwise_and}</p>")
    print(f"<p>Bitwise OR: {bitwise_or}</p>")
    print(f"<p>Bitwise XOR: {bitwise_xor}</p>")

    # Filtering with loops
    greater_than_threshold = [num for num in numbers if num > threshold]
    print(
        f"<p>Numbers greater than {threshold}: {', '.join(map(str, greater_than_threshold))}</p>"
    )

    print("</body></html>")

except Exception as e:
    print(f"<html><body><p>Error: {str(e)}</p></body></html>")
